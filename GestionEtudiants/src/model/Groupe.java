package model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;

/**
 * Classe qui représente un groupe d'étudiants.
 * Un groupe a un nom, un type (CM, TD, TP), une liste d'étudiants et une liste de cours.
 */
public class Groupe {

    /** Nom du groupe. */
    private final String nom;

    /** Liste des étudiants du groupe. */
    private final List<Etudiant> etudiants = new ArrayList<>();

    /** Liste des cours associés au groupe. */
    private final List<Cours> cours = new ArrayList<>();

    /** Type du groupe, par défaut CM. */
    private TypeCours type = TypeCours.CM;

    /**
     * Constructeur du groupe.
     *
     * @param nom nom du groupe
     * @throws IllegalArgumentException si le nom est vide
     */
    public Groupe(String nom) {
        if (nom == null || nom.isBlank())
            throw new IllegalArgumentException("nom de groupe vide");
        this.nom = nom;
    }

    /**
     * Constructeur du groupe avec type.
     *
     * @param nom nom du groupe
     * @param type type du groupe (CM, TD ou TP)
     */
    public Groupe(String nom, TypeCours type) {
        if (nom == null || nom.isBlank())
            throw new IllegalArgumentException("nom de groupe vide");
        this.nom = nom;
        this.type = (type == null) ? TypeCours.CM : type;
    }

    /**
     * Retourne le nom du groupe.
     *
     * @return le nom du groupe
     */
    public String getNom() {
        return nom;
    }

    /**
     * Retourne le type du groupe.
     *
     * @return le type du groupe
     */
    public TypeCours getType() {
        return type;
    }

    /**
     * Change le type du groupe.
     *
     * @param type nouveau type
     */
    public void setType(TypeCours type) {
        if (type == null)
            throw new IllegalArgumentException("type nul");
        this.type = type;
    }

    /**
     * Retourne la liste des étudiants du groupe.
     * La liste ne peut pas être modifiée directement.
     *
     * @return liste des étudiants
     */
    public List<Etudiant> getEtudiants() {
        return Collections.unmodifiableList(etudiants);
    }

    /**
     * Retourne la liste des cours du groupe.
     * La liste ne peut pas être modifiée directement.
     *
     * @return liste des cours
     */
    public List<Cours> getCours() {
        return Collections.unmodifiableList(cours);
    }

    /**
     * Ajoute un étudiant dans le groupe.
     *
     * @param e étudiant à ajouter
     * @return true si ajouté, false sinon
     */
    public boolean ajouterEtudiant(Etudiant e) {
        Objects.requireNonNull(e, "étudiant nul");
        if (etudiants.contains(e)) return false;
        return etudiants.add(e);
    }

    /**
     * Retire un étudiant du groupe.
     *
     * @param e étudiant à retirer
     * @return true si retiré, false sinon
     */
    public boolean retirerEtudiant(Etudiant e) {
        return etudiants.remove(e);
    }

    /**
     * Ajoute un cours au groupe.
     *
     * @param c cours à associer
     * @return true si ajouté, false sinon
     */
    public boolean associerCours(Cours c) {
        Objects.requireNonNull(c, "cours nul");
        if (cours.contains(c)) return false;
        return cours.add(c);
    }

    /**
     * Retire un cours du groupe.
     *
     * @param c cours à retirer
     * @return true si retiré, false sinon
     */
    public boolean retirerCours(Cours c) {
        return cours.remove(c);
    }

    /**
     * Retourne une description du groupe.
     *
     * @return texte avec le nom, le type et le nombre d'étudiants et de cours
     */
    @Override
    public String toString() {
        return "Groupe{nom='%s', type='%s', etudiants=%d, cours=%d}"
                .formatted(nom, type, etudiants.size(), cours.size());
    }
}
