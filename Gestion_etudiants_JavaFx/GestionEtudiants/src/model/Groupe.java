package model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

/**
 * Classe représentant un groupe d'étudiants.
 * Chaque groupe peut suivre plusieurs cours.
 */
public class Groupe {

    private final String nom; // nom unique du groupe
    private final List<Etudiant> etudiants = new ArrayList<>();
    private final List<Cours> cours = new ArrayList<>();

    // ajout du type de groupe (CM, TD, TP)
    private TypeCours type = TypeCours.CM; // valeur par défaut

    /**
     * Constructeur de la classe Groupe.
     *
     * @param nom nom unique du groupe
     * @throws IllegalArgumentException si le nom est vide
     */
    public Groupe(String nom) {
        if (nom == null || nom.isBlank())
            throw new IllegalArgumentException("nom de groupe vide");
        this.nom = nom;
    }

    /**
     * Constructeur avec type de groupe.
     * @param nom nom du groupe
     * @param type type de cours (CM, TD, TP)
     */
    public Groupe(String nom, TypeCours type) {
        if (nom == null || nom.isBlank())
            throw new IllegalArgumentException("nom de groupe vide");
        this.nom = nom;
        this.type = (type == null) ? TypeCours.CM : type;
    }

    // Getters
    public String getNom() { return nom; }

    public TypeCours getType() { return type; }
    public void setType(TypeCours type) {
        if (type == null) throw new IllegalArgumentException("type nul");
        this.type = type;
    }

    /** Retourne une vue non modifiable de la liste des étudiants */
    public List<Etudiant> getEtudiants() {
        return Collections.unmodifiableList(etudiants);
    }

    /** Retourne une vue non modifiable de la liste des cours */
    public List<Cours> getCours() {
        return Collections.unmodifiableList(cours);
    }

    // Gestion des étudiants

    public boolean ajouterEtudiant(Etudiant e) {
        Objects.requireNonNull(e, "étudiant nul");
        if (etudiants.contains(e)) return false; // déjà présent
        return etudiants.add(e);
    }

    public boolean retirerEtudiant(Etudiant e) {
        return etudiants.remove(e);
    }

    // Gestion des cours

    public boolean associerCours(Cours c) {
        Objects.requireNonNull(c, "cours nul");
        if (cours.contains(c)) return false; // déjà présent
        return cours.add(c);
    }

    public boolean retirerCours(Cours c) {
        return cours.remove(c);
    }

    @Override
    public String toString() {
        return "Groupe{nom='%s', type='%s', etudiants=%d, cours=%d}"
                .formatted(nom, type, etudiants.size(), cours.size());
    }
}
