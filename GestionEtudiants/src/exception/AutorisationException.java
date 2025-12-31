package exception;

/**
 * Exception levée lorsqu'un utilisateur (les profs) tente d'accéder
 * à une ressource  ou d'effectuer une action sans autorisation.
 */
public class AutorisationException extends Exception {

    /**
     * Construit une nouvelle exception avec un message d’erreur spécifié.
     * @param message le message décrivant la cause de l’exception
     */
    public AutorisationException(String message) {
        super(message);
    }
}
