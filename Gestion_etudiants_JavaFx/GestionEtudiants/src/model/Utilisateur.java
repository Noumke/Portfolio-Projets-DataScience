package model;

public interface Utilisateur {
    String getLogin();
    boolean verifierMotDePasse(String motDePasseClair);
}
