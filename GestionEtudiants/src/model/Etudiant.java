package model;
import exception.AgeInvalideException;
/**
 * Classe qui représente un étudiant.
 * Un étudiant est une personne avec un matricule, une filière et un semestre.
 */
public class Etudiant extends Personne {

    /** Matricule de l'étudiant. */
    private final String matricule;

    /** Filière de l'étudiant. */
    private String filiere;

    /** Semestre actuel de l'étudiant. */
    private String semestre;

    /**
     * Constructeur de la classe Etudiant.
     *
     * @param id identifiant unique de la personne
     * @param nom nom de l'étudiant
     * @param prenom prénom de l'étudiant
     * @param age âge de l'étudiant
     * @param matricule code unique de l'étudiant
     * @param filiere filière suivie (exemple : Data Science)
     * @param semestre semestre actuel (exemple : S3)
     * @throws AgeInvalideException si l'âge est invalide
     * @throws IllegalArgumentException si le matricule est vide ou nul
     */
    public Etudiant(String id, String nom, String prenom, int age,
                    String matricule, String filiere, String semestre)
            throws AgeInvalideException {
        super(id, nom, prenom, age);
        if (matricule == null || matricule.isBlank())
            throw new IllegalArgumentException("matricule vide");
        this.matricule = matricule;
        this.filiere = filiere;
        this.semestre = semestre;
    }

    /**
     * Retourne le matricule de l'étudiant.
     *
     * @return le matricule
     */
    public String getMatricule() {
        return matricule;
    }

    /**
     * Retourne la filière de l'étudiant.
     *
     * @return la filière
     */
    public String getFiliere() {
        return filiere;
    }

    /**
     * Change la filière de l'étudiant.
     *
     * @param filiere nouvelle filière
     */
    public void setFiliere(String filiere) {
        this.filiere = filiere;
    }

    /**
     * Retourne le semestre de l'étudiant.
     *
     * @return le semestre
     */
    public String getSemestre() {
        return semestre;
    }

    /**
     * Change le semestre de l'étudiant.
     *
     * @param semestre nouveau semestre
     */
    public void setSemestre(String semestre) {
        this.semestre = semestre;
    }

    /**
     * Retourne une description de l'étudiant.
     *
     * @return texte avec le matricule, nom, prénom, filière et semestre
     */
    @Override
    public String toString() {
        return "Etudiant{matricule='%s', nom='%s', prenom='%s', filiere='%s', semestre='%s'}"
                .formatted(matricule, getNom(), getPrenom(), filiere, semestre);
    }
}
