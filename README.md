# MedTrack

## About The Project

A software package named "MedTrack App". This app is designed to assist patients in managing their medication regimen. It provides a comprehensive solution for managing medication schedules, prescription details, and drug interactions, benefiting patients and doctors. It emphasizes user-friendly interfaces and reminders, ensuring effective medication management and adherence to prescribed treatments.

### Table of content:
```
│  .coverage
│  .DS_Store
│  .travis.yml
│  cover.png
│  DATA533projectstep1.pdf
│  list.txt
│  main.py
│  README.md
│  requirements.txt
│  test_doctor.py
│  test_patient.py
│  TravisCI.png
│
├─doctor
│  │  prescription.py
│  │  report.py
│  │  __init__.py
│  │
│
├─patient
│  │  medication.py
│  │  reminder.py
│  │  __init__.py
```

### Features
Patient Registration and Login: Secure registration and login system for patients.

Personal Information Management: Patients can update their personal details such as name, sex, marital status, date of birth, address, contact information, and email.

Medication Management: Allows patients to add, update, or remove their medication details.

Reminder System: Patients can set, view, and delete reminders for medication intake.

Data Persistence: (If implemented) Ensures all patient information and reminders are saved and retrieved between sessions.

Add_prescription: For doctors to add new prescriptions.

Delete_prescription: Allows the deletion of prescriptions.

Expiry_alert: Notifies about the expiry of prescriptions

Drug_interaction: Checks for interactions between drugs.

Export_history: Exports the medication history of a patient.

Search_history: Searches through the medication history.




### TravisCI

[![Build Status](https://app.travis-ci.com/HHWZHANG/MedTrack.svg?branch=main)](https://app.travis-ci.com/HHWZHANG/MedTrack)

### Coverage
![image](./cover.png)

### Authors
Hanwen Zhang

Zerui Zhang
