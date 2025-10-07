-- 1. HOSPITAL (doit être inséré en premier car référencé par plusieurs tables)
INSERT INTO HOSPITAL (HOSP_NAME, COUNTRY, ADDRESS) VALUES
('King Hamad University Hospital', 'Kingdom of Bahrain', 'Sheikh Isa bin Salman Bridge, Al Sayh, Busaiteen, Bahrain'),
('Mayo Clinic', 'United States', '4500 San Pablo Road, US'),
('Bahrain Defence Force Hospital', 'Kingdom of Bahrain', 'Waly Alahed Avenue, West Riffa, Bahrain'),
('Salmaniya Hospital', 'Kingdom of Bahrain', 'Salmaniya Medical Complex, Manama, Bahrain'),
('St Thomas'' Hospital London', 'United Kingdom', 'Westminster Bridge Rd, London'),
('King Faisal Specialist Hospital & Research Centre', 'Kingdom of Saudi Arabia', 'Al Mathar Ash Shamali, Riyadh 11564, Saudi Arabia'),
('Al-Hilal Hospital', 'Kingdom of Bahrain', 'Al-Hilal Hospital, Muharraq, Bahrain'),
('Emirates Hospital', 'United Arab Emirates', 'Jumeirah Beach Rd, Dubai, UAE'),
('American Mission Hospital', 'Kingdom of Bahrain', 'Sheikh Essa Road, Manama, Bahrain'),
('Dar Al Shifa Hospital', 'Kuwait', 'Beirut Street, Hawally, Kuwait');

-- 2. MEDICINE (nécessaire pour PURCHASE et MEDICINE_COUNTRY)
INSERT INTO MEDICINE (REG_NO, MED_NAME, PRICE, EXP_DATE) VALUES
(20, 'Adol Syrup', 0.300, '2023-05-15'),
(21, 'Amoxil Capsules', 0.700, '2023-03-10'),
(22, 'Aspirin', 1.000, '2023-12-09'),
(23, 'Bonjela Gel', 0.400, '2024-09-23'),
(24, 'Paracetamol', 1.200, '2024-05-17'),
(25, 'Atorvastatin', 1.500, '2023-06-15'),
(26, 'Coversyl', 1.000, '2023-05-15'),
(27, 'Diamicron', 0.900, '2024-02-03'),
(28, 'Lipitor', 1.400, '2025-03-12'),
(29, 'Glucophage', 1.700, '2024-07-19');

-- 3. DOCTOR (nécessaire pour NURSE, DIAGNOSIS et EXAMINE)
INSERT INTO DOCTOR (DOC_ID, DNAME, GENDER, QUALIFICATION, JOB_SPECIFICATION, HOSP_NAME) VALUES 
(1, 'Abdullah', 'M', 'MBBS', 'Dermatologist', 'Bahrain Defence Force Hospital'),
(2, 'Ahmed', 'M', 'Board Certified', 'Opthalmologist', 'King Hamad University Hospital'),
(3, 'Ameera', 'F', 'MD', 'Pediatrician', 'Salmaniya Hospital'),
(4, 'Ali', 'M', 'BPT', 'Physiotherapist', 'Al-Hilal Hospital'),
(5, 'Carolina', 'F', 'MS', 'Surgeon', 'Mayo Clinic'),
(6, 'Sarah', 'F', 'MD', 'Anatomy', 'Emirates Hospital'),
(7, 'Qasim', 'M', 'MD', 'Radiologist', 'King Hamad University Hospital'),
(8, 'Fatema', 'F', 'Residency', 'Anesthologist', 'Salmaniya Hospital'),
(9, 'Khalid', 'M', 'MBBS', 'Psychiatrist', 'American Mission Hospital'),
(10, 'Amal', 'F', 'D.M.', 'Nephrologist', 'King Hamad University Hospital');

-- 4. NURSE (nécessaire pour PATIENT et DIAGNOSIS)
INSERT INTO NURSE (NURSE_ID, NAME, GENDER, DOC_ID, HOSP_NAME) VALUES
(1, 'Sanaa', 'F', 2, 'King Hamad University Hospital'),
(2, 'Kathy', 'F', 7, 'King Hamad University Hospital'),
(3, 'Mary', 'F', 5, 'Mayo Clinic'),
(4, 'Ibrahim', 'M', 8, 'Salmaniya Hospital'),
(5, 'Anaya', 'F', 3, 'Salmaniya Hospital'),
(6, 'Asha', 'F', 9, 'American Mission Hospital'),
(7, 'Zainab', 'F', 1, 'Bahrain Defence Force Hospital'),
(8, 'Zeshan', 'M', 10, 'King Hamad University Hospital'),
(9, 'Adam', 'M', 4, 'Al-Hilal Hospital'),
(10, 'Hawra', 'F', 6, 'Emirates Hospital');

-- 5. RECEPTION (nécessaire pour PATIENT et APPOINTMENT)
INSERT INTO RECEPTION (REC_ID, TEL_NO, EMAIL, HOSP_NAME) VALUES
(41, '39123456', 'khuh@gmail.com', 'King Hamad University Hospital'),
(42, '39123456', 'khuh@gmail.com', 'King Hamad University Hospital'),
(43, '39456780', 'mayoclinic@facebook.com', 'Mayo Clinic'),
(44, '33456780', 'emirateshospital@yahoo.com', 'Emirates Hospital'),
(45, '33123456', 'bdf@yahoo.com', 'Bahrain Defence Force Hospital'),
(46, '33678901', 'alhilal@facebook.com', 'Al-Hilal Hospital'),
(47, '39678901', 'daralshifa@gmail.com', 'Dar Al Shifa Hospital'),
(48, '33912045', 'st.thomashospital@gmail.com', 'St Thomas'' Hospital London'),
(49, '39912045', 'kingfaisalshrc@yahoo.com', 'King Faisal Specialist Hospital & Research Centre'),
(50, '39678901', 'daralshifa@gmail.com', 'Dar Al Shifa Hospital');

