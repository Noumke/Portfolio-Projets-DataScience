package ui;

import exception.AuthentificationException;
import exception.AutorisationException;
import exception.AgeInvalideException;
import exception.NoteInvalideException;
import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import model.*;
import service.Gestionnaire;
import javafx.beans.property.ReadOnlyStringWrapper;
import javafx.scene.layout.ColumnConstraints;
import javafx.scene.layout.Priority;
import javafx.scene.layout.Region;



public class FenetrePrincipale extends Application {

    private final Gestionnaire gestionnaire = new Gestionnaire();

    // État de session
    private Enseignant enseignantCourant = null;
    private String loginCourant = null;
    private String passwordCourant = null;

    // Données locales d’affichage
    private final ObservableList<Cours> tousLesCours = FXCollections.observableArrayList();
    private final ObservableList<Cours> coursAutorises = FXCollections.observableArrayList();
    private final ObservableList<Etudiant> etudiants = FXCollections.observableArrayList();
    private final ObservableList<Enseignant> enseignants = FXCollections.observableArrayList();
    private final ObservableList<Groupe> groupes = FXCollections.observableArrayList();

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Gestion des Étudiants - JavaFX");

        // Jeu de données démo
        initDemo();

        // Onglet 1 : Connexion/Saisie
        VBox tabConnexion = buildConnexionAndSaisiePane();

        // Onglet 2 : Admin
        VBox tabAdmin = buildAdminPane();

        // Onglet 3 : Groupes (création confirmée + suppression)
        VBox tabGroupes = buildGroupesPane();

        // Onglet 4 : Autorisations Prof ↔ Cours
        VBox tabAutorisations = buildAutorisationsPane();

        // Tabs
        TabPane tabs = new TabPane();
        Tab t1 = new Tab("Connexion / Saisie", tabConnexion); t1.setClosable(false);
        Tab t2 = new Tab("Admin", tabAdmin); t2.setClosable(false);
        Tab t3 = new Tab("Groupes", tabGroupes); t3.setClosable(false);
        Tab t4 = new Tab("Autorisations", tabAutorisations); t4.setClosable(false);
        tabs.getTabs().addAll(t1, t2, t3, t4);

