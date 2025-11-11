package model;

import exception.NoteInvalideException;
import java.util.Objects;

/**
 * Classe représentant une note attribuée à un étudiant pour un cours.
 */
public class Note {

    private final Etudiant etudiant; // étudiant concerné
    private final Cours cours;       // cours concerné
    private double valeur;           // note sur 20

    /**
     * Constructeur de la classe Note.
     *
     * @param etudiant étudiant concerné
     * @param cours cours concerné
     * @param valeur note attribuée (entre 0 et 20)
     * @throws NoteInvalideException si la note est hors de l'intervalle [0, 20]
     */
    public Note(Etudiant etudiant, Cours cours, double valeur) throws NoteInvalideException {
        this.etudiant = Objects.requireNonNull(etudiant, "étudiant nul");
        this.cours = Objects.requireNonNull(cours, "cours nul");
        setValeur(valeur); // vérifie la validité
    }

    //  Getters ET Setters

    public Etudiant getEtudiant() { return etudiant; }
    public Cours getCours() { return cours; }

    public double getValeur() { return valeur; }

    /**
     * Définit la valeur de la note et vérifie qu'elle est comprise entre 0 et 20.
     * @param valeur la note à attribuer
     * @throws NoteInvalideException si la valeur est invalide
     */
    public void setValeur(double valeur) throws NoteInvalideException {
        if (valeur < 0 || valeur > 20)
            throw new NoteInvalideException("Note invalide : " + valeur + " (doit être entre 0 et 20)");
        this.valeur = valeur;
    }

    @Override
    public String toString() {
        return "Note{étudiant='%s %s', cours='%s', valeur=%.2f}"
                .formatted(etudiant.getPrenom(), etudiant.getNom(),
                        cours.getLibelle(), valeur);
    }
}
