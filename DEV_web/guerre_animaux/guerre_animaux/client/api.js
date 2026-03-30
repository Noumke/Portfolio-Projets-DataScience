// URL de base de l'API Django
const API_BASE = 'http://127.0.0.1:8000/api';

// token et nom d'utilisateur récupérés depuis le localStorage
let TOKEN    = localStorage.getItem('token')    || null;
let USERNAME = localStorage.getItem('username') || null;

// FONCTION GENERIQUE D'APPEL API
async function api(endpoint, method = 'GET', body = null) {
  const headers = { 'Content-Type': 'application/json' };

  // on ajoute le token dans les headers si l'utilisateur est connecté
  if (TOKEN) headers['Authorization'] = `Token ${TOKEN}`;

  const options = { method, headers };
  if (body) options.body = JSON.stringify(body);

  const response = await fetch(`${API_BASE}${endpoint}`, options);

  // une réponse 204 (No Content) ne contient pas de JSON
  const data = response.status === 204 ? null : await response.json();
  return { ok: response.ok, status: response.status, data };
}

// CONNEXION DE L'UTILISATEUR
async function doLogin() {
  const username = document.getElementById('loginUsername').value.trim();
  const password = document.getElementById('loginPassword').value;

  const { ok, data } = await api('/auth/login/', 'POST', { username, password });
  if (ok) {
    // on sauvegarde le token dans le localStorage pour garder la session
    TOKEN    = data.token;
    USERNAME = data.user.username;
    localStorage.setItem('token',    TOKEN);
    localStorage.setItem('username', USERNAME);

    document.getElementById('loginModal').classList.add('hidden');
    document.getElementById('loginError').textContent = '';
    updateAuthUI();
    loadMyArmy();
    loadMyAnimals();
  } else {
    document.getElementById('loginError').textContent = (data.error || 'Erreur de connexion.');
  }
}

// DECONNEXION DE L'UTILISATEUR
async function doLogout() {
  // on supprime le token côté serveur
  await api('/auth/logout/', 'POST');

  // on nettoie le localStorage et l'état local
  TOKEN = null;
  USERNAME = null;
  localStorage.removeItem('token');
  localStorage.removeItem('username');

  updateAuthUI();
  document.getElementById('myArmyInfo').innerHTML    = '<p class="loading">Connectez-vous pour voir votre armée.</p>';
  document.getElementById('myAnimalsGrid').innerHTML = '';
}

// bascule entre connexion et déconnexion selon l'état actuel
function toggleAuth() {
  if (TOKEN) {
    doLogout();
  } else {
    document.getElementById('loginModal').classList.remove('hidden');
  }
}

// on peut aussi appuyer sur Entrée dans le champ mot de passe
document.getElementById('loginPassword').addEventListener('keydown', e => {
  if (e.key === 'Enter') doLogin();
});
