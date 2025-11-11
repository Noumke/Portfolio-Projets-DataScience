package model;

import exception.AgeInvalideException;

/**
 * Classe représentant un étudiant.
 * Hérite de la classe Personne.
 */
public class Etudiant extends Personne {

    private final String matricule; // identifiant unique étudiant
    private String filiere;
    private String semestre;

    /**
     * Constructeur de la classe Etudiant.
     *
     * @param id identifiant unique (hérité de Personne)
     * @param nom nom de l'étudiant
     * @param prenom prénom de l'étudiant
     * @param age âge de l'étudiant
     * @param matricule code unique de l'étudiant
     * @param filiere filière suivie (ex : Data Science)
     * @param semestre semestre actuel (ex : S3)
     * @throws AgeInvalideException si l'âge est invalide
     */
    public Etudiant(String id, String nom, String prenom, int age,
                    String matricule, String filiere, String semestre)
            throws AgeInvalideException {
        super(id, nom, prenom, age); // appelle le constructeur de Personne
        if (matricule == null || matricule.isBlank())
            throw new IllegalArgumentException("matricule vide");
        this.matricule = matricule;
        this.filiere = filiere;
        this.semestre = semestre;
    }

    // Getters / Setters
    public String getMatricule() { return matricule; }
    public String getFiliere() { return filiere; }
    public void setFiliere(String filiere) { this.filiere = filiere; }

    public String getSemestre() { return semestre; }
    public void setSemestre(String semestre) { this.semestre = semestre; }

    @Override
    public String toString() {
        return "Etudiant{matricule='%s', nom='%s', prenom='%s', filiere='%s', semestre='%s'}"
                .formatted(matricule, getNom(), getPrenom(), filiere, semestre);
    }
}
