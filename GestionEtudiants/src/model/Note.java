package model;

import exception.NoteInvalideException;
import java.util.Objects;

/**
 * Classe qui représente une note donnée à un étudiant pour un cours.
 * Une note est toujours comprise entre 0 et 20.
 */
public class Note {

    /** Étudiant qui reçoit la note. */
    private final Etudiant etudiant;

    /** Cours concerné par la note. */
    private final Cours cours;

    /** Valeur de la note sur 20. */
    private double valeur;

    /**
     * Constructeur de la classe Note.
     *
     * @param etudiant étudiant concerné
     * @param cours cours concerné
     * @param valeur note entre 0 et 20
     * @throws NoteInvalideException si la note n’est pas entre 0 et 20
     */
    public Note(Etudiant etudiant, Cours cours, double valeur) throws NoteInvalideException {
        this.etudiant = Objects.requireNonNull(etudiant, "étudiant nul");
        this.cours = Objects.requireNonNull(cours, "cours nul");
        setValeur(valeur);
    }

    /**
     * Retourne l’étudiant concerné.
     *
     * @return l’étudiant
     */
    public Etudiant getEtudiant() {
        return etudiant;
    }

    /**
     * Retourne le cours concerné.
     *
     * @return le cours
     */
    public Cours getCours() {
        return cours;
    }

    /**
     * Retourne la valeur de la note.
     *
     * @return la valeur sur 20
     */
    public double getValeur() {
        return valeur;
    }

    /**
     * Modifie la valeur de la note.
     * La valeur doit être comprise entre 0 et 20.
     *
     * @param valeur nouvelle valeur
     * @throws NoteInvalideException si la valeur est hors de l’intervalle
     */
    public void setValeur(double valeur) throws NoteInvalideException {
        if (valeur < 0 || valeur > 20)
            throw new NoteInvalideException("Note invalide : " + valeur + " (doit être entre 0 et 20)");
        this.valeur = valeur;
    }

    /**
     * Retourne une phrase avec le nom de l’étudiant, le cours et la note.
     *
     * @return description de la note
     */
    @Override
    public String toString() {
        return "Note{étudiant='%s %s', cours='%s', valeur=%.2f}"
                .formatted(etudiant.getPrenom(), etudiant.getNom(),
                        cours.getLibelle(), valeur);
    }
}