        Scene scene = new Scene(tabs, 1040, 720);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    // Onglet Connexion / Saisie (individuelle) + Consultation bulletin
    private VBox buildConnexionAndSaisiePane() {
        Label titre = new Label("Système de Gestion des Étudiants");
        titre.setStyle("-fx-font-size: 18px; -fx-font-weight: bold;");

        // Connexion
        TextField loginField = new TextField(); loginField.setPromptText("Login (ex: prof-vidal)");
        PasswordField passwordField = new PasswordField(); passwordField.setPromptText("Mot de passe (ex: secret)");
        Button btnLogin = new Button("Se connecter");
        Button btnLogout = new Button("Se déconnecter"); btnLogout.setDisable(true);
        Label status = new Label("Non connecté");

        HBox loginBox = new HBox(10, new Label("Login:"), loginField,
                new Label("Mot de passe:"), passwordField, btnLogin, btnLogout);
        loginBox.setAlignment(Pos.CENTER_LEFT);

        VBox header = new VBox(8, titre, loginBox, status);
        header.setPadding(new Insets(12));
        header.setStyle("-fx-background-color: #f1f5f9; -fx-border-color: #e2e8f0; -fx-border-width: 0 0 1 0;");

        // Liste des cours autorisés (taille forcée + expansion)
        ListView<Cours> listCours = new ListView<>(coursAutorises);
        listCours.setMinHeight(35);
        listCours.setPrefHeight(70);
        listCours.setMaxHeight(Double.MAX_VALUE);
        listCours.setPrefWidth(Double.MAX_VALUE);

        // le ListView doit grandir dans la GridPane
        GridPane.setHgrow(listCours, Priority.ALWAYS);
        GridPane.setVgrow(listCours, Priority.ALWAYS);


        // Saisie individuelle
        TextField tfMatricule = new TextField(); tfMatricule.setPromptText("Matricule étudiant (ex: M0001)");
        TextField tfValeur = new TextField(); tfValeur.setPromptText("Note (ex: 15.5)");
        Button btnSaisirNote = new Button("Saisir note (individuelle) sur le cours sélectionné");
        btnSaisirNote.setDisable(true);

        // Consultation bulletin
        ComboBox<Etudiant> cbEtudiants = new ComboBox<>(etudiants);
        cbEtudiants.setPromptText("Choisir un étudiant"); cbEtudiants.setMaxWidth(Double.MAX_VALUE);
        Button btnAfficherBulletin = new Button("Afficher bulletin"); btnAfficherBulletin.setMaxWidth(Double.MAX_VALUE);
        // Tableau des notes de l'étudiant sélectionné
        TableView<Note> tvNotes = new TableView<>();
        tvNotes.setPrefHeight(220);

        TableColumn<Note, String> colCours = new TableColumn<>("Cours");
        colCours.setCellValueFactory(data ->
                new ReadOnlyStringWrapper(data.getValue().getCours().getLibelle()));
        colCours.setPrefWidth(260);

        TableColumn<Note, String> colCoef = new TableColumn<>("Coef");
        colCoef.setCellValueFactory(data ->
                new ReadOnlyStringWrapper(String.format("%.1f", data.getValue().getCours().getCoefficient())));
        colCoef.setPrefWidth(80);

        TableColumn<Note, String> colValeur = new TableColumn<>("Note");
        colValeur.setCellValueFactory(data ->
                new ReadOnlyStringWrapper(String.format("%.1f", data.getValue().getValeur())));
        colValeur.setPrefWidth(100);

        tvNotes.getColumns().addAll(colCours, colCoef, colValeur);

        // Label de moyenne pondérée
        Label moyenneLabel = new Label("Moyenne : —");


        TextArea console = new TextArea(); console.setEditable(false); console.setPrefRowCount(12);

        GridPane zoneSaisie = new GridPane();
        zoneSaisie.setHgap(8); zoneSaisie.setVgap(8);
        // Colonne 0 = libellés (fixe), colonnes 1–2 = s'étirent
        ColumnConstraints col0 = new ColumnConstraints();
        col0.setHgrow(Priority.NEVER);
        col0.setMinWidth(120);

        ColumnConstraints col1 = new ColumnConstraints();
        col1.setHgrow(Priority.ALWAYS);

        ColumnConstraints col2 = new ColumnConstraints();
        col2.setHgrow(Priority.ALWAYS);

        zoneSaisie.getColumnConstraints().setAll(col0, col1, col2);

        zoneSaisie.add(new Label("Cours autorisés :"), 0, 0);
        zoneSaisie.add(listCours, 0, 1, 3, 1);
        zoneSaisie.add(new Label("Matricule :"), 0, 2);
        zoneSaisie.add(tfMatricule, 1, 2);
        zoneSaisie.add(new Label("Note :"), 0, 3);
        zoneSaisie.add(tfValeur, 1, 3);
        zoneSaisie.add(btnSaisirNote, 0, 4, 3, 1);

        VBox zoneBulletin = new VBox(8,
                new Label("Consultation du bulletin (lecture seule) :"),
                cbEtudiants, btnAfficherBulletin,
                new Label("Notes de l'étudiant :"),
                tvNotes,
                moyenneLabel
        );

        zoneBulletin.setPadding(new Insets(8));
        zoneBulletin.setStyle("-fx-background-color: #f8fafc; -fx-border-color: #e2e8f0; -fx-border-radius: 6; -fx-background-radius: 6;");

        VBox root = new VBox(12, header, zoneSaisie, zoneBulletin, new Label("Journal :"), console);
        root.setPadding(new Insets(16));

        // Handlers
        btnLogin.setOnAction(e -> {
            String login = loginField.getText().trim();
            String mdp = passwordField.getText();
            try {
                Enseignant eCourant = gestionnaire.authentifier(login, mdp);
                enseignantCourant = eCourant; loginCourant = login; passwordCourant = mdp;
                btnLogin.setDisable(true); btnLogout.setDisable(false);
                loginField.setDisable(true); passwordField.setDisable(true);
                status.setText("Connecté: " + eCourant.getPrenom() + " " + eCourant.getNom());
                rafraichirCoursAutorises();
                btnSaisirNote.setDisable(false);
                console.appendText("Connexion réussie \n");
            } catch (AuthentificationException ex) {
                status.setText("Non connecté");
                console.appendText("Échec de connexion: " + ex.getMessage() + "\n");
            } catch (Exception ex) {
                status.setText("Non connecté");
                console.appendText("Erreur: " + ex.getMessage() + "\n");
            }
        });

        btnLogout.setOnAction(e -> {
            enseignantCourant = null; loginCourant = null; passwordCourant = null;
            btnLogin.setDisable(false); btnLogout.setDisable(true);
            loginField.setDisable(false); passwordField.setDisable(false);
            status.setText("Non connecté"); coursAutorises.clear(); btnSaisirNote.setDisable(true);
            console.appendText("Déconnexion effectuée \n");
        });

        btnSaisirNote.setOnAction(e -> {
            Cours selected = listCours.getSelectionModel().getSelectedItem();
            if (selected == null) { console.appendText("Choisissez d'abord un cours autorisé.\n"); return; }
            String matricule = tfMatricule.getText().trim();
            String valStr = tfValeur.getText().trim();
            if (matricule.isEmpty() || valStr.isEmpty()) { console.appendText("Renseignez matricule et note.\n"); return; }
            try {
                double note = Double.parseDouble(valStr);
                gestionnaire.saisirNoteParEnseignant(loginCourant, passwordCourant, matricule, selected.getCode(), note);
                console.appendText("Note " + note + " saisie pour " + matricule + " sur " + selected.getLibelle() + " \n");
                // Si le tableau affiche déjà cet étudiant, rafraîchir immédiatement
                Etudiant etuSel = cbEtudiants.getSelectionModel().getSelectedItem();
                if (etuSel != null && etuSel.getMatricule().equals(matricule)) {
                    tvNotes.setItems(FXCollections.observableArrayList(
                            gestionnaire.getNotesEtudiant(etuSel.getMatricule())
                    ));
                    double m2 = gestionnaire.moyennePonderee(etuSel.getMatricule());
                    moyenneLabel.setText(Double.isNaN(m2) ? "Moyenne : —" : String.format("Moyenne : %.2f", m2));
                }

            } catch (NumberFormatException nfe) {
                console.appendText("La note doit être un nombre.\n");
            } catch (AuthentificationException ex) {
                console.appendText("Connexion invalide: " + ex.getMessage() + "\n");
            } catch (AutorisationException ex) {
                console.appendText("Refus d'accès: " + ex.getMessage() + "\n");
            } catch (NoteInvalideException ex) {
                console.appendText("Note invalide: " + ex.getMessage() + "\n");
            } catch (Exception ex) {
                console.appendText("Erreur: " + ex.getMessage() + "\n");
            }
        });

        btnAfficherBulletin.setOnAction(e -> {
            Etudiant etu = cbEtudiants.getSelectionModel().getSelectedItem();
            if (etu == null) { console.appendText("Choisissez un étudiant pour afficher son bulletin.\n"); return; }
            try {
                // Charger toutes les notes de l'étudiant
                var notesEtu = FXCollections.observableArrayList(gestionnaire.getNotesEtudiant(etu.getMatricule()));
                tvNotes.setItems(notesEtu);

                // Mettre à jour la moyenne pondérée
                double m = gestionnaire.moyennePonderee(etu.getMatricule());
                moyenneLabel.setText(Double.isNaN(m) ? "Moyenne : —" : String.format("Moyenne : %.2f", m));

                // Conserver aussi le résumé texte en console
                String b = gestionnaire.bulletin(etu.getMatricule());
                console.appendText(b + "\n");

            } catch (Exception ex) {
                console.appendText("Erreur bulletin: " + ex.getMessage() + "\n");
            }
        });

        return root;
    }


