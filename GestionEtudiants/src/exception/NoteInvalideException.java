package exception;

/**
 * Exception personnalisée levée lorsqu'une note est invalide.
 * Une note doit être comprise entre 0 et 20.
 */
public class NoteInvalideException extends Exception {

    /**
     * Construit une nouvelle exception avec un message d’erreur spécifié.
     * @param message le message décrivant la cause de l’exception
     */
    public NoteInvalideException(String message) {
        super(message);
    }
}