-- 6. PATIENT (nécessaire pour VISIT, PURCHASE et EXAMINE)
INSERT INTO PATIENT (SSN, FNAME, LNAME, AGE, GENDER, NURSE_ID, REC_ID) VALUES
(100000001, 'Sara', 'Majeed', 27, 'F', 7, 46),
(100000002, 'Ahmed', 'Jamaal', 59, 'M', 3, 43),
(100000003, 'Abdulla', 'Hameed', 45, 'M', 9, 48),
(100000004, 'Mariam', 'Muhammad', 40, 'F', 1, 41),
(100000005, 'Fatema', 'Hasan', 64, 'F', 6, 47),
(100000006, 'Zainab', 'Abdulla', 55, 'F', 2, 49),
(100000007, 'Khalil', 'Ibrahim', 35, 'M', 8, 44),
(100000008, 'Alyaa', 'Husain', 57, 'F', 5, 42),
(100000009, 'Khalid', 'Ahmed', 60, 'M', 4, 50),
(100000010, 'Jawad', 'Ali', 20, 'M', 10, 45);

-- 7. APPOINTMENT
INSERT INTO APPOINTMENT (APPOINT_NO, APPOINT_DATE, APPOINT_TIME, REC_ID) VALUES
(1, '2022-03-05', '07:05:03', 45),
(2, '2022-03-17', '13:30:00', 49),
(3, '2022-12-22', '09:45:00', 44),
(4, '2022-07-09', '17:20:00', 48),
(5, '2022-05-03', '12:15:00', 41),
(6, '2022-11-20', '08:05:00', 47),
(7, '2022-07-12', '15:40:00', 42),
(8, '2022-04-01', '14:00:00', 50),
(9, '2022-08-30', '10:25:00', 43),
(10, '2022-06-15', '16:50:00', 46);

-- 8. DIAGNOSIS
INSERT INTO DIAGNOSIS (DIAGNOS_NO, ISSUE_DATE, TREATMENT, REMARKS, NURSE_ID, DOC_ID) VALUES
(31, '2022-06-04', 'Physiotherapy', 'Once a month', 4, 8),
(32, '2022-05-29', 'Aromatherapy', 'Twice a week', 7, 1),
(33, '2022-06-18', 'Cyrotherapy', 'Twice a month', 5, 3),
(34, '2022-07-07', 'Phototherapy', 'Once a month', 10, 6),
(35, '2022-08-13', 'Radiotherapy', 'Once in 3 months', 2, 7),
(36, '2022-12-03', 'Immunotherapy', 'Once a month', 6, 9),
(37, '2022-07-04', 'Monotherapy', 'Once a month', 1, 2),
(38, '2022-06-04', 'Pharmacotherapy', 'Once a month', 8, 10),
(39, '2022-07-19', 'Oxygen therapy', 'Once a week', 3, 5),
(40, '2022-06-25', 'Gene therapy', 'Once a month', 9, 4);

-- 9. VISIT
INSERT INTO VISIT (VISIT_DATE, SSN, HOSP_NAME) VALUES
('2021-10-10', 100000009, 'Dar Al Shifa Hospital'),
('2020-05-15', 100000005, 'Dar Al Shifa Hospital'),
('2022-01-30', 100000006, 'King Faisal Specialist Hospital & Research Centre'),
('2019-06-04', 100000002, 'Mayo Clinic'),
('2020-12-24', 100000010, 'Bahrain Defence Force Hospital'),
('2020-11-11', 100000004, 'King Hamad University Hospital'),
('2021-02-06', 100000001, 'Al-Hilal Hospital'),
('2022-04-21', 100000003, 'St Thomas'' Hospital London'),
('2022-04-19', 100000007, 'Emirates Hospital'),
('2021-02-07', 100000008, 'King Hamad University Hospital');

-- 10. PURCHASE (corrigé pour utiliser les bons SSN)
INSERT INTO PURCHASE (SSN, REG_NO) VALUES
(100000007, 20),
(100000004, 28),
(100000009, 25),
(100000003, 21),
(100000006, 29),
(100000008, 22),
(100000002, 27),
(100000007, 24);

-- 11. EXAMINE (corrigé pour utiliser les bons DOC_ID et SSN)
INSERT INTO EXAMINE (SSN, DOC_ID) VALUES
(100000004, 1),
(100000006, 2),
(100000002, 3),
(100000009, 4),
(100000008, 5),
(100000005, 6),
(100000001, 7),
(100000007, 8),
(100000003, 9),
(100000010, 10);

-- 12. MEDICINE_COUNTRY (inversé les colonnes pour correspondre à la table)
INSERT INTO MEDICINE_COUNTRY (REG_NO, MAN_COUNTRY) VALUES
(20, 'United States'),
(21, 'Australia'),
(22, 'United States'),
(23, 'Germany'),
(24, 'United Kingdom'),
(25, 'United Kingdom'),
(26, 'Kingdom of Saudi Arabia'),
(27, 'Germany'),
(28, 'Switzerland'),
(29, 'Germany');