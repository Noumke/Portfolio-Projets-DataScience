package model;

import java.util.Objects;

/**
 * Classe représentant les identifiants d’un utilisateur.
 * Elle contient le login et le hachage du mot de passe associé.
 */
public class Credentials {

    private final String login;
    private final String passwordHash;

    /**
     * Construit un objet Credentials avec un login et un mot de passe haché.
     * @param login le nom d’utilisateur, non nul
     * @param passwordHash le hachage du mot de passe, non nul
     * @throws NullPointerException si l’un des paramètres est nul
     */
    public Credentials(String login, String passwordHash) {
        this.login = Objects.requireNonNull(login, "login nul");
        this.passwordHash = Objects.requireNonNull(passwordHash, "hash nul");
    }

    /**
     * Retourne le login de l’utilisateur.
     * @return le login sous forme de chaîne de caractères
     */
    public String login() { return login; }

    /**
     * Retourne le hachage du mot de passe de l’utilisateur.
     * @return le hachage du mot de passe
     */
    public String passwordHash() { return passwordHash; }
}
