package service;

import exception.NoteInvalideException;
import exception.AuthentificationException;
import exception.AutorisationException;
import model.*;

import java.util.*;
import java.util.stream.Collectors;

/**
 * Classe centrale permettant de gérer les étudiants, enseignants, cours, groupes et notes.
 */
public class Gestionnaire {

    // Collections pour stocker les données
    private final Map<String, Etudiant> etudiants = new HashMap<>();
    private final Map<String, Enseignant> enseignants = new HashMap<>();
    private final Map<String, Cours> cours = new HashMap<>();
    private final Map<String, Groupe> groupes = new HashMap<>();
    private final Map<Etudiant, List<Note>> notes = new HashMap<>();

    // annuaire login -> Enseignant pour l'authentification
    private final Map<String, Enseignant> logins = new HashMap<>();

    // Étudiants
    public void ajouterEtudiant(Etudiant e) {
        Objects.requireNonNull(e, "étudiant nul");
        if (etudiants.containsKey(e.getMatricule()))
            throw new IllegalArgumentException("Matricule déjà existant : " + e.getMatricule());
        etudiants.put(e.getMatricule(), e);
    }

    public Etudiant getEtudiant(String matricule) {
        Etudiant e = etudiants.get(matricule);
        if (e == null)
            throw new NoSuchElementException("Étudiant introuvable : " + matricule);
        return e;
    }

    /** Liste en lecture seule de tous les étudiants (pour l'UI). */
    public Collection<Etudiant> getTousEtudiants() {
        return Collections.unmodifiableCollection(etudiants.values());
    }

    //  Enseignants

    // on alimente aussi la map des logins si credentials présents
    public void ajouterEnseignant(Enseignant ens) {
        Objects.requireNonNull(ens, "enseignant nul");
        if (enseignants.containsKey(ens.getId()))
            throw new IllegalArgumentException("Enseignant déjà existant : " + ens.getId());

        String login = ens.getLogin();
        if (login != null) {
            if (logins.containsKey(login))
                throw new IllegalArgumentException("Login déjà utilisé : " + login);
            // on réserve le login tout de suite pour éviter les races
            logins.put(login, ens);
        }
        enseignants.put(ens.getId(), ens);
    }

    public Enseignant getEnseignant(String id) {
        Enseignant e = enseignants.get(id);
        if (e == null)
            throw new NoSuchElementException("Enseignant introuvable : " + id);
        return e;
    }

    /** Liste en lecture seule de tous les enseignants (pour l'UI). */
    public Collection<Enseignant> getTousEnseignants() {
        return Collections.unmodifiableCollection(enseignants.values());
    }

    //  Cours

    public void ajouterCours(Cours c) {
        Objects.requireNonNull(c, "cours nul");
        if (cours.containsKey(c.getCode()))
            throw new IllegalArgumentException("Cours déjà existant : " + c.getCode());
        cours.put(c.getCode(), c);
    }

    public Cours getCours(String code) {
        Cours c = cours.get(code);
        if (c == null)
            throw new NoSuchElementException("Cours introuvable : " + code);
        return c;
    }

    /** Liste en lecture seule de tous les cours (pour l'UI). */
    public Collection<Cours> getTousCours() {
        return Collections.unmodifiableCollection(cours.values());
    }

    // Groupes

    public void ajouterGroupe(Groupe g) {
        Objects.requireNonNull(g, "groupe nul");
        if (groupes.containsKey(g.getNom()))
            throw new IllegalArgumentException("Groupe déjà existant : " + g.getNom());
        groupes.put(g.getNom(), g);
    }

    public Groupe getGroupe(String nom) {
        Groupe g = groupes.get(nom);
        if (g == null)
            throw new NoSuchElementException("Groupe introuvable : " + nom);
        return g;
    }

    public boolean supprimerGroupe(String nom) {
        // Supprime le groupe de la map; renvoie true si existait
        return groupes.remove(Objects.requireNonNull(nom, "nom nul")) != null;
    }

    public void ajouterEtudiantAuGroupe(String matricule, String nomGroupe) {
        Etudiant e = getEtudiant(matricule);
        Groupe g = getGroupe(nomGroupe);
        g.ajouterEtudiant(e);
    }

    public void associerCoursAuGroupe(String codeCours, String nomGroupe) {
        Cours c = getCours(codeCours);
        Groupe g = getGroupe(nomGroupe);
        g.associerCours(c);
    }

    // Notes (mode libre)

    public void saisirNote(String matricule, String codeCours, double valeur) throws NoteInvalideException {
        Etudiant e = getEtudiant(matricule);
        Cours c = getCours(codeCours);
        Note n = new Note(e, c, valeur);
        notes.computeIfAbsent(e, k -> new ArrayList<>()).add(n);
    }

    public List<Note> getNotesEtudiant(String matricule) {
        Etudiant e = getEtudiant(matricule);
        return Collections.unmodifiableList(notes.getOrDefault(e, List.of()));
    }

