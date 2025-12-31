package exception;

/**
 * Exception levée lorsqu'une erreur d'authentification se produit.
 * Par exemple, lorsque le login ou le mot de passe est incorrect.
 */
public class AuthentificationException extends Exception {

    /**
     * Construit une nouvelle exception avec un message d’erreur spécifié.
     * @param message le message décrivant la cause de l’exception
     */
    public AuthentificationException(String message) {
        super(message);
    }
}
