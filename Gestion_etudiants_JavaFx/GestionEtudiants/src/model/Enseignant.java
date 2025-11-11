package model;

import exception.AgeInvalideException;

/**
 * Classe représentant un enseignant.
 * Hérite de la classe Personne et implémente Utilisateur (authentification).
 */
public class Enseignant extends Personne implements Utilisateur {

    private String departement;
    private String specialite;

    /** Identifiants (login + hash du mot de passe). */
    private Credentials credentials;

    /**
     * Constructeur historique (compatibilité).
     *
     * @param id identifiant unique (hérité de Personne)
     * @param nom nom de l'enseignant
     * @param prenom prénom de l'enseignant
     * @param age âge de l'enseignant
     * @param departement département auquel il appartient
     * @param specialite spécialité principale
     * @throws AgeInvalideException si l'âge est invalide
     */
    public Enseignant(String id, String nom, String prenom, int age,
                      String departement, String specialite)
            throws AgeInvalideException {
        super(id, nom, prenom, age); // appel du constructeur de Personne
        this.departement = (departement == null || departement.isBlank()) ? "Inconnu" : departement;
        this.specialite = (specialite == null || specialite.isBlank()) ? "Généraliste" : specialite;
        this.credentials = null; // pas d'identifiants avec ce constructeur
    }

    /**
     * Nouveau constructeur avec identifiants (login + hash du mot de passe).
     *
     * @param id identifiant unique (hérité de Personne)
     * @param nom nom de l'enseignant
     * @param prenom prénom de l'enseignant
     * @param age âge de l'enseignant
     * @param departement département auquel il appartient
     * @param specialite spécialité principale
     * @param credentials identifiants (login + passwordHash)
     * @throws AgeInvalideException si l'âge est invalide
     */
    public Enseignant(String id, String nom, String prenom, int age,
                      String departement, String specialite,
                      Credentials credentials)
            throws AgeInvalideException {
        super(id, nom, prenom, age);
        this.departement = (departement == null || departement.isBlank()) ? "Inconnu" : departement;
        this.specialite = (specialite == null || specialite.isBlank()) ? "Généraliste" : specialite;
        this.credentials = credentials;
    }

    // Getters et Setters

    public String getDepartement() { return departement; }
    public void setDepartement(String departement) { this.departement = departement; }

    public String getSpecialite() { return specialite; }
    public void setSpecialite(String specialite) { this.specialite = specialite; }

    /** Accès/MAJ des identifiants. */
    public Credentials getCredentials() { return credentials; }
    public void setCredentials(Credentials credentials) { this.credentials = credentials; }

    // Implémentation Utilisateur

    @Override
    public String getLogin() {
        return credentials == null ? null : credentials.login();
    }

    @Override
    public boolean verifierMotDePasse(String motDePasseClair) {
        return credentials != null && Passwords.matches(motDePasseClair, credentials.passwordHash());
    }

    @Override
    public String toString() {
        return "Enseignant{nom='%s', prenom='%s', département='%s', spécialité='%s'}"
                .formatted(getNom(), getPrenom(), departement, specialite);
    }
}
