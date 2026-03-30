// ID de l'animal en cours de modification d'arme (utilisé dans plusieurs fonctions)
let currentAnimalId = null;

// affiche un message temporaire (succès ou erreur) qui disparaît après 3 secondes
function showMsg(id, msg, isError = false) {
  const el = document.getElementById(id);
  if (!el) return;
  el.className   = isError ? 'msg-error' : 'msg-success';
  el.textContent = msg;
  setTimeout(() => el.textContent = '', 3000);
}

// GESTION DES ONGLETS

document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    // on désactive tous les onglets puis on active celui cliqué
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(btn.dataset.tab).classList.add('active');
  });
});

// BARRE D'AUTHENTIFICATION

function updateAuthUI() {
  const badge      = document.getElementById('userBadge');
  const btn        = document.getElementById('authBtn');
  const weaponCard = document.getElementById('createWeaponCard');

  if (TOKEN) {
    // on affiche le nom de l'utilisateur connecté
    badge.textContent   = USERNAME;
    badge.style.display = 'inline-block';
    btn.textContent     = 'DECONNEXION';
    if (weaponCard) weaponCard.style.display = 'block';
  } else {
    badge.style.display = 'none';
    btn.textContent     = 'CONNEXION';
    if (weaponCard) weaponCard.style.display = 'none';
  }
}

// MON ARMEE

async function loadMyArmy() {
  if (!TOKEN) return;
  const { ok, data, status } = await api('/my-army/');
  const container = document.getElementById('myArmyInfo');

  if (ok) {
    // on affiche les infos de l'armée
    container.innerHTML = `
      <div class="army-header">
        <div>
          <div class="army-name">${data.name}</div>
          <div class="army-owner">Commandant : ${data.owner.username}</div>
          <span class="badge badge-count">${data.animal_count} animaux</span>
        </div>
        <button class="btn btn-ghost" onclick="showArmyForm('${data.name}','${data.description}')">MODIFIER</button>
      </div>
      <p class="army-desc" style="margin-top:.75rem;">${data.description || '—'}</p>`;
  } else if (status === 404) {
    // l'utilisateur n'a pas encore créé d'armée
    container.innerHTML = `
      <p style="color:var(--muted);margin-bottom:1rem;">Vous n'avez pas encore d'armée.</p>
      <button class="btn btn-primary" onclick="showArmyForm()">CREER MON ARMEE</button>`;
  }
}

function showArmyForm(name = '', desc = '') {
  // on pré-remplit le formulaire si on modifie une armée existante
  document.getElementById('armyName').value = name;
  document.getElementById('armyDesc').value = desc;
  document.getElementById('armyForm').style.display = 'block';
}

async function saveArmy() {
  const name        = document.getElementById('armyName').value.trim();
  const description = document.getElementById('armyDesc').value.trim();
  if (!name) { showMsg('armyFormMsg', 'Nom requis.', true); return; }

  // on essaie de créer l'armée, si elle existe déjà on la modifie
  let { ok, data } = await api('/my-army/', 'POST', { name, description });
  if (!ok) ({ ok, data } = await api('/my-army/', 'PUT', { name, description }));

  if (ok) {
    showMsg('armyFormMsg', 'Armée sauvegardée !');
    document.getElementById('armyForm').style.display = 'none';
    loadMyArmy();
  } else {
    showMsg('armyFormMsg', JSON.stringify(data), true);
  }
}

// MES ANIMAUX

async function loadMyAnimals() {
  if (!TOKEN) return;
  const { ok, data } = await api('/my-army/animals/');
  const grid = document.getElementById('myAnimalsGrid');

  if (!ok || !data.length) {
    grid.innerHTML = '<p class="loading">Aucun animal dans votre armée.</p>';
    return;
  }
  // on affiche chaque animal avec ses boutons d'action
  grid.innerHTML = data.map(a => renderAnimalCard(a, true)).join('');
}

