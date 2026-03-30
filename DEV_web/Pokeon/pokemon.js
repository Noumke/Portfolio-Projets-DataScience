// lien de base vers l'API PokeAPI
const BASE_URL = "https://pokeapi.co/api/v2";

// on récupère tous les éléments HTML dont on a besoin
const searchInput  = document.getElementById("searchInput");
const searchBtn    = document.getElementById("searchBtn");
const pokeResult   = document.getElementById("pokeResult");
const pokeListBox  = document.getElementById("pokeListBox");
const berryListBox = document.getElementById("berryListBox");
const berryDetail  = document.getElementById("berryDetail");
const genSelect    = document.getElementById("genSelect");
const tabBtns      = document.querySelectorAll(".tab-btn");
const tabPanels    = document.querySelectorAll(".tab-panel");
const cryAudio     = document.getElementById("cryAudio");
const scanLine     = document.getElementById("scanLine");

// GESTION DES ONGLETS
tabBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    // on enlève la classe active de tous les onglets
    tabBtns.forEach(b => b.classList.remove("active"));
    tabPanels.forEach(p => p.classList.remove("active"));

    // puis on active celui sur lequel on a cliqué
    btn.classList.add("active");
    document.getElementById(btn.dataset.tab).classList.add("active");
  });
});

// fonction pour afficher un message d'erreur
function showError(container, message) {
  container.innerHTML = `<p class="error-msg">${message}</p>`;
}

// lance l'animation de la ligne de scan
function triggerScan() {
  scanLine.classList.remove("scanning");
  void scanLine.offsetWidth; // petit trick pour forcer le reflow et relancer l'animation
  scanLine.classList.add("scanning");
}

// RECHERCHE D'UN POKEMON PAR NUMERO

searchBtn.addEventListener("click", () => {
  const id = parseInt(searchInput.value.trim());
  if (!id || id < 1) {
    showError(pokeResult, "Entrez un numéro de Pokémon valide (minimum 1).");
    return;
  }
  fetchPokemon(id);
});

// on peut aussi appuyer sur Entrée pour lancer la recherche
searchInput.addEventListener("keydown", e => {
  if (e.key === "Enter") searchBtn.click();
});

async function fetchPokemon(id) {
  pokeResult.innerHTML = `<p class="loading">[ SCAN EN COURS... ]</p>`;
  triggerScan();

  try {
    // on appelle l'API pour récupérer les infos du pokémon
    const res  = await fetch(`${BASE_URL}/pokemon/${id}`);
    if (!res.ok) throw new Error("Pokémon introuvable.");
    const data = await res.json();

    // on récupère aussi les infos de l'espèce pour avoir la description
    const specRes  = await fetch(`${BASE_URL}/pokemon-species/${id}`);
    const specData = await specRes.json();

    // on cherche d'abord la description en français, sinon on prend l'anglais
    const entry = specData.flavor_text_entries.find(
      e => e.language.name === "fr"
    ) || specData.flavor_text_entries.find(
      e => e.language.name === "en"
    );
    const description = entry
      ? entry.flavor_text.replace(/\f|\n/g, " ")
      : "Aucune description disponible.";

    // URL du fichier audio du cri
    const cryUrl = data.cries?.latest || data.cries?.legacy || null;

    renderPokemon(data, description, cryUrl);
  } catch (err) {
    showError(pokeResult, err.message);
  }
}

