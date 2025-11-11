package exception;

/**
 * Exception personnalisee levee lorsqu'uune note est invalide.
 * Une note doit etre comprise entre 0 et 20.
 */
public class NoteInvalideException extends Exception {

    /**
     * Constructeur de l'exception avec un message explicatif.
     * @param message détail de l'erreur
     */
    public NoteInvalideException(String message) {
        super(message);
    }
}
