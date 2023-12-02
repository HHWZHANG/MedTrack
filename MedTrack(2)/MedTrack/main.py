
from patient import Patient, Reminder, Medication, Med_db


patients = []

def find_patient(id):
    for patient in patients:
        if patient.id == id:
            return patient
    return None


def patient_auth():
    print("You are a patient")
    print("Please choose:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    choice = choice.strip().lower()
    if choice == "1":
        print("Register")
        name = input("Enter patient name: ")
        # TODO: patient register
        patient = Patient(name, ...)
        patients.append(patient)
        print("Patient added successfully")
        patient(patient)
    elif choice == "2":
        print("Login")
        id = input("Enter patient ID: ")
        patient = find_patient(id)
        if patient is not None:
            patient(patient)
        else:
            print("Invalid ID, please try again")
            patient_auth()
    elif choice == "3":
        print("Exit")
        return
    else:
        print("Invalid choice")


def patient(patient):
    print(f"Welcome, {patient.name}(ID: {patient.id})")
    patient.show_reminders()
    print("Please choose:")
    #TODO: add more options





print("--------------------")
print("|     MedTrack     |")
print("--------------------")


# Choose a role
role = input("Choose a role (patient/doctor): ")
role = role.strip().lower()
if role in ["patient", "p"]:
    patient_auth()