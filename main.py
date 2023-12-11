
from patient import Patient, Reminder, Medication, Med_db
from doctor import Doctor

med_db = Med_db()
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
        sex = input("Enter sex (Male/Female/Other): ")
        marital_status = input("Enter marital status (Single/Married/Divorced/Widowed): ")
        dob = input("Enter date of birth (YYYY-MM-DD): ")
        address = input("Enter address: ")
        phoneNumber = input("Enter phone number: ")
        email = input("Enter email: ")
        patient = Patient(name, sex, marital_status,dob, address, phoneNumber, email)
        patients.append(patient)
        print("Patient added successfully")
        patient_menu(patient)
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


def patient_menu(patient):
    while True:
        print(f"Welcome, {patient.name} (ID: {patient.id})")
        patient.show_reminders()
        print("Please choose:")
        print("1. Update Personal Information")
        print("2. Add Medication")
        print("3. Remove Medication")
        print("4. Update Medication")
        print("5. Add Reminder")
        print("6. Delete Reminder")
        print("7. Show All Reminders")
        print("8. Add Medication to Medication Database")
        print("9. Logout")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            patient.update_patient()
        elif choice == "2":
            medication = med_db.search_medication_CLI()
            patient.add_medication(medication)
        elif choice == "3":
            patient.remove_medication()
        elif choice == "4":
            patient.update_medication()
        elif choice == "5":
            patient.add_reminder()
        elif choice == "6":
            patient.delete_reminder()
        elif choice == "7":
            patient.show_reminders()
        elif choice == "8":
            medication = med_db.add_medication()
            if medication is not None:
                print("Medication added successfully")
        elif choice == "9":
            print("Logging out...")
            break
        else:
            print("Invalid choice, please try again.")





print("--------------------")
print("|     MedTrack     |")
print("--------------------")




# Choose a role
role = input("Choose a role (patient/doctor): ")
role = role.strip().lower()
if role in ["patient", "p"]:
    patient_auth()
