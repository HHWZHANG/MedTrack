from patient import Patient, Reminder, Medication, Med_db
from doctor import Doctor, Prescription,  Prescrptn_db,Report

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
    try:
        choice = int(input("Enter your choice: "))
        if choice not in [1,2,3]:
            raise ValueError
    except ValueError:
        print("Please input right number")
        patient_auth()

    if choice == 1:
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
    elif choice == 2:
        print("Login")
        id = input("Enter patient ID: ")
        patient = find_patient(id)
        if patient is not None:
            patient(patient)
        else:
            print("Invalid ID, please try again")
            patient_auth()
    elif choice == 3:
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
        try:
            choice = int(input("Enter your choice: "))
            if choice not in [1,2,3,4,5,6,7,8,9]:
                raise ValueError
        except ValueError:
            print("Please input right number for choice")
            continue

        if choice == 1:
            patient.update_patient()
        elif choice == 2:
            medication = med_db.search_medication_CLI()
            patient.add_medication(medication)
        elif choice == 3:
            patient.remove_medication()
        elif choice == 4:
            patient.update_medication()
        elif choice == 5:
            patient.add_reminder()
        elif choice == 6:
            patient.delete_reminder()
        elif choice == 7:
            patient.show_reminders()
        elif choice == 8:
            medication = med_db.add_medication()
            if medication is not None:
                print("Medication added successfully")
        elif choice == 9:
            print("Logging out...")
            break
        else:
            print("Invalid choice, please try again.")


prescrptn_db=Prescrptn_db()

doctors = []

def find_doctor(id):
    for doctor in doctors:
        if doctor.id == id:
            return doctor
    return None

def doctor_auth():
    print("You are a doctor")
    print("Please choose:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    try:
        choice = int(input("Enter your choice: "))
        if choice not in [1,2,3]:
            raise ValueError
    except ValueError:
        print("Please input right number")
        doctor_auth()
    if choice == 1:
        print("Register")
        name = input("Enter doctor name: ")
        # TODO: doctor register
        address = input("Enter address: ")
        email = input("Enter email: ")
        phoneNumber =input("Enter phone number: ")
        doctor = Doctor(name, address, email, phoneNumber)
        doctors.append(doctor)
        print("Doctor added successfully")
        doctor_menu(doctor)
    elif choice == 2:
        print("Login")
        id = input("Enter doctor ID: ")
        doctor = find_doctor(id)
        if doctor is not None:
            doctor(doctor)
        else:
            print("Invalid ID, please try again")
            doctor_auth()
    elif choice == 3:
        print("Exit")
        return
    else:
        print("Invalid choice")

def doctor_menu(doctor):
    while True:
        print(f"Welcome, {doctor.name}(ID: {doctor.id})")
        print("Please choose:")
        print("1. add new prescriptions")
        print("2. delet prescriptions")
        print("3. warning expiration")
        print("4. Check for interactions between medications")
        print("5. Export the medication history of a patient")
        print("6. Search for a patient's medication records")
        print("7. Logout")
        try:
            choice = int(input("Enter your choice: "))
            if choice not in [1,2,3,4,5,6]:
                raise ValueError
        except ValueError:
            print("Please input right number for choice")
            continue
        if choice == 1:
            prescrptn_db.add_prescription()
        elif choice == 2:
            prescrptn=input("please input prescrptn you want remove：")
            prescrptn_db.remove_prescription(prescrptn)
        elif choice == 3:
            prescrptn_db.warning()
        elif choice == 4:
            ID=input("please input patient id")
            report1=Report(ID,"")
            report1.check_drug_interactions(prescrptn_db)
        elif choice == 5:
            ID = input("please input patient id")
            report2 = Report(ID, "")
            report2.generate_report(prescrptn_db)
        elif choice == 6:
            ID = input("please input patient id")
            med_name=input("please int medicine name")
            report3 = Report(ID, "")
            report3.search_medication_history(med_name,prescrptn_db)
        elif choice == 7:
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
if role in ["doctor", "d"]:
    doctor_auth()
