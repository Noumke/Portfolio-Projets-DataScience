package model;

import java.util.Objects;

public class Credentials {
    private final String login;
    private final String passwordHash;

    public Credentials(String login, String passwordHash) {
        this.login = Objects.requireNonNull(login, "login nul");
        this.passwordHash = Objects.requireNonNull(passwordHash, "hash nul");
    }

    public String login() { return login; }
    public String passwordHash() { return passwordHash; }
}
