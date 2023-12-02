# doctor/prescription.py
import datetime

class Prescription:
    def __init__(self, patient_id, medication_details, expiry_date):
        self.patient_id = patient_id
        self.medication_details = medication_details
        self.expiry_date = expiry_date

    def __str__(self):
        return f"Prescription for Patient ID {self.patient_id}, Medication: {self.medication_details}, Expiry Date: {self.expiry_date}"

prescriptions = []

def add_prescription(patient_id, medication_details, expiry_date):
    prescription = Prescription(patient_id, medication_details, expiry_date)
    prescriptions.append(prescription)
    return prescription

def update_prescription(prescription_id, updated_info):
    if prescription_id < len(prescriptions):
        prescription = prescriptions[prescription_id]
        prescription.medication_details = updated_info.get('medication_details', prescription.medication_details)
        prescription.expiry_date = updated_info.get('expiry_date', prescription.expiry_date)
        return prescription
    else:
        raise ValueError("Prescription not found.")

def expiry_alert(prescription_id, threshold_days=7):
    if prescription_id < len(prescriptions):
        prescription = prescriptions[prescription_id]
        today = datetime.date.today()
        expiry_date = datetime.datetime.strptime(prescription.expiry_date, "%Y-%m-%d").date()
        days_until_expiry = (expiry_date - today).days

        if days_until_expiry <= threshold_days:
            print(f"Reminder: Your prescription for Medication ({prescription.medication_details}) is close to expiring on {prescription.expiry_date}. Please consider renewing it.")

    else:
        raise ValueError("Prescription not found.")

