\COPY client(id_client, nom, prenom, civilite, ddn, adresse, cp, ville, matricule_agent) FROM 'C:/Users/ibtou/OneDrive/Con-Im-BD/client.csv' DELIMITER ',' CSV HEADER;

\COPY agent(matricule_agent, nom_agent, ddn_agent, civilite_agent) FROM 'C:/Users/ibtou/OneDrive/Con-Im-BD/agent.csv' DELIMITER ',' CSV HEADER;

\COPY compte(numcpt, designation_compte, date_rattachement, type_rattachement, id_client) FROM 'C:/Users/ibtou/OneDrive/Con-Im-BD/compte.csv' DELIMITER ',' CSV HEADER;

\COPY mouvement(id_mouvement, dt_mouvement, montant, designation_mouvement, numcpt, id_client) FROM 'C:/Users/ibtou/OneDrive/Con-Im-BD/mouvement_modifie.csv' DELIMITER ',' CSV HEADER;

\COPY parrainage(id_client_parrain, id_client_filleul, date_parrainage, nom_parrain) FROM 'C:/Users/ibtou/OneDrive/Con-Im-BD/parrainage_corrige.csv' DELIMITER ',' CSV HEADER;

--les scripts d'exporations 
\COPY client(id_client, nom, prenom, civilite, ddn, adresse, cp, ville, matricule_agent) TO 'C:/Users/ibtou/OneDrive/Con-Im-BD/export_client.csv' DELIMITER ',' CSV HEADER;
\COPY agent(matricule_agent, nom_agent, ddn_agent, civilite_agent) TO 'C:/Users/ibtou/OneDrive/Con-Im-BD/export_agent.csv' DELIMITER ',' CSV HEADER;
\COPY compte(numcpt, designation_compte, date_rattachement, type_rattachement, id_client) TO 'C:/Users/ibtou/OneDrive/Con-Im-BD/export_compte.csv' DELIMITER ',' CSV HEADER;
\COPY mouvement(id_mouvement, dt_mouvement, montant, designation_mouvement, numcpt, id_client) TO 'C:/Users/ibtou/OneDrive/Con-Im-BD/export_mouvement.csv' DELIMITER ',' CSV HEADER;
\COPY parrainage(id_client_parrain, id_client_filleul, date_parrainage, nom_parrain) TO 'C:/Users/ibtou/OneDrive/Con-Im-BD/export_parrainage.csv' DELIMITER ',' CSV HEADER;
