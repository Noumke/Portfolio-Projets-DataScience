import sqlite3
import os
from loguru import logger

#Importer le chemin de la base depuis settings local
from settings import DB_PATH


def get_connection() -> sqlite3.Connection:
    #Créer le dossier parent seulement s'il existe dans le chemin
    dossier = os.path.dirname(DB_PATH)
    if dossier:
        os.makedirs(dossier, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    #Initialiser toutes les tables de la base de données
    conn = get_connection()
    cursor = conn.cursor()

    #Créer la table des classements de ligue
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS classements (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            ligue        TEXT    NOT NULL,
            equipe       TEXT    NOT NULL,
            rang         INTEGER,
            matchs       INTEGER,
            victoires    INTEGER,
            nuls         INTEGER,
            defaites     INTEGER,
            buts_pour    INTEGER,
            buts_contre  INTEGER,
            difference   INTEGER,
            points       INTEGER,
            saison       TEXT    NOT NULL,
            UNIQUE(ligue, equipe, saison)
        )
    """)

    #Créer la table des résultats de matchs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resultats (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            ligue      TEXT NOT NULL,
            semaine    INTEGER,
            date_match TEXT,
            heure      TEXT,
            domicile   TEXT,
            exterieur  TEXT,
            score      TEXT,
            xg_dom     REAL,
            xg_ext     REAL,
            saison     TEXT NOT NULL
        )
    """)

    #Créer la table des statistiques des joueurs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stats_joueurs (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id   TEXT,
            joueur      TEXT NOT NULL,
            nation      TEXT,
            equipe      TEXT,
            ligue       TEXT,
            age         TEXT,
            poste       TEXT,
            matchs      INTEGER,
            titulaire   INTEGER,
            minutes     INTEGER,
            buts        INTEGER,
            passes_dec  INTEGER,
            xg          REAL,
            xag         REAL,
            saison      TEXT NOT NULL,
            UNIQUE(player_id, ligue, saison)
        )
    """)

    #Créer la table des statistiques des équipes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stats_equipes (
            id             INTEGER PRIMARY KEY AUTOINCREMENT,
            equipe         TEXT NOT NULL,
            ligue          TEXT NOT NULL,
            matchs         INTEGER,
            buts_marques   INTEGER,
            buts_encaisses INTEGER,
            xg             REAL,
            xga            REAL,
            possession     REAL,
            saison         TEXT NOT NULL,
            UNIQUE(equipe, ligue, saison)
        )
    """)

    #Créer la table des images joueurs téléchargées
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS images_joueurs (
            player_id  TEXT PRIMARY KEY,
            joueur     TEXT,
            chemin     TEXT,
            telecharge INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()
    logger.success("Base de données initialisée avec succès")


def insert_classement(rows: list) -> None:
    #Insérer ou mettre à jour les données de classement
    if not rows:
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT OR REPLACE INTO classements
            (ligue, equipe, rang, matchs, victoires, nuls, defaites,
             buts_pour, buts_contre, difference, points, saison)
        VALUES
            (:ligue, :equipe, :rang, :matchs, :victoires, :nuls, :defaites,
             :buts_pour, :buts_contre, :difference, :points, :saison)
    """, rows)
    conn.commit()
    conn.close()
    logger.success(f"{len(rows)} lignes classement insérées")


def insert_resultats(rows: list) -> None:
    #Insérer les résultats de matchs
    if not rows:
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT INTO resultats
            (ligue, semaine, date_match, heure, domicile, exterieur,
             score, xg_dom, xg_ext, saison)
        VALUES
            (:ligue, :semaine, :date_match, :heure, :domicile, :exterieur,
             :score, :xg_dom, :xg_ext, :saison)
    """, rows)
    conn.commit()
    conn.close()
    logger.success(f"{len(rows)} résultats insérés")


def insert_stats_joueurs(rows: list) -> None:
    #Insérer ou mettre à jour les statistiques des joueurs
    if not rows:
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT OR REPLACE INTO stats_joueurs
            (player_id, joueur, nation, equipe, ligue, age, poste,
             matchs, titulaire, minutes, buts, passes_dec, xg, xag, saison)
        VALUES
            (:player_id, :joueur, :nation, :equipe, :ligue, :age, :poste,
             :matchs, :titulaire, :minutes, :buts, :passes_dec, :xg, :xag, :saison)
    """, rows)
    conn.commit()
    conn.close()
    logger.success(f"{len(rows)} stats joueurs insérées")


def insert_stats_equipes(rows: list) -> None:
    #Insérer ou mettre à jour les statistiques des équipes
    if not rows:
        return
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executemany("""
        INSERT OR REPLACE INTO stats_equipes
            (equipe, ligue, matchs, buts_marques, buts_encaisses, xg, xga, possession, saison)
        VALUES
            (:equipe, :ligue, :matchs, :buts_marques, :buts_encaisses, :xg, :xga, :possession, :saison)
    """, rows)
    conn.commit()
    conn.close()
    logger.success(f"{len(rows)} stats équipes insérées")


def insert_image_joueur(player_id: str, joueur: str, chemin: str) -> None:
    #Enregistrer le chemin local de l'image d'un joueur
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO images_joueurs (player_id, joueur, chemin, telecharge)
        VALUES (?, ?, ?, 1)
    """, (player_id, joueur, chemin))
    conn.commit()
    conn.close()