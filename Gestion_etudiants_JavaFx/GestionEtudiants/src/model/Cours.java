package model;

import java.util.HashSet;
import java.util.Set;

/**
 * Classe représentant un cours.
 * Chaque cours possède un code unique, un libellé, un coefficient et un enseignant référent.
 */
public class Cours {

    private final String code;        // code unique du cours
    private String libelle;           // nom du cours
    private double coefficient;       // doit être > 0
    private Enseignant referent;      // enseignant responsable du cours

    // N1 : type de cours + liste des enseignants autorisés
    private TypeCours type = TypeCours.CM;      // valeur par défaut
    private final Set<Enseignant> autorises = new HashSet<>();

    /**
     * Constructeur de la classe Cours.
     *
     * @param code code unique du cours
     * @param libelle nom du cours
     * @param coefficient valeur du coefficient (doit être > 0)
     * @param referent enseignant responsable
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

    // Gestion du type et des autorisations

    public TypeCours getType() { return type; }

    public void setType(TypeCours type) {
        if (type == null) throw new IllegalArgumentException("type nul");
        this.type = type;
    }

    public boolean autoriser(Enseignant e) {
        if (e == null) return false;
        return autorises.add(e);
    }

    public boolean retirerAutorisation(Enseignant e) {
        if (e == null) return false;
        if (referent != null && referent.equals(e)) return false; // le référent reste autorisé
        return autorises.remove(e);
    }

    public boolean estAutorise(Enseignant e) {
        return e != null && autorises.contains(e);
    }

    // Getters / Setters de base

    public String getCode() { return code; }

    public String getLibelle() { return libelle; }
    public void setLibelle(String libelle) { this.libelle = libelle; }

    public double getCoefficient() { return coefficient; }
    public void setCoefficient(double coefficient) {
        if (coefficient <= 0)
            throw new IllegalArgumentException("le coefficient doit être > 0");
        this.coefficient = coefficient;
    }

    public Enseignant getReferent() { return referent; }
    public void setReferent(Enseignant referent) {
        if (referent == null)
            throw new IllegalArgumentException("enseignant référent manquant");
        this.referent = referent;
        // garantir que le nouveau référent est autorisé
        this.autorises.add(referent);
    }

    @Override
    public String toString() {
        return "Cours{code='%s', libelle='%s', coefficient=%.1f, referent='%s %s'}"
                .formatted(code, libelle, coefficient,
                        referent.getPrenom(), referent.getNom());
    }
}
