package model;

import exception.AgeInvalideException;
import java.util.Objects;

/**
 * Classe abstraite représentant une personne.
 * Contient les informations communes aux étudiants et enseignants.
 */
public abstract class Personne {

    /** âge minimal autorisé */
    public static final int AGE_MIN = 0;
    /** âge maximal autorisé */
    public static final int AGE_MAX = 130;

    private final String id;     // identifiant unique
    private String nom;
    private String prenom;
    private int age;

    /**
     * Constructeur de la classe Personne.
     * @param id identifiant unique de la personne
     * @param nom nom de la personne
     * @param prenom prénom de la personne
     * @param age âge de la personne
     * @throws AgeInvalideException si l'âge est hors des bornes autorisées
     */
    protected Personne(String id, String nom, String prenom, int age) throws AgeInvalideException {
        if (id == null || id.isBlank()) throw new IllegalArgumentException("id vide");
        this.id = id;
        this.nom = Objects.requireNonNull(nom, "nom obligatoire");
        this.prenom = Objects.requireNonNull(prenom, "prenom obligatoire");
        setAge(age); // vérifie la validité avec AgeInvalideException
    }

    // Getters et Setters

    public String getId() { return id; }
    public String getNom() { return nom; }
    public void setNom(String nom) { this.nom = Objects.requireNonNull(nom, "nom obligatoire"); }

    public String getPrenom() { return prenom; }
    public void setPrenom(String prenom) { this.prenom = Objects.requireNonNull(prenom, "prenom obligatoire"); }

    public int getAge() { return age; }

    /**
     * Définit l'âge de la personne et vérifie sa validité.
     * @param age âge à définir
     * @throws AgeInvalideException si l'âge est inférieur à AGE_MIN ou supérieur à AGE_MAX
     */
    public void setAge(int age) throws AgeInvalideException {
        if (age < AGE_MIN || age > AGE_MAX) {
            throw new AgeInvalideException("Âge invalide : " + age);
        }
        this.age = age;
    }

    // Autres méthodes utiles

    @Override
    public String toString() {
        return "%s{id='%s', nom='%s', prenom='%s', age=%d}"
                .formatted(getClass().getSimpleName(), id, nom, prenom, age);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Personne other)) return false;
        return id.equals(other.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
