package exception;

/**
 * Exception personnalisée levée lorsqu'un âge invalide est fourni.
 * Utilisée dans la classe Personne pour vérifier la validité de l'âge.
 *
 * @author Alia TOURE
 * @version 1.0
 */
public class AgeInvalideException extends Exception {

    /**
     * Constructeur de l'exception avec un message explicatif.
     * @param message détail de l'erreur
     */
    public AgeInvalideException(String message) {
        super(message);
    }
}
