# doctor/report.py
import datetime

class Report:
    def __init__(self, patient_id, report_text):
        self.patient_id = patient_id
        self.report_text = report_text
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"Medical Report for Patient ID {self.patient_id} (Timestamp: {self.timestamp}): {self.report_text}"

    def generate_report(self, Prescrptn_db):
        prescription_history = []
        flag=True
        for prescription in Prescrptn_db.prescrptn_array:
            if prescription.patient_id == self.patient_id:
                flag=False
                prescription_history.append({
                    'Prescription_ID': prescription.rx_id,
                    'Medication_Name': prescription.med_name,
                    'Strength': prescription.strength,
                    'Frequency': prescription.frequency,
                    'Date': prescription.date,
                    'Expiry_Date': prescription.expiry_date
                })
        if flag==True:
            print("have no prsccrptn existed")
        report_content = f"Prescription History for Patient ID {self.patient_id}:\n"
        report_content += "---------------------------------------------------------\n"
        for entry in prescription_history:
            report_content += f"Prescription ID: {entry['Prescription_ID']}\n"
            report_content += f"Medication Name: {entry['Medication_Name']}\n"
            report_content += f"Strength: {entry['Strength']}\n"
            report_content += f"Frequency: {entry['Frequency']}\n"
            report_content += f"Date: {entry['Date']}\n"
            report_content += f"Expiry Date: {entry['Expiry_Date']}\n"
            report_content += "---------------------------------------------------------\n"
        self.report_text = report_content


    

    def check_drug_interactions(self, Prescrptn_db):
        sample_drug_interaction_pairs = {("Aspirin", "Ibuprofen"): "Increased risk of gastrointestinal bleeding",
                                     ("Ibuprofen", "Paracetamol"): "Possible kidney damage"}

        interactions = []

        valid_prescriptions = [prescription for prescription in Prescrptn_db.prescrptn_array
                               if prescription.expiry_date >= datetime.datetime.now()
                               and prescription.patient_id == self.patient_id]

        # Check interactions between all pairs of valid prescriptions
        flag=True
        for i in range(len(valid_prescriptions)):
            for j in range(i + 1, len(valid_prescriptions)):
                drug_pair = (valid_prescriptions[i].med_name, valid_prescriptions[j].med_name)

                # Check if the drug pair is in the drug interaction pairs list
                if drug_pair in sample_drug_interaction_pairs:
                    interaction_description = sample_drug_interaction_pairs[drug_pair]
                    interactions.append((drug_pair, interaction_description))
                    flag=False
        if flag==True:
            print("no prescrtn have interactions ")
        return interactions

    def search_medication_history(self, medication_name, Prescrptn_db):
        medication_records = []
        flag=True
        for prescription in Prescrptn_db.prescrptn_array:
            if prescription.patient_id == self.patient_id and prescription.med_name == medication_name:
                flag=False
                medication_records.append({
                    'Prescription_ID': prescription.rx_id,
                    'Medication_Name': prescription.med_name,
                    'Strength': prescription.strength,
                    'Frequency': prescription.frequency,
                    'Date': prescription.date,
                    'Expiry_Date': prescription.expiry_date
                })
        if flag==True:
            print("this medicine don't exist")
        return medication_records