    // Onglet Admin : Ajouter / Supprimer Enseignant / Cours / Étudiant
    private VBox buildAdminPane() {
        // Ajouter Enseignant
        TextField tfEId = new TextField(); tfEId.setPromptText("ID (ex: ENS-3)");
        TextField tfENom = new TextField(); tfENom.setPromptText("Nom");
        TextField tfEPrenom = new TextField(); tfEPrenom.setPromptText("Prénom");
        TextField tfEAge = new TextField(); tfEAge.setPromptText("Âge");
        TextField tfEDep = new TextField(); tfEDep.setPromptText("Département");
        TextField tfESpec = new TextField(); tfESpec.setPromptText("Spécialité");
        TextField tfELogin = new TextField(); tfELogin.setPromptText("Login (optionnel)");
        PasswordField pfEMdp = new PasswordField(); pfEMdp.setPromptText("Mot de passe (optionnel)");
        Button btnAjoutEns = new Button("Ajouter enseignant");

        VBox boxEns = new VBox(6,
                new Label("Ajouter un enseignant :"),
                new HBox(8, tfEId, tfENom, tfEPrenom, tfEAge),
                new HBox(8, tfEDep, tfESpec),
                new HBox(8, tfELogin, pfEMdp, btnAjoutEns)
        );
        boxEns.setPadding(new Insets(10));
        boxEns.setStyle("-fx-background-color:#f8fafc; -fx-border-color:#e2e8f0; -fx-border-radius:6; -fx-background-radius:6;");

        // Ajouter Cours
        TextField tfCCode = new TextField(); tfCCode.setPromptText("Code (ex: POO102)");
        TextField tfCLib = new TextField(); tfCLib.setPromptText("Libellé");
        TextField tfCCoef = new TextField(); tfCCoef.setPromptText("Coefficient");
        ComboBox<TypeCours> cbCType = new ComboBox<>(FXCollections.observableArrayList(TypeCours.values()));
        cbCType.getSelectionModel().select(TypeCours.CM);
        ComboBox<Enseignant> cbCRef = new ComboBox<>(enseignants); cbCRef.setPromptText("Référent");
        Button btnAjoutCours = new Button("Ajouter cours");

        VBox boxCours = new VBox(6,
                new Label("Ajouter un cours :"),
                new HBox(8, tfCCode, tfCLib, tfCCoef),
                new HBox(8, new Label("Type:"), cbCType, new Label("Référent:"), cbCRef, btnAjoutCours)
        );
        boxCours.setPadding(new Insets(10));
        boxCours.setStyle("-fx-background-color:#f8fafc; -fx-border-color:#e2e8f0; -fx-border-radius:6; -fx-background-radius:6;");

        //  Ajouter Étudiant
        TextField tfSId = new TextField(); tfSId.setPromptText("ID (ex: ETU-10)");
        TextField tfSNom = new TextField(); tfSNom.setPromptText("Nom");
        TextField tfSPrenom = new TextField(); tfSPrenom.setPromptText("Prénom");
        TextField tfSAge = new TextField(); tfSAge.setPromptText("Âge");
        TextField tfSMat = new TextField(); tfSMat.setPromptText("Matricule");
        TextField tfSFiliere = new TextField(); tfSFiliere.setPromptText("Filière");
        TextField tfSSem = new TextField(); tfSSem.setPromptText("Semestre");
        Button btnAjoutEtu = new Button("Ajouter étudiant");

        VBox boxEtu = new VBox(6,
                new Label("Ajouter un étudiant :"),
                new HBox(8, tfSId, tfSNom, tfSPrenom, tfSAge),
                new HBox(8, tfSMat, tfSFiliere, tfSSem, btnAjoutEtu)
        );
        boxEtu.setPadding(new Insets(10));
        boxEtu.setStyle("-fx-background-color:#f8fafc; -fx-border-color:#e2e8f0; -fx-border-radius:6; -fx-background-radius:6;");

        //  Supprimer (Enseignant / Cours / Étudiant)
        ComboBox<Enseignant> cbDelEns = new ComboBox<>(enseignants);
        cbDelEns.setPromptText("Choisir un enseignant à supprimer");
        Button btnDelEns = new Button("Supprimer enseignant");

        ComboBox<Cours> cbDelCours = new ComboBox<>(tousLesCours);
        cbDelCours.setPromptText("Choisir un cours à supprimer");
        Button btnDelCours = new Button("Supprimer cours");

        ComboBox<Etudiant> cbDelEtu = new ComboBox<>(etudiants);
        cbDelEtu.setPromptText("Choisir un étudiant à supprimer");
        Button btnDelEtu = new Button("Supprimer étudiant");

        VBox boxDelete = new VBox(6,
                new Label("Supprimer des enregistrements :"),
                new HBox(8, cbDelEns, btnDelEns),
                new HBox(8, cbDelCours, btnDelCours),
                new HBox(8, cbDelEtu, btnDelEtu)
        );
        boxDelete.setPadding(new Insets(10));
        boxDelete.setStyle("-fx-background-color:#fff7ed; -fx-border-color:#fdba74; -fx-border-radius:6; -fx-background-radius:6;");

        TextArea console = new TextArea(); console.setEditable(false); console.setPrefRowCount(10);

        VBox root = new VBox(12, boxEns, boxCours, boxEtu, boxDelete, new Label("Journal :"), console);
        root.setPadding(new Insets(12));

        // Handlers Admin
        btnAjoutEns.setOnAction(e -> {
            try {
                String id = tfEId.getText().trim();
                String nom = tfENom.getText().trim();
                String prenom = tfEPrenom.getText().trim();
                int age = Integer.parseInt(tfEAge.getText().trim());
                String dep = tfEDep.getText().trim();
                String spec = tfESpec.getText().trim();
                String login = tfELogin.getText().trim();
                String mdp = pfEMdp.getText();

                Enseignant ens;
                if (!login.isEmpty() && !mdp.isEmpty()) {
                    ens = new Enseignant(id, nom, prenom, age, dep, spec,
                            new Credentials(login, Passwords.sha256(mdp)));
                } else {
                    ens = new Enseignant(id, nom, prenom, age, dep, spec);
                }
                gestionnaire.ajouterEnseignant(ens);
                enseignants.add(ens);
                console.appendText("Enseignant ajouté: " + ens + " \n");

                tfEId.clear(); tfENom.clear(); tfEPrenom.clear(); tfEAge.clear();
                tfEDep.clear(); tfESpec.clear(); tfELogin.clear(); pfEMdp.clear();

            } catch (NumberFormatException nfe) {
                console.appendText("Âge enseignant invalide.\n");
            } catch (AgeInvalideException ex) {
                console.appendText("Âge enseignant invalide: " + ex.getMessage() + "\n");
            } catch (Exception ex) {
                console.appendText("Erreur ajout enseignant: " + ex.getMessage() + "\n");
            }
        });

        btnAjoutCours.setOnAction(e -> {
            try {
                String code = tfCCode.getText().trim();
                String lib = tfCLib.getText().trim();
                double coef = Double.parseDouble(tfCCoef.getText().trim());
                TypeCours type = cbCType.getValue();
                Enseignant ref = cbCRef.getValue();
                if (ref == null) { console.appendText("Choisissez un référent.\n"); return; }

                Cours c = new Cours(code, lib, coef, ref);
                c.setType(type);
                gestionnaire.ajouterCours(c);
                tousLesCours.add(c);
                console.appendText("Cours ajouté: " + c + " \n");

                tfCCode.clear(); tfCLib.clear(); tfCCoef.clear();
                cbCType.getSelectionModel().select(TypeCours.CM);
                cbCRef.getSelectionModel().clearSelection();

            } catch (NumberFormatException nfe) {
                console.appendText("Coefficient invalide.\n");
            } catch (Exception ex) {
                console.appendText("Erreur ajout cours: " + ex.getMessage() + "\n");
            }
        });

        btnAjoutEtu.setOnAction(e -> {
            try {
                String id = tfSId.getText().trim();
                String nom = tfSNom.getText().trim();
                String prenom = tfSPrenom.getText().trim();
                int age = Integer.parseInt(tfSAge.getText().trim());
                String mat = tfSMat.getText().trim();
                String fil = tfSFiliere.getText().trim();
                String sem = tfSSem.getText().trim();

                Etudiant etu = new Etudiant(id, nom, prenom, age, mat, fil, sem);
                gestionnaire.ajouterEtudiant(etu);
                etudiants.add(etu);
                console.appendText("Étudiant ajouté: " + etu + " \n");

                tfSId.clear(); tfSNom.clear(); tfSPrenom.clear(); tfSAge.clear();
                tfSMat.clear(); tfSFiliere.clear(); tfSSem.clear();

            } catch (NumberFormatException nfe) {
                console.appendText("Âge étudiant invalide.\n");
            } catch (AgeInvalideException ex) {
                console.appendText("Âge étudiant invalide: " + ex.getMessage() + "\n");
            } catch (Exception ex) {
                console.appendText("Erreur ajout étudiant: " + ex.getMessage() + "\n");
            }
        });

        // Handlers Suppression
        btnDelEns.setOnAction(e -> {
            Enseignant sel = cbDelEns.getSelectionModel().getSelectedItem();
            if (sel == null) { console.appendText("Sélectionnez un enseignant.\n"); return; }

            Alert confirm = new Alert(Alert.AlertType.CONFIRMATION,
                    "Supprimer définitivement l'enseignant " + sel.getPrenom() + " " + sel.getNom() + " (" + sel.getId() + ") ?",
                    ButtonType.OK, ButtonType.CANCEL);
            confirm.setHeaderText("Confirmation de suppression");
            confirm.showAndWait();
            if (confirm.getResult() != ButtonType.OK) return;

            try {
                boolean ok = gestionnaire.supprimerEnseignant(sel.getId());
                if (ok) {
                    enseignants.remove(sel);
                    // Si cet enseignant était référent d'un cours supprimé ailleurs, la combo cours se mettra à jour via les listes
                    console.appendText("Enseignant supprimé: " + sel.getId() + " \n");
                    cbDelEns.getSelectionModel().clearSelection();
                } else {
                    console.appendText("Enseignant introuvable côté service.\n");
                }
            } catch (IllegalStateException ise) {
                console.appendText("Refus : " + ise.getMessage() + "\n");
            } catch (Exception ex) {
                console.appendText("Erreur suppression enseignant: " + ex.getMessage() + "\n");
            }
        });

        btnDelCours.setOnAction(e -> {
            Cours sel = cbDelCours.getSelectionModel().getSelectedItem();
            if (sel == null) { console.appendText("Sélectionnez un cours.\n"); return; }

            Alert confirm = new Alert(Alert.AlertType.CONFIRMATION,
                    "Supprimer définitivement le cours " + sel.getLibelle() + " (" + sel.getCode() + ") ?\n" +
                            "Les notes liées à ce cours seront supprimées.",
                    ButtonType.OK, ButtonType.CANCEL);
            confirm.setHeaderText("Confirmation de suppression");
            confirm.showAndWait();
            if (confirm.getResult() != ButtonType.OK) return;

            try {
                boolean ok = gestionnaire.supprimerCours(sel.getCode());
                if (ok) {
                    tousLesCours.remove(sel);
                    // si un prof est connecté, on met à jour directement ses cours autorisés
                    rafraichirCoursAutorises();
                    console.appendText("Cours supprimé: " + sel.getCode() + " \n");
                    cbDelCours.getSelectionModel().clearSelection();
                } else {
                    console.appendText("Cours introuvable côté service.\n");
                }
            } catch (Exception ex) {
                console.appendText("Erreur suppression cours: " + ex.getMessage() + "\n");
            }
        });

        btnDelEtu.setOnAction(e -> {
            Etudiant sel = cbDelEtu.getSelectionModel().getSelectedItem();
            if (sel == null) { console.appendText("Sélectionnez un étudiant.\n"); return; }

            Alert confirm = new Alert(Alert.AlertType.CONFIRMATION,
                    "Supprimer définitivement l'étudiant " + sel.getPrenom() + " " + sel.getNom() + " (" + sel.getMatricule() + ") ?\n" +
                            "Toutes ses notes seront supprimées.",
                    ButtonType.OK, ButtonType.CANCEL);
            confirm.setHeaderText("Confirmation de suppression");
            confirm.showAndWait();
            if (confirm.getResult() != ButtonType.OK) return;

            try {
                boolean ok = gestionnaire.supprimerEtudiant(sel.getMatricule());
                if (ok) {
                    etudiants.remove(sel);
                    console.appendText("Étudiant supprimé: " + sel.getMatricule() + " \n");
                    cbDelEtu.getSelectionModel().clearSelection();
                } else {
                    console.appendText("Étudiant introuvable côté service.\n");
                }
            } catch (Exception ex) {
                console.appendText("Erreur suppression étudiant: " + ex.getMessage() + "\n");
            }
        });

        return root;
    }


