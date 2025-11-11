package app;

import exception.AgeInvalideException;
import exception.NoteInvalideException;
import exception.AuthentificationException;
import exception.AutorisationException;
import model.*;
import service.Gestionnaire;

/**
 * Point d'entrée du programme Gestion d'Étudiants.
 * Permet de tester les fonctionnalités principales.
 */
public class AppMain {

    public static void main(String[] args) {
        try {
            Gestionnaire g = new Gestionnaire();

            // Création des enseignants
            // prof1 sans identifiants (constructeur historique)
            Enseignant prof1 = new Enseignant("ENS-1", "Vidal", "Morgane", 31, "Science des données", "Java");
            g.ajouterEnseignant(prof1);

            // prof2 avec identifiants (login + mot de passe hashé)
            Credentials cred = new Credentials("prof-vidal", Passwords.sha256("secret"));
            Enseignant prof2 = new Enseignant("ENS-2", "Bergeron", "Jean yves", 42, "Sciences des données", "Economie", cred);
            g.ajouterEnseignant(prof2);

            //  Création des cours (référent = prof1)
            Cours poo = new Cours("POO101", "Programmation Objet", 2.0, prof1);
            Cours Eco = new Cours("ECO201", "Economie Politique",       1.5, prof1);
            g.ajouterCours(poo);
            g.ajouterCours(Eco);

            // Autoriser prof2 sur POO101 (mais PAS sur ECO201)
            g.attribuerCoursAEnseignant("POO101", "ENS-2");

            // Création d’un groupe
            Groupe g1 = new Groupe("Groupe A");
            g.ajouterGroupe(g1);

            // Création des étudiants
            Etudiant e1 = new Etudiant("ETU-1", "Toure",  "Alia", 20, "M0001", "Data Science", "S3");
            Etudiant e2 = new Etudiant("ETU-2", "Hugues", "Jean", 19, "M0002", "Informatique", "S3");
            g.ajouterEtudiant(e1);
            g.ajouterEtudiant(e2);

            // Association des étudiants et cours au groupe
            g.ajouterEtudiantAuGroupe("M0001", "Groupe A");
            g.ajouterEtudiantAuGroupe("M0002", "Groupe A");
            g.associerCoursAuGroupe("POO101", "Groupe A");
            g.associerCoursAuGroupe("ECO201",  "Groupe A");

            //Attribution des notes (mode libre, comme avant)
            g.saisirNote("M0001", "POO101", 16.0);
            g.saisirNote("M0001", "ECO201",  14.0);
            g.saisirNote("M0002", "POO101", 12.0);
            g.saisirNote("M0002", "ECO201",  10.0);

            //  Affichage des bulletins (comme avant)
            System.out.println(g.bulletin("M0001"));
            System.out.println(g.bulletin("M0002"));

            //tests connexion + droits par enseignant
            // OK : prof2 est autorisé sur POO101
            g.saisirNoteParEnseignant("prof-vidal", "secret", "M0001", "POO101", 15.5);
            System.out.println("Note saisie par prof2 sur POO101 ");

            //  prof2 n'est PAS autorisé sur ECO201
            try {
                g.saisirNoteParEnseignant("prof-vidal", "secret", "M0001", "ECO201", 9.0);
                System.out.println("cela ne devrait pas passer !");
            } catch (AutorisationException ex) {
                System.out.println("Refus attendu sur ECO201: " + ex.getMessage());
            }

            //mauvais mot de passe
            try {
                g.saisirNoteParEnseignant("prof-vidal", "mauvais", "M0001", "POO101", 13.0);
                System.out.println("authentification aurait dû échouer !");
            } catch (AuthentificationException ex) {
                System.out.println("Échec de connexion (attendu): " + ex.getMessage());
            }

        } catch (AgeInvalideException | NoteInvalideException
                 | AuthentificationException | AutorisationException e) {
            System.err.println("Erreur : " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Autre erreur : " + e.getMessage());
        }
    }
}
