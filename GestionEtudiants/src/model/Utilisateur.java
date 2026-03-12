package model;
/**
 * Interface représentant un utilisateur du système.
 * Fournit les méthodes nécessaires pour récupérer le login
 * et vérifier le mot de passe d'un utilisateur.
 */
public interface Utilisateur {

    /**
     * Retourne le login de l'utilisateur.
     * @return le login sous forme de chaîne de caractères
     */
    String getLogin();

    /**
     * Vérifie si le mot de passe fourni correspond à celui de l'utilisateur.
     * @param motDePasseClair le mot de passe en clair à vérifier
     * @return true si le mot de passe est correct, false sinon
     */
    boolean verifierMotDePasse(String motDePasseClair);
}