function renderPokemon(data, description, cryUrl) {
  // on génère les badges de type
  const types = data.types
    .map(t => `<span class="badge type-${t.type.name}">${t.type.name.toUpperCase()}</span>`)
    .join(" ");

  // on génère les barres de statistiques
  const stats = data.stats
    .map(s => `
      <div class="stat-row">
        <span class="stat-label">${s.stat.name.toUpperCase()}</span>
        <div class="stat-bar-bg">
          <div class="stat-bar" style="width:${Math.min(s.base_stat, 255) / 255 * 100}%"></div>
        </div>
        <span class="stat-val">${s.base_stat}</span>
      </div>`).join("");

  // on prend l'image officielle, sinon le sprite de base
  const imgUrl = data.sprites.other["official-artwork"].front_default
    || data.sprites.front_default;

  pokeResult.innerHTML = `
    <div class="poke-card">
      <div class="poke-header">
        <span class="poke-id">#${String(data.id).padStart(4,"0")}</span>
        <span class="poke-name">${data.name.toUpperCase()}</span>
        <div class="poke-types">${types}</div>
      </div>
      <div class="poke-body">
        <div class="poke-visual">
          <img src="${imgUrl}" alt="${data.name}" class="poke-img" />
          ${cryUrl ? `<button class="cry-btn" id="playCry" title="Écouter le cri">CRI</button>` : ""}
        </div>
        <div class="poke-info">
          <p class="poke-desc">${description}</p>
          <div class="poke-meta">
            <span>Poids : ${data.weight / 10} kg</span>
            <span>Taille : ${data.height / 10} m</span>
          </div>
          <div class="stats-block">${stats}</div>
        </div>
      </div>
    </div>`;

  // on branche le bouton pour jouer le cri si l'URL existe
  if (cryUrl) {
    document.getElementById("playCry").addEventListener("click", () => {
      cryAudio.src = cryUrl;
      cryAudio.play();
    });
  }
}

// LISTE DES POKEMONS PAR GENERATION

// plages d'ID pour chaque génération
const GENERATIONS = {
  "all":  [1, 1025],
  "gen1": [1, 151],
  "gen2": [152, 251],
  "gen3": [252, 386],
  "gen4": [387, 493],
  "gen5": [494, 649],
  "gen6": [650, 721],
  "gen7": [722, 809],
  "gen8": [810, 905],
  "gen9": [906, 1025],
};

genSelect.addEventListener("change", () => loadPokeList(genSelect.value));

async function loadPokeList(gen = "all") {
  pokeListBox.innerHTML = `<p class="loading">[ CHARGEMENT... ]</p>`;
  const [start, end] = GENERATIONS[gen];
  const limit = end - start + 1;

  try {
    const res  = await fetch(`${BASE_URL}/pokemon?limit=${limit}&offset=${start - 1}`);
    const data = await res.json();
    renderPokeList(data.results);
  } catch {
    showError(pokeListBox, "Impossible de charger la liste.");
  }
}

function renderPokeList(pokemons) {
  pokeListBox.innerHTML = "";

  pokemons.forEach((p, idx) => {
    const item = document.createElement("div");
    item.className = "list-item";
    // on extrait le numéro depuis l'URL renvoyée par l'API
    const id = p.url.split("/").filter(Boolean).pop();
    item.innerHTML = `<span class="list-id">#${String(parseInt(id)).padStart(4,"0")}</span> ${p.name.toUpperCase()}`;

    // clic sur un pokémon de la liste : on affiche sa fiche
    item.addEventListener("click", () => {
      searchInput.value = id;
      tabBtns[0].click(); // on revient sur l'onglet recherche
      fetchPokemon(parseInt(id));
    });

    pokeListBox.appendChild(item);
  });
}

// LISTE DES BAIES

async function loadBerryList() {
  berryListBox.innerHTML = `<p class="loading">[ CHARGEMENT... ]</p>`;

  try {
    // l'API contient 64 baies au total
    const res  = await fetch(`${BASE_URL}/berry?limit=64`);
    const data = await res.json();
    renderBerryList(data.results);
  } catch {
    showError(berryListBox, "Impossible de charger les baies.");
  }
}

function renderBerryList(berries) {
  berryListBox.innerHTML = "";

  berries.forEach(b => {
    const item = document.createElement("div");
    item.className = "list-item berry-item";
    item.textContent = b.name.toUpperCase();

    // clic sur une baie pour voir ses détails à droite
    item.addEventListener("click", () => {
      document.querySelectorAll(".berry-item").forEach(el => el.classList.remove("selected"));
      item.classList.add("selected");
      fetchBerryDetail(b.url);
    });

    berryListBox.appendChild(item);
  });
}