    // créer CM/TD/TP (confirme), supprimer, affecter/retirer étudiants, associer cours

    private VBox buildGroupesPane() {
        // Création d’un groupe
        TextField tfNomGroupe = new TextField(); tfNomGroupe.setPromptText("Nom du groupe (ex: TD1)");
        ComboBox<TypeCours> cbTypeGroupe = new ComboBox<>(FXCollections.observableArrayList(TypeCours.values()));
        cbTypeGroupe.getSelectionModel().select(TypeCours.TD);
        Button btnCreerGroupe = new Button("Créer groupe");
        HBox boxCreate = new HBox(8, new Label("Créer groupe:"), tfNomGroupe, new Label("Type:"), cbTypeGroupe, btnCreerGroupe);
        boxCreate.setAlignment(Pos.CENTER_LEFT);

        // Sélection d’un groupe à gérer
        ComboBox<Groupe> cbGroupes = new ComboBox<>(groupes);
        cbGroupes.setPromptText("Sélectionner un groupe");
        cbGroupes.setMaxWidth(Double.MAX_VALUE);
        Button btnSupprimerGroupe = new Button("Supprimer groupe");

        // Listes étudiants
        ListView<Etudiant> lvTousEtudiants = new ListView<>(etudiants);
        lvTousEtudiants.setPrefSize(360, 260);

        ObservableList<Etudiant> lvEtudiantsDuGroupe = FXCollections.observableArrayList();
        ListView<Etudiant> lvGroupe = new ListView<>(lvEtudiantsDuGroupe);
        lvGroupe.setPrefSize(360, 260);

        Button btnAdd = new Button(">>");
        Button btnRemove = new Button("<<");
        VBox boxButtons = new VBox(10, btnAdd, btnRemove);
        boxButtons.setAlignment(Pos.CENTER);

        // Association cours ↔ groupe
        ComboBox<Cours> cbCoursAssoc = new ComboBox<>(tousLesCours);
        cbCoursAssoc.setPromptText("Cours à associer");
        Button btnAssocierCours = new Button("Associer au groupe");
        ListView<Cours> lvCoursDuGroupe = new ListView<>();
        lvCoursDuGroupe.setPrefHeight(120);

        // Console
        TextArea console = new TextArea(); console.setEditable(false); console.setPrefRowCount(8);

        // Layout
        TitledPane paneCreate = new TitledPane("Création de groupe", boxCreate); paneCreate.setCollapsible(false);

        HBox lists = new HBox(12,
                new VBox(6, new Label("Tous les étudiants"), lvTousEtudiants),
                boxButtons,
                new VBox(6, new Label("Étudiants du groupe"), lvGroupe)
        );

        HBox selectGroupRow = new HBox(8, new Label("Groupe :"), cbGroupes, btnSupprimerGroupe);
        selectGroupRow.setAlignment(Pos.CENTER_LEFT);

        TitledPane paneAffect = new TitledPane("Affectation d'étudiants", new VBox(8, selectGroupRow, lists)); paneAffect.setCollapsible(false);
        TitledPane paneCours = new TitledPane("Cours du groupe",
                new VBox(8, new HBox(8, cbCoursAssoc, btnAssocierCours), lvCoursDuGroupe)); paneCours.setCollapsible(false);

        VBox root = new VBox(12, paneCreate, paneAffect, paneCours, new Label("Journal :"), console);
        root.setPadding(new Insets(12));

        // Handlers
        btnCreerGroupe.setOnAction(e -> {
            try {
                String nom = tfNomGroupe.getText().trim();
                TypeCours type = cbTypeGroupe.getValue();
                if (nom.isEmpty()) { console.appendText("Nom de groupe requis.\n"); return; }

                boolean existe = groupes.stream().anyMatch(gx -> gx.getNom().equalsIgnoreCase(nom));
                if (existe) { console.appendText("Groupe déjà existant: " + nom + "\n"); return; }

                Alert confirm = new Alert(Alert.AlertType.CONFIRMATION,
                        "Créer le groupe \"" + nom + "\" (" + type + ") ?",
                        ButtonType.OK, ButtonType.CANCEL);
                confirm.setHeaderText("Confirmation");
                confirm.showAndWait();
                if (confirm.getResult() != ButtonType.OK) return;

                Groupe g = new Groupe(nom, type);
                gestionnaire.ajouterGroupe(g);
                groupes.add(g);
                console.appendText("Groupe créé: " + g + " \n");
                tfNomGroupe.clear(); cbTypeGroupe.getSelectionModel().select(TypeCours.TD);
            } catch (Exception ex) {
                console.appendText("Erreur création groupe: " + ex.getMessage() + "\n");
            }
        });

        btnSupprimerGroupe.setOnAction(e -> {
            Groupe g = cbGroupes.getSelectionModel().getSelectedItem();
            if (g == null) { console.appendText("Choisissez un groupe à supprimer.\n"); return; }

            Alert confirm = new Alert(Alert.AlertType.CONFIRMATION,
                    "Supprimer définitivement le groupe \"" + g.getNom() + "\" ?",
                    ButtonType.OK, ButtonType.CANCEL);
            confirm.setHeaderText("Confirmation de suppression");
            confirm.showAndWait();
            if (confirm.getResult() != ButtonType.OK) return;

            try {
                boolean ok = gestionnaire.supprimerGroupe(g.getNom());
                if (ok) {
                    groupes.remove(g);
                    lvEtudiantsDuGroupe.clear();
                    lvGroupe.setItems(lvEtudiantsDuGroupe);
                    lvCoursDuGroupe.setItems(FXCollections.observableArrayList());
                    cbGroupes.getSelectionModel().clearSelection();
                    console.appendText("Groupe supprimé: " + g.getNom() + " \n");
                } else {
                    console.appendText("Groupe introuvable côté service: " + g.getNom() + "\n");
                }
            } catch (Exception ex) {
                console.appendText("Erreur suppression groupe: " + ex.getMessage() + "\n");
            }
        });

        cbGroupes.setOnAction(e -> {
            Groupe g = cbGroupes.getSelectionModel().getSelectedItem();
            if (g == null) return;
            lvEtudiantsDuGroupe.setAll(g.getEtudiants());
            lvGroupe.setItems(lvEtudiantsDuGroupe);
            lvCoursDuGroupe.setItems(FXCollections.observableArrayList(g.getCours()));
        });

        btnAdd.setOnAction(e -> {
            Groupe g = cbGroupes.getSelectionModel().getSelectedItem();
            Etudiant selected = lvTousEtudiants.getSelectionModel().getSelectedItem();
            if (g == null) { console.appendText("Choisissez un groupe.\n"); return; }
            if (selected == null) { console.appendText("Sélectionnez un étudiant à ajouter.\n"); return; }
            try {
                gestionnaire.ajouterEtudiantAuGroupe(selected.getMatricule(), g.getNom());
                lvEtudiantsDuGroupe.setAll(g.getEtudiants());
                console.appendText("Ajouté " + selected.getMatricule() + " à " + g.getNom() + " \n");
            } catch (Exception ex) {
                console.appendText("Erreur ajout étudiant: " + ex.getMessage() + "\n");
            }
        });

        btnRemove.setOnAction(e -> {
            Groupe g = cbGroupes.getSelectionModel().getSelectedItem();
            Etudiant selected = lvGroupe.getSelectionModel().getSelectedItem();
            if (g == null) { console.appendText("Choisissez un groupe.\n"); return; }
            if (selected == null) { console.appendText("Sélectionnez un étudiant à retirer.\n"); return; }
            try {
                g.retirerEtudiant(selected);
                lvEtudiantsDuGroupe.setAll(g.getEtudiants());
                console.appendText("Retiré " + selected.getMatricule() + " de " + g.getNom() + " \n");
            } catch (Exception ex) {
                console.appendText("Erreur retrait étudiant: " + ex.getMessage() + "\n");
            }
        });

        btnAssocierCours.setOnAction(e -> {
            Groupe g = cbGroupes.getSelectionModel().getSelectedItem();
            Cours c = cbCoursAssoc.getSelectionModel().getSelectedItem();
            if (g == null) { console.appendText("Choisissez un groupe.\n"); return; }
            if (c == null) { console.appendText("Choisissez un cours à associer.\n"); return; }
            try {
                gestionnaire.associerCoursAuGroupe(c.getCode(), g.getNom());
                lvCoursDuGroupe.setItems(FXCollections.observableArrayList(g.getCours()));
                console.appendText("Cours " + c.getCode() + " associé à " + g.getNom() + " \n");
            } catch (Exception ex) {
                console.appendText("Erreur association cours: " + ex.getMessage() + "\n");
            }
        });

        return root;
    }