function renderAnimalCard(a, withActions = false) {
  // image de l'animal ou placeholder si pas d'URL
  const imgHtml = a.image_url
    ? `<img src="${a.image_url}" class="animal-img" alt="${a.name}"
         onerror="this.parentNode.innerHTML='<div class=animal-img-placeholder>?</div>'">`
    : `<div class="animal-img-placeholder">?</div>`;

  // on affiche l'arme ou "sans arme" si l'animal n'en a pas
  const weaponHtml = a.weapon
    ? `<div class="weapon-tag">${a.weapon.name} (${a.weapon.damage} dmg)</div>`
    : `<div class="weapon-tag" style="opacity:.4">— sans arme —</div>`;

  // les boutons d'action ne s'affichent que pour le propriétaire
  const actions = withActions ? `
    <div class="animal-actions">
      <button class="btn btn-ghost" style="font-size:.7rem;padding:.3rem .6rem"
        onclick="openWeaponModal(${a.id},'${a.name}')">ARME</button>
      <button class="btn btn-danger" style="font-size:.7rem;padding:.3rem .6rem"
        onclick="removeAnimal(${a.id})">RETIRER</button>
    </div>` : '';

  return `
    <div class="animal-card">
      ${imgHtml}
      <div class="animal-body">
        <div class="animal-name">${a.name.toUpperCase()}</div>
        <div class="animal-breed">${a.breed || '?'}</div>
        ${weaponHtml}
        ${actions}
      </div>
    </div>`;
}

function toggleAddAnimalForm() {
  const f = document.getElementById('addAnimalForm');
  f.style.display = f.style.display === 'none' ? 'block' : 'none';
}

async function addAnimal() {
  const name      = document.getElementById('animalName').value.trim();
  const breed     = document.getElementById('animalBreed').value.trim();
  const image_url = document.getElementById('animalImg').value.trim();
  if (!name) { showMsg('addAnimalMsg', 'Nom requis.', true); return; }

  const { ok, data } = await api('/my-army/animals/', 'POST', { name, breed, image_url });
  if (ok) {
    showMsg('addAnimalMsg', `${name} ajouté à l'armée !`);
    // on vide le formulaire après ajout
    document.getElementById('animalName').value  = '';
    document.getElementById('animalBreed').value = '';
    document.getElementById('animalImg').value   = '';
    loadMyAnimals();
    loadMyArmy();
  } else {
    showMsg('addAnimalMsg', (data.error || JSON.stringify(data)), true);
  }
}

async function removeAnimal(id) {
  if (!confirm("Supprimer cet animal de l'armée ?")) return;
  const { ok } = await api(`/my-army/animals/${id}/`, 'DELETE');
  if (ok) { loadMyAnimals(); loadMyArmy(); }
}

// ARME D'UN ANIMAL

async function openWeaponModal(animalId, animalName) {
  currentAnimalId = animalId;
  document.getElementById('weaponAnimalName').textContent = animalName;
  document.getElementById('weaponModalMsg').textContent   = '';

  // on charge la liste des armes pour remplir le select
  const { ok, data } = await api('/weapons/');
  const sel = document.getElementById('weaponSelect');
  sel.innerHTML = '<option value="">— Sélectionner —</option>';
  if (ok) {
    data.forEach(w => {
      const opt = document.createElement('option');
      opt.value       = w.id;
      opt.textContent = `${w.name} (${w.damage} dmg)`;
      sel.appendChild(opt);
    });
  }
  document.getElementById('weaponModal').classList.remove('hidden');
}

function closeWeaponModal() {
  document.getElementById('weaponModal').classList.add('hidden');
  currentAnimalId = null;
}

async function assignWeapon() {
  const weaponId  = document.getElementById('weaponSelect').value;
  const newName   = document.getElementById('newWeaponName').value.trim();
  const newDamage = document.getElementById('newWeaponDamage').value;
  const newDesc   = document.getElementById('newWeaponDesc').value.trim();

  let body;
  if (weaponId) {
    // on assigne une arme existante par son ID
    body = { weapon_id: parseInt(weaponId) };
  } else if (newName) {
    // on crée une nouvelle arme et on l'assigne directement
    body = { name: newName, damage: parseInt(newDamage) || 0, description: newDesc };
  } else {
    showMsg('weaponModalMsg', 'Choisir une arme ou en créer une.', true);
    return;
  }

  const { ok, data } = await api(`/animals/${currentAnimalId}/weapon/`, 'POST', body);
  if (ok) {
    showMsg('weaponModalMsg', 'Arme assignée !');
    setTimeout(() => { closeWeaponModal(); loadMyAnimals(); loadWeapons(); }, 1000);
  } else {
    showMsg('weaponModalMsg', (data.error || JSON.stringify(data)), true);
  }
}