async function fetchBerryDetail(url) {
  berryDetail.innerHTML = `<p class="loading">[ ANALYSE... ]</p>`;

  try {
    const res  = await fetch(url);
    const data = await res.json();

    // on récupère la description de l'objet correspondant à la baie
    const itemRes  = await fetch(data.item.url);
    const itemData = await itemRes.json();

    const desc = itemData.flavor_text_entries.find(
      e => e.language.name === "fr"
    ) || itemData.flavor_text_entries.find(
      e => e.language.name === "en"
    );

    const description = desc
      ? desc.text.replace(/\f|\n/g, " ")
      : "Aucune description disponible.";

    // l'image du sprite de la baie est dans itemData.sprites.default
    const imgUrl = itemData.sprites.default || null;

    // on affiche toutes les caractéristiques de la baie
    berryDetail.innerHTML = `
      <div class="berry-card">
        <h3 class="berry-title">${data.name.toUpperCase()}</h3>
        ${imgUrl ? `<img src="${imgUrl}" alt="${data.name}" style="width:64px;height:64px;object-fit:contain;margin-bottom:10px;image-rendering:pixelated;" />` : ""}
        <p class="poke-desc">${description}</p>
        <div class="berry-stats">
          <div class="berry-row"><span>Taille</span><span>${data.size} mm</span></div>
          <div class="berry-row"><span>Fermeté</span><span>${data.firmness.name}</span></div>
          <div class="berry-row"><span>Temps de croissance</span><span>${data.growth_time} h</span></div>
          <div class="berry-row"><span>Douceur</span><span>${data.smoothness}</span></div>
          <div class="berry-row"><span>Saveur dominante</span>
            <span>${data.flavors.reduce((a,b) => b.potency>a.potency ? b : a, data.flavors[0])?.flavor?.name || "?"}</span>
          </div>
        </div>
      </div>`;
  } catch {
    showError(berryDetail, "Erreur lors du chargement de la baie.");
  }
}

// COMPARATEUR DE DEUX POKEMONS (bonus)

const compareInput1 = document.getElementById("compareInput1");
const compareInput2 = document.getElementById("compareInput2");
const compareBtn    = document.getElementById("compareBtn");
const compareResult = document.getElementById("compareResult");

compareBtn.addEventListener("click", async () => {
  const id1 = parseInt(compareInput1.value.trim());
  const id2 = parseInt(compareInput2.value.trim());

  if (!id1 || !id2 || id1 < 1 || id2 < 1) {
    showError(compareResult, "Entrez deux numéros valides.");
    return;
  }

  compareResult.innerHTML = `<p class="loading">[ COMPARAISON EN COURS... ]</p>`;

  try {
    // on charge les deux pokémons en parallèle avec Promise.all
    const [r1, r2] = await Promise.all([
      fetch(`${BASE_URL}/pokemon/${id1}`).then(r => r.json()),
      fetch(`${BASE_URL}/pokemon/${id2}`).then(r => r.json()),
    ]);

    renderComparison(r1, r2);
  } catch {
    showError(compareResult, "Erreur lors du chargement des Pokémons.");
  }
});

function renderComparison(p1, p2) {
  const statNames = p1.stats.map(s => s.stat.name);

  // pour chaque stat on compare les deux valeurs et on met en évidence le gagnant
  const rows = statNames.map(name => {
    const v1 = p1.stats.find(s => s.stat.name === name).base_stat;
    const v2 = p2.stats.find(s => s.stat.name === name).base_stat;
    const winner = v1 > v2 ? "left" : v2 > v1 ? "right" : "tie";

    return `
      <div class="cmp-row">
        <span class="cmp-val ${winner === "left" ? "cmp-win" : ""}">${v1}</span>
        <span class="cmp-stat">${name.toUpperCase()}</span>
        <span class="cmp-val ${winner === "right" ? "cmp-win" : ""}">${v2}</span>
      </div>`;
  }).join("");

  const img1 = p1.sprites.other["official-artwork"].front_default || p1.sprites.front_default;
  const img2 = p2.sprites.other["official-artwork"].front_default || p2.sprites.front_default;

  compareResult.innerHTML = `
    <div class="cmp-header">
      <div class="cmp-side">
        <img src="${img1}" class="cmp-img" alt="${p1.name}" />
        <span class="cmp-name">${p1.name.toUpperCase()}</span>
      </div>
      <span class="cmp-vs">VS</span>
      <div class="cmp-side">
        <img src="${img2}" class="cmp-img" alt="${p2.name}" />
        <span class="cmp-name">${p2.name.toUpperCase()}</span>
      </div>
    </div>
    <div class="cmp-rows">${rows}</div>`;
}

// INITIALISATION au chargement de la page
window.addEventListener("DOMContentLoaded", () => {
  loadPokeList("all");
  loadBerryList();
});