    //  attribuer/retirer des profs autorisés par cours

    private VBox buildAutorisationsPane() {
        ComboBox<Cours> cbCours = new ComboBox<>(tousLesCours);
        cbCours.setPromptText("Choisir un cours");
        cbCours.setMaxWidth(Double.MAX_VALUE);

        // Listes profs autorisés / non autorisés
        ObservableList<Enseignant> profsAutorises = FXCollections.observableArrayList();
        ObservableList<Enseignant> profsDispo = FXCollections.observableArrayList();

        ListView<Enseignant> lvAutorises = new ListView<>(profsAutorises);
        lvAutorises.setPrefSize(360, 260);
        ListView<Enseignant> lvDisponibles = new ListView<>(profsDispo);
        lvDisponibles.setPrefSize(360, 260);

        Button btnAutoriser = new Button("Autoriser >>");
        Button btnRetirer = new Button("<< Retirer");
        VBox boxBtns = new VBox(10, btnAutoriser, btnRetirer);
        boxBtns.setAlignment(Pos.CENTER);

        TextArea console = new TextArea(); console.setEditable(false); console.setPrefRowCount(8);

        HBox lists = new HBox(12,
                new VBox(6, new Label("Professeurs disponibles"), lvDisponibles),
                boxBtns,
                new VBox(6, new Label("Professeurs autorisés sur le cours"), lvAutorises)
        );

        VBox root = new VBox(12,
                new HBox(8, new Label("Cours :"), cbCours),
                lists,
                new Label("Journal :"), console
        );
        root.setPadding(new Insets(12));

        // Handlers
        cbCours.setOnAction(e -> {
            Cours c = cbCours.getSelectionModel().getSelectedItem();
            if (c == null) return;
            // Recalcule les deux listes en fonction du cours choisi
            profsAutorises.setAll(enseignants.filtered(c::estAutorise));
            profsDispo.setAll(enseignants.filtered(e1 -> !c.estAutorise(e1)));
        });

        btnAutoriser.setOnAction(e -> {
            Cours c = cbCours.getSelectionModel().getSelectedItem();
            Enseignant sel = lvDisponibles.getSelectionModel().getSelectedItem();
            if (c == null) { console.appendText("Choisissez un cours.\n"); return; }
            if (sel == null) { console.appendText("Choisissez un professeur à autoriser.\n"); return; }
            if (c.autoriser(sel)) {
                profsDispo.remove(sel);
                profsAutorises.add(sel);
                console.appendText("Autorisé " + sel.getPrenom() + " " + sel.getNom() + " sur " + c.getCode() + " \n");
            } else {
                console.appendText("Déjà autorisé.\n");
            }
        });

        btnRetirer.setOnAction(e -> {
            Cours c = cbCours.getSelectionModel().getSelectedItem();
            Enseignant sel = lvAutorises.getSelectionModel().getSelectedItem();
            if (c == null) { console.appendText("Choisissez un cours.\n"); return; }
            if (sel == null) { console.appendText("Choisissez un professeur à retirer.\n"); return; }
            if (c.retirerAutorisation(sel)) {
                profsAutorises.remove(sel);
                profsDispo.add(sel);
                console.appendText("Autorisation retirée pour " + sel.getPrenom() + " " + sel.getNom() + " sur " + c.getCode() + " ✅\n");
            } else {
                console.appendText("Impossible de retirer (le référent reste autorisé ou non présent).\n");
            }
        });

        return root;
    }
    // Données poiur faire une demonstration

