
-- Création de la table AGENT (sans dépendances)
CREATE TABLE agent (
    matricule_agent BIGINT PRIMARY KEY,
    nom_agent VARCHAR(50) NOT NULL,
    ddn_agent DATE,
    civilite_agent VARCHAR(10)
);

-- Création de la table CLIENT (dépend de AGENT)
CREATE TABLE client (
    id_client BIGINT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    civilite VARCHAR(10),
    ddn DATE,
    adresse TEXT,
    cp VARCHAR(10),
    ville VARCHAR(50),
    matricule_agent BIGINT,
    CONSTRAINT fk_client_agent FOREIGN KEY (matricule_agent) REFERENCES agent(matricule_agent)
);

-- Création de la table COMPTE (dépend de CLIENT) avec clé primaire composite
CREATE TABLE compte (
    numcpt BIGINT NOT NULL,
    designation_compte VARCHAR(100),
    date_rattachement DATE,
    type_rattachement VARCHAR(50),
    id_client BIGINT NOT NULL,
    CONSTRAINT pk_compte PRIMARY KEY (id_client, numcpt)
);

-- création de la table mouvement 
CREATE TABLE mouvement (
    id SERIAL PRIMARY KEY,
    id_mouvement BIGINT,
    dt_mouvement DATE NOT NULL,
    montant NUMERIC(15,2) NOT NULL,
    designation_mouvement VARCHAR(100),
    numcpt BIGINT NOT NULL,
    id_client BIGINT NOT NULL,
    CONSTRAINT fk_mouvement_compte FOREIGN KEY (numcpt, id_client)
        REFERENCES compte(numcpt, id_client)
);



-- Création de la table PARRAINAGE (dépend de CLIENT ×2)
CREATE TABLE parrainage (
    id_parrainage SERIAL PRIMARY KEY,
    id_client_parrain BIGINT NOT NULL,
    id_client_filleul BIGINT NOT NULL,
    date_parrainage DATE NOT NULL,
    nom_parrain VARCHAR(100),
    CONSTRAINT unique_couple_parrain_filleul UNIQUE (id_client_parrain, id_client_filleul),
    CONSTRAINT fk_parrain FOREIGN KEY (id_client_parrain) REFERENCES client(id_client),
    CONSTRAINT fk_filleul FOREIGN KEY (id_client_filleul) REFERENCES client(id_client)

);
ALTER TABLE parrainage
ADD CONSTRAINT unique_filleul UNIQUE (id_client_filleul); --un filleul ne peut etre parrainer q'une seule fois 