package model;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

/**
 * Classe utilitaire pour la gestion des mots de passe.
 * Fournit des méthodes pour le hachage et la vérification
 * des mots de passe à l’aide de l’algorithme SHA-256.
 */
public final class Passwords {

    /**
     * Constructeur privé pour empêcher l’instanciation de la classe utilitaire.
     */
    private Passwords() {}

    /**
     * Génère le hachage SHA-256 d’une chaîne donnée.
     * @param clear le mot de passe en clair
     * @return le hachage du mot de passe sous forme hexadécimale
     * @throws IllegalStateException si l’algorithme SHA-256 n’est pas supporté
     */
    public static String sha256(String clear) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] digest = md.digest(clear.getBytes(StandardCharsets.UTF_8));
            StringBuilder sb = new StringBuilder(digest.length * 2);
            for (byte b : digest) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch (NoSuchAlgorithmException e) {
            throw new IllegalStateException("SHA-256 non supporté", e);
        }
    }

    /**
     * Vérifie si le mot de passe fourni correspond au hachage attendu.
     * @param clear le mot de passe en clair à vérifier
     * @param expectedHash le hachage attendu
     * @return true si le mot de passe correspond, false sinon
     */
    public static boolean matches(String clear, String expectedHash) {
        return sha256(clear).equals(expectedHash);
    }
}
