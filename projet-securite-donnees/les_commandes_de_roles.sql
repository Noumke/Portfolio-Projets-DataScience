-- (a) Création de comptes utilisateurs
-- Syntaxe de base 
-- CREATE USER nom_utilisateur WITH PASSWORD 'mot_de_passe' ENCRYPTED;

-- Exemples concrets 
CREATE USER dr_dupont WITH PASSWORD 'Medecin123';
CREATE USER infirmier_leclerc WITH PASSWORD 'Soins2025@';
CREATE USER admin_hopital WITH PASSWORD 'Adminhop25';

-- Pourquoi  
-- Chaque utilisateur a son propre compte (audit trail)
-- Mots de passe complexes exigés (politique de sécurité)
-- Compatible avec l'authentification PostgreSQL

-- (b) Création de rôles
-- Rôles principaux
CREATE ROLE administration;
CREATE ROLE medecin;
CREATE ROLE infirmier;
CREATE ROLE patient;

-- Sous-rôles spécialisés (créés comme rôles standards, mais seront hiérarchisés ensuite)
CREATE ROLE chirurgien;
CREATE ROLE pediatre;

-- Pourquoi 
-- Hiérarchisation des responsabilités
-- Facilité de gestion des permissions
-- Réutilisation des profils

-- (c) Attribution de rôles aux utilisateurs
-- Lier comptes individuels et profils génériques
GRANT medecin TO dr_dupont;
GRANT chirurgien TO dr_dupont;  -- Cumul possible
GRANT infirmier TO infirmier_leclerc;
GRANT administration TO admin_hopital;

-- Remarque  Pour révoquer un rôle d'un utilisateur, on peut utiliser 
-- REVOKE medecin FROM dr_dupont;

-- Pourquoi  
-- Principe de moindre privilège
-- Flexibilité (1 utilisateur = plusieurs rôles)
-- Cohérence avec l'organisation hospitalière

-- (d) Hiérarchie des rôles
-- Structure hiérarchique
GRANT infirmier TO medecin;  -- Tous les médecins héritent des droits infirmiers
GRANT pediatre TO medecin;   -- Les médecins peuvent avoir un sous-rôle spécifique
GRANT medecin TO administration;  -- L'admin a tous les droits, y compris ceux de médecin

-- Pourquoi 
-- Simplifie la gestion
-- Évite les doublons de permissions
-- Respecte la chaîne de responsabilité


-- 1. PRIVILÈGES ADMINISTRATION
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO administration;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO administration;
GRANT CREATE, TEMPORARY ON DATABASE hospital_db TO administration;

-- Pourquoi 
-- Contrôle total nécessaire pour la gestion globale de l'hôpital
-- Création d'objets pour les évolutions du système
-- Gestion des séquences pour maintenir l'intégrité des données auto-incrémentées

-- 2. PRIVILÈGES MÉDECINS

GRANT SELECT, INSERT, UPDATE ON
    diagnosis,  -- Accès complet aux diagnostics (colonnes diagnos_no, issue_date, treatment, remarks)
    examine,    -- Droit complet sur les examens médicaux
    appointment -- Gestion des rendez-vous
TO medecin;

GRANT SELECT ON
    patient,   -- Consultation des dossiers patients
    doctor,    -- Liste du personnel médical
    medicine,  -- Référence des médicaments
    hospital   -- Informations sur l'établissement
TO medecin;

REVOKE ALL ON 
    purchase,         -- Données financières sensibles
    medicine_country  -- Relations commerciales protégées
FROM medecin;

-- Pourquoi 
-- Accès complet au cœur métier médical (diagnostics, examens)
-- Consultation seule des données de référence
-- Protection stricte des informations financières et logistiques

-- 3. PRIVILÈGES INFIRMIERS

GRANT SELECT, UPDATE ON
    patient,  -- Mise à jour des informations patients
    nurse     -- Gestion du personnel infirmier
TO infirmier;

GRANT SELECT ON
    medicine,    -- Consultation des traitements
    appointment, -- Visualisation du planning
    visit        -- Suivi des présences
TO infirmier;

GRANT SELECT, UPDATE (treatment, remarks) ON diagnosis TO infirmier;

-- Pourquoi 
-- Mise à jour limitée aux champs relevant du suivi infirmier
-- Consultation nécessaire pour la coordination des soins
-- Impossible de modifier le diagnostic principal (issue_date, doc_id)

-- 4. PRIVILÈGES PATIENTS

CREATE OR REPLACE VIEW patient_info AS
SELECT 
    ssn,        -- Identifiant unique
    fname,      -- Prénom
    lname,      -- Nom
    age,        -- Âge
    gender,     -- Sexe
    nurse_id,   -- Identifiant de l'infirmier référent
    rec_id      -- Identifiant de la réception
FROM patient;

-- Pourquoi 
-- Protection des données sensibles (adresse, sécurité sociale)
-- Conformité RGPD
-- Accès strictement limité aux informations d'identité de base

-- 5. SÉCURITÉ DE BASE

REVOKE ALL ON ALL TABLES IN SCHEMA public FROM PUBLIC;
REVOKE ALL ON medicine_country, purchase FROM PUBLIC;

-- Pourquoi 
-- Politique de zero trust par défaut
-- Protection renforcée des données critiques
-- Nécessité d'accorder explicitement chaque droit nécessaire


-- SESSION 1  Connexion en tant que médecin (dr_dupont)



-- Ce médecin a les rôles  medecin, chirurgien
-- On suppose qu'on s'est connecté avec  c hospital_db dr_dupont
--doit reussir
--  Lire les rendez-vous des patients (car GRANT SELECT ON appointment TO medecin)
SELECT  FROM appointment;

--doit reussir
--  Insérer un nouveau diagnostic (car GRANT INSERT ON diagnosis TO medecin)
INSERT INTO diagnosis (diagnos_no, issue_date, treatment, remarks)
VALUES (30, '2025-05-11', 'Antibiotiques', 'Infection urinaire');

--doit echouer
--suppressiuon d'un element
delete from diagnosis where diagnos_no=30;

--doit echouer
--  Tentative d'accès aux données sensibles (purchase), qui est interdite même aux médecins
-- Devrait échouer avec une erreur de permission
SELECT  FROM purchase;



-- SESSION 2  Connexion en tant qu'infirmier (infirmier_leclerc)

-- Ce compte a le rôle infirmier
-- On suppose qu'on s'est connecté avec  c hospital_db infirmier_leclerc
--doit reussir
--  Mettre à jour un champ autorisé dans un diagnostic
UPDATE diagnosis SET treatment = 'Paracétamol 500mg'
WHERE diagnos_no =30;

--doit echouer
-- Modifier un champ interdit (issue_date), même si la table est accessible
-- Cela échoue car seul UPDATE(treatment, remarks) a été autorisé
UPDATE diagnosis SET issue_date = '2025-05-01'
WHERE diagnos_no = 30;

--doit reussir
--  Lire les rendez-vous, comme prévu
SELECT  FROM appointment;



-- SESSION 3  Connexion en tant qu’administrateur (admin_hopital)

-- Ce compte a le rôle administration
-- On suppose qu'on s'est connecté avec  c hospital_db admin_hopital
-- tout doit reussir
-- Supprimer une ligne de la table visit (ce rôle a TOUS les droits sauf purchase)
DELETE FROM visit WHERE patient_id = 1;

-- Créer une nouvelle table pour les tests
CREATE TABLE log_admin_actions (
    action_id SERIAL PRIMARY KEY,
    description TEXT,
    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