    public double moyenneSimple(String matricule) {
        List<Note> liste = getNotesEtudiant(matricule);
        if (liste.isEmpty()) return Double.NaN;
        return liste.stream().mapToDouble(Note::getValeur).average().orElse(Double.NaN);
    }

    public double moyennePonderee(String matricule) {
        List<Note> liste = getNotesEtudiant(matricule);
        double num = 0, den = 0;
        for (Note n : liste) {
            num += n.getValeur() * n.getCours().getCoefficient();
            den += n.getCours().getCoefficient();
        }
        return den == 0 ? Double.NaN : num / den;
    }

    public String bulletin(String matricule) {
        Etudiant e = getEtudiant(matricule);
        List<Note> liste = getNotesEtudiant(matricule);
        String notesStr = liste.stream()
                .map(n -> "%s=%.1f".formatted(n.getCours().getLibelle(), n.getValeur()))
                .collect(Collectors.joining(", "));
        return "Bulletin de %s %s (%s): %s | Moyenne: %.2f"
                .formatted(e.getPrenom(), e.getNom(), e.getMatricule(), notesStr, moyennePonderee(matricule));
    }

    //  Authentification et Autorisations

    /** Authentifie un enseignant via login + mot de passe clair. */
    public Enseignant authentifier(String login, String motDePasse) throws AuthentificationException {
        Enseignant e = logins.get(login);
        if (e == null || !e.verifierMotDePasse(motDePasse)) {
            throw new AuthentificationException("Identifiants invalides");
        }
        return e;
    }

    /** Autorise un enseignant (par id) à intervenir sur un cours (par code). */
    public void attribuerCoursAEnseignant(String codeCours, String idEnseignant) {
        Cours c = getCours(codeCours);
        Enseignant e = getEnseignant(idEnseignant);
        c.autoriser(e);
    }

    /** Saisie d'une note par un enseignant authentifié et autorisé sur le cours. */
    public void saisirNoteParEnseignant(String login, String mdp,
                                        String matricule, String codeCours, double valeur)
            throws AuthentificationException, AutorisationException, NoteInvalideException {
        Enseignant prof = authentifier(login, mdp);
        Cours c = getCours(codeCours);
        if (!c.estAutorise(prof)) {
            throw new AutorisationException("Accès refusé au cours " + codeCours);
        }
        saisirNote(matricule, codeCours, valeur);
    }

    /** Saisie d'une même note pour tout un groupe, par un enseignant authentifié et autorisé. */
    public void saisirNoteGroupeParEnseignant(String login, String mdp,
                                              String nomGroupe, String codeCours, double valeur)
            throws AuthentificationException, AutorisationException, NoteInvalideException {
        Enseignant prof = authentifier(login, mdp);
        Cours c = getCours(codeCours);
        if (!c.estAutorise(prof)) {
            throw new AutorisationException("Accès refusé au cours " + codeCours);
        }
        Groupe g = getGroupe(nomGroupe);
        for (Etudiant etu : g.getEtudiants()) {
            saisirNote(etu.getMatricule(), codeCours, valeur);
        }
    }

    //  SUPPRESSIONS avec intégrité

    /**
     * Supprime un enseignant s'il n'est ni référent d'un cours ni autorisé sur un cours.
     * Retire également son login de l'annuaire.
     */
    public boolean supprimerEnseignant(String id) {
        Objects.requireNonNull(id, "id nul");
        Enseignant e = enseignants.get(id);
        if (e == null) return false;

        // Vérification des liens aux cours
        for (Cours c : cours.values()) {
            if (c.getReferent().equals(e) || c.estAutorise(e)) {
                throw new IllegalStateException(
                        "Impossible de supprimer : l'enseignant est lié au cours " + c.getCode()
                );
            }
        }
        // Nettoyage annuaire des logins
        String login = e.getLogin();
        if (login != null) {
            Enseignant current = logins.get(login);
            if (current != null && current.equals(e)) {
                logins.remove(login);
            }
        }
        return enseignants.remove(id) != null;
    }

    /**
     * Supprime un cours : le retire de tous les groupes et supprime toutes les notes liées.
     */
    public boolean supprimerCours(String code) {
        Objects.requireNonNull(code, "code nul");
        Cours c = cours.remove(code);
        if (c == null) return false;

        // Retirer des groupes
        for (Groupe g : groupes.values()) {
            g.retirerCours(c);
        }
        // Retirer les notes liées à ce cours
        for (var entry : notes.entrySet()) {
            entry.getValue().removeIf(n -> n.getCours().equals(c));
        }
        return true;
    }

    /**
     * Supprime un étudiant : le retire de tous les groupes et supprime toutes ses notes.
     */
    public boolean supprimerEtudiant(String matricule) {
        Objects.requireNonNull(matricule, "matricule nul");
        Etudiant e = etudiants.remove(matricule);
        if (e == null) return false;

        // Retirer des groupes
        for (Groupe g : groupes.values()) {
            g.retirerEtudiant(e);
        }
        // Supprimer ses notes
        notes.remove(e);
        return true;
    }
}