    private void initDemo() {
        try {
            // Enseignants
            Enseignant prof1 = new Enseignant("ENS-1", " Bergeron", "Jean yves", 31, "Sciences des données", "Economie");
            gestionnaire.ajouterEnseignant(prof1);

            Credentials cred = new Credentials("prof-vidal", Passwords.sha256("secret"));
            Enseignant prof2 = new Enseignant("ENS-2", "Vidal", "Morgane", 42, "Sciences des données", "Java", cred);
            gestionnaire.ajouterEnseignant(prof2);

            enseignants.setAll(prof1, prof2);

            // Cours (référent = prof1)
            Cours poo = new Cours("POO101", "Programmation Objet", 2.0, prof2);
            Cours Econ  = new Cours("ECO201",  "Economie Politique",    1.5, prof1);
            gestionnaire.ajouterCours(poo);
            gestionnaire.ajouterCours(Econ);

            // Autoriser prof2 uniquement sur POO101
            gestionnaire.attribuerCoursAEnseignant("POO101", "ENS-2");

            // Groupes et étudiants
            Groupe g1 = new Groupe("Groupe A", TypeCours.TD);
            gestionnaire.ajouterGroupe(g1);
            groupes.add(g1);

            Etudiant e1 = new Etudiant("ETU-1", "Toure",  "Nomouke", 19, "M0001", "Sciences des donnees", "S3");
            Etudiant e2 = new Etudiant("ETU-2", "Hugues", "Jean", 24, "M0002", "Informatique", "S3");
            gestionnaire.ajouterEtudiant(e1);
            gestionnaire.ajouterEtudiant(e2);

            gestionnaire.ajouterEtudiantAuGroupe("M0001", "Groupe A");
            gestionnaire.ajouterEtudiantAuGroupe("M0002", "Groupe A");
            gestionnaire.associerCoursAuGroupe("POO101", "Groupe A");
            gestionnaire.associerCoursAuGroupe("ECO201",  "Groupe A");

            // listes locales
            tousLesCours.setAll(poo, Econ);
            etudiants.setAll(e1, e2);

        } catch (AgeInvalideException ex) {
            throw new RuntimeException("Échec init démo (âge): " + ex.getMessage(), ex);
        }
    }

    private void rafraichirCoursAutorises() {
        coursAutorises.clear();
        if (enseignantCourant == null) return;
        for (Cours c : tousLesCours) {
            if (c.estAutorise(enseignantCourant)) {
                coursAutorises.add(c);
            }
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