async function removeWeapon() {
  // on retire l'arme de l'animal sans la supprimer de la base
  const { ok } = await api(`/animals/${currentAnimalId}/weapon/`, 'DELETE');
  if (ok) { closeWeaponModal(); loadMyAnimals(); }
}

// VUE PUBLIQUE — TOUTES LES ARMEES

async function loadPublicArmies() {
  const container = document.getElementById('publicArmiesContainer');
  const { ok, data } = await api('/armies/');

  if (!ok || !data.length) {
    container.innerHTML = '<p class="loading">Aucune armée enregistrée.</p>';
    return;
  }
  container.innerHTML = data.map(army => {
    // on construit la liste des animaux de l'armée
    const animalsHtml = army.animals.map(a => {
      const weapon = a.weapon ? a.weapon.name : '—';
      return `<div class="pub-animal-chip">${a.name}
        <span style="color:var(--muted);font-size:.65rem">${weapon}</span></div>`;
    }).join('');

    return `
      <div class="pub-army">
        <div class="pub-army-name">${army.name}
          <span class="badge badge-count">${army.animal_count} animaux</span>
        </div>
        <div class="pub-army-owner">${army.owner.username}</div>
        <div class="army-desc">${army.description || '—'}</div>
        <div class="pub-animal-list">
          ${animalsHtml || '<span style="color:var(--muted);font-size:.8rem">Aucun animal</span>'}
        </div>
      </div>`;
  }).join('');
}

// ARMES DISPONIBLES

async function loadWeapons() {
  const container = document.getElementById('weaponsList');
  const { ok, data } = await api('/weapons/');

  if (!ok || !data.length) {
    container.innerHTML = '<p class="loading">Aucune arme disponible.</p>';
    return;
  }
  // on calcule la barre de progression par rapport au max
  const dmgMax = Math.max(...data.map(w => w.damage));
  container.innerHTML = `<div class="animal-grid">` + data.map(w => {
    const pct = dmgMax ? Math.round(w.damage / dmgMax * 100) : 0;
    return `
      <div class="weapon-card" style="flex-direction:column;align-items:flex-start;">
        <div style="display:flex;align-items:center;gap:.75rem;width:100%">
          <div>
            <div class="weapon-name">${w.name}</div>
            <div class="weapon-dmg">${w.damage} points de dégâts</div>
          </div>
        </div>
        <div style="width:100%;background:var(--border);border-radius:3px;height:6px;margin-top:.5rem;">
          <div style="width:${pct}%;background:var(--accent);height:100%;border-radius:3px;"></div>
        </div>
        <p style="font-size:.75rem;color:var(--muted);margin-top:.4rem;">${w.description || '—'}</p>
      </div>`;
  }).join('') + `</div>`;
}

async function createWeapon() {
  const name        = document.getElementById('wName').value.trim();
  const damage      = parseInt(document.getElementById('wDamage').value) || 0;
  const description = document.getElementById('wDesc').value.trim();
  if (!name) { showMsg('weaponCreateMsg', 'Nom requis.', true); return; }

  const { ok, data } = await api('/weapons/', 'POST', { name, damage, description });
  if (ok) {
    showMsg('weaponCreateMsg', `${name} créée !`);
    document.getElementById('wName').value   = '';
    document.getElementById('wDamage').value = '';
    document.getElementById('wDesc').value   = '';
    loadWeapons();
  } else {
    showMsg('weaponCreateMsg', JSON.stringify(data), true);
  }
}

// INITIALISATION au chargement de la page
window.addEventListener('DOMContentLoaded', () => {
  updateAuthUI();     // on met à jour la barre selon le token sauvegardé
  loadPublicArmies(); // on charge les armées publiques
  loadWeapons();      // on charge la liste des armes

  // si l'utilisateur était déjà connecté on charge ses données
  if (TOKEN) {
    loadMyArmy();
    loadMyAnimals();
  }
});
