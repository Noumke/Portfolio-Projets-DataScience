CREATE OR REPLACE VIEW comptes_dormants AS
SELECT 
    c.nom AS nom_client,
    c.prenom AS prenom_client,
    cp.numcpt,
    MAX(m.dt_mouvement) AS date_dernier_mouvement,
    SUM(m.montant) AS solde_compte
FROM compte cp
JOIN client c ON cp.id_client = c.id_client
JOIN mouvement m ON m.numcpt = cp.numcpt AND m.id_client = cp.id_client
GROUP BY c.nom, c.prenom, cp.numcpt, cp.id_client
HAVING MAX(m.dt_mouvement) < DATE '2021-12-31';

-- Export CSV
\COPY (SELECT * FROM comptes_dormants) TO 'C:/Users/ibtou/OneDrive/Con-Im-BD/comptes_dormants.csv' CSV HEADER;


CREATE OR REPLACE VIEW etat_parrainages AS
SELECT
    a.nom_agent,
    p_client.nom AS nom_parrain,
    f_client.nom AS nom_filleul,
    pr.date_parrainage,
    MAX(m.dt_mouvement) AS date_dernier_mouvement_parrain
FROM parrainage pr
JOIN client p_client ON pr.id_client_parrain = p_client.id_client
JOIN client f_client ON pr.id_client_filleul = f_client.id_client
JOIN agent a ON p_client.matricule_agent = a.matricule_agent
LEFT JOIN mouvement m ON m.id_client = p_client.id_client
WHERE pr.date_parrainage >= DATE '2022-01-01'
GROUP BY a.nom_agent, p_client.nom, f_client.nom, pr.date_parrainage;

-- Export CSV
\COPY (SELECT * FROM etat_parrainages) TO 'C:/Users/ibtou/OneDrive/Con-Im-BD/etat_parrainages.csv' CSV HEADER;
