package exception;

/**
 * Exception levée quand l'âge fourni est invalide.
 * Exemple de cas : âge négatif, trop grand, ou incohérent avec les règles du projet.
 */
public class AgeInvalideException extends Exception {

    public AgeInvalideException(String message) {
        super(message);
    }

    public AgeInvalideException(String message, Throwable cause) {
        super(message, cause);
    }
}
