package model;

import java.util.HashSet;
import java.util.Set;

/**
 * Classe qui représente un cours.
 * Un cours possède un code, un nom, un coefficient et un enseignant référent.
 * Il peut aussi avoir un type (CM, TD, TP) et une liste d’enseignants autorisés.
 */
public class Cours {

    /** Code du cours. */
    private final String code;

    /** Nom du cours. */
    private String libelle;

    /** Coefficient du cours, doit être supérieur à 0. */
    private double coefficient;

    /** Enseignant responsable du cours. */
    private Enseignant referent;

    /** Type du cours, par défaut CM. */
    private TypeCours type = TypeCours.CM;

    /** Liste des enseignants autorisés à faire ce cours. */
    private final Set<Enseignant> autorises = new HashSet<>();

    /**
     * Constructeur du cours.
     *
     * @param code code du cours
     * @param libelle nom du cours
     * @param coefficient coefficient du cours, doit être supérieur à 0
     * @param referent enseignant référent du cours
     * @throws IllegalArgumentException si un paramètre est invalide
     */
    public Cours(String code, String libelle, double coefficient, Enseignant referent) {
        if (code == null || code.isBlank())
            throw new IllegalArgumentException("code de cours vide");
        if (coefficient <= 0)
            throw new IllegalArgumentException("le coefficient doit être > 0");
        if (referent == null)
            throw new IllegalArgumentException("enseignant référent manquant");

        this.code = code;
        this.libelle = libelle;
        this.coefficient = coefficient;
        this.referent = referent;

        // Le référent est autorisé par défaut
        this.autorises.add(referent);
    }

    /**
     * Retourne le type du cours.
     *
     * @return le type
     */
    public TypeCours getType() {
        return type;
    }

    /**
     * Change le type du cours.
     *
     * @param type nouveau type
     */
    public void setType(TypeCours type) {
        if (type == null)
            throw new IllegalArgumentException("type nul");
        this.type = type;
    }

    /**
     * Autorise un enseignant à donner le cours.
     *
     * @param e enseignant à autoriser
     * @return true si ajouté, false sinon
     */
    public boolean autoriser(Enseignant e) {
        if (e == null) return false;
        return autorises.add(e);
    }

    /**
     * Retire un enseignant autorisé, sauf le référent.
     *
     * @param e enseignant à retirer
     * @return true si retiré, false sinon
     */
    public boolean retirerAutorisation(Enseignant e) {
        if (e == null) return false;
        if (referent != null && referent.equals(e)) return false;
        return autorises.remove(e);
    }

    /**
     * Vérifie si un enseignant est autorisé.
     *
     * @param e enseignant à vérifier
     * @return true si autorisé, false sinon
     */
    public boolean estAutorise(Enseignant e) {
        return e != null && autorises.contains(e);
    }

    /**
     * Retourne le code du cours.
     *
     * @return le code
     */
    public String getCode() {
        return code;
    }

    /**
     * Retourne le nom du cours.
     *
     * @return le nom
     */
    public String getLibelle() {
        return libelle;
    }

    /**
     * Change le nom du cours.
     *
     * @param libelle nouveau nom
     */
    public void setLibelle(String libelle) {
        this.libelle = libelle;
    }

    /**
     * Retourne le coefficient du cours.
     *
     * @return le coefficient
     */
    public double getCoefficient() {
        return coefficient;
    }

    /**
     * Change le coefficient du cours.
     *
     * @param coefficient nouveau coefficient
     */
    public void setCoefficient(double coefficient) {
        if (coefficient <= 0)
            throw new IllegalArgumentException("le coefficient doit être > 0");
        this.coefficient = coefficient;
    }

    /**
     * Retourne l’enseignant référent du cours.
     *
     * @return le référent
     */
    public Enseignant getReferent() {
        return referent;
    }

    /**
     * Change l’enseignant référent du cours.
     * Il devient automatiquement autorisé.
     *
     * @param referent nouveau référent
     */
    public void setReferent(Enseignant referent) {
        if (referent == null)
            throw new IllegalArgumentException("enseignant référent manquant");
        this.referent = referent;
        this.autorises.add(referent);
    }

    /**
     * Retourne une phrase avec les infos principales du cours.
     *
     * @return description du cours
     */
    @Override
    public String toString() {
        return "Cours{code='%s', libelle='%s', coefficient=%.1f, referent='%s %s'}"
                .formatted(code, libelle, coefficient,
                        referent.getPrenom(), referent.getNom());
    }
}
