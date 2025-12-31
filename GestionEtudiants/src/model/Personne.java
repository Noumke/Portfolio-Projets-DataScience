package model;
import java.util.Objects;
import exception.AgeInvalideException;
/**
 * Classe abstraite qui représente une personne.
 * Elle contient les informations communes aux étudiants et aux enseignants.
 */
public abstract class Personne {

    /** Âge minimal autorisé. */
    public static final int AGE_MIN = 3;

    /** Âge maximal autorisé. */
    public static final int AGE_MAX = 90;

    /** Identifiant unique de la personne. */
    private final String id;

    /** Nom de la personne. */
    private String nom;

    /** Prénom de la personne. */
    private String prenom;

    /** Âge de la personne. */
    private int age;

    /**
     * Constructeur de la classe Personne.
     *
     * @param id identifiant unique
     * @param nom nom de la personne
     * @param prenom prénom de la personne
     * @param age âge de la personne
     * @throws AgeInvalideException si l'âge n'est pas valide
     */
    protected Personne(String id, String nom, String prenom, int age) throws AgeInvalideException {
        if (id == null || id.isBlank())
            throw new IllegalArgumentException("id vide");
        this.id = id;
        this.nom = Objects.requireNonNull(nom, "nom obligatoire");
        this.prenom = Objects.requireNonNull(prenom, "prenom obligatoire");
        setAge(age);
    }

    /**
     * Retourne l'identifiant de la personne.
     *
     * @return l'identifiant
     */
    public String getId() {
        return id;
    }

    /**
     * Retourne le nom de la personne.
     *
     * @return le nom
     */
    public String getNom() {
        return nom;
    }

    /**
     * Change le nom de la personne.
     *
     * @param nom nouveau nom
     */
    public void setNom(String nom) {
        this.nom = Objects.requireNonNull(nom, "nom obligatoire");
    }

    /**
     * Retourne le prénom de la personne.
     *
     * @return le prénom
     */
    public String getPrenom() {
        return prenom;
    }

    /**
     * Change le prénom de la personne.
     *
     * @param prenom nouveau prénom
     */
    public void setPrenom(String prenom) {
        this.prenom = Objects.requireNonNull(prenom, "prenom obligatoire");
    }

    /**
     * Retourne l'âge de la personne.
     *
     * @return l'âge
     */
    public int getAge() {
        return age;
    }

    /**
     * Modifie l'âge de la personne.
     * L'âge doit être compris entre AGE_MIN et AGE_MAX.
     *
     * @param age nouvel âge
     * @throws AgeInvalideException si l'âge n'est pas valide
     */
    public void setAge(int age) throws AgeInvalideException {
        if (age < AGE_MIN || age > AGE_MAX)
            throw new AgeInvalideException("Âge invalide : " + age);
        this.age = age;
    }

    /**
     * Retourne une phrase avec les informations principales de la personne.
     *
     * @return texte contenant le type, l'id, le nom, le prénom et l'âge
     */
    @Override
    public String toString() {
        return "%s{id='%s', nom='%s', prenom='%s', age=%d}"
                .formatted(getClass().getSimpleName(), id, nom, prenom, age);
    }

    /**
     * Vérifie si deux personnes ont le même identifiant.
     *
     * @param obj autre objet à comparer
     * @return true si les identifiants sont identiques
     */
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Personne other)) return false;
        return id.equals(other.id);
    }

    /**
     * Retourne le code de hachage basé sur l'identifiant.
     *
     * @return le code de hachage
     */
    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
