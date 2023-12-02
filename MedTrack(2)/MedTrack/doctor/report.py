# doctor/report.py
import datetime

class Report:
    def __init__(self, patient_id, report_text):
        self.patient_id = patient_id
        self.report_text = report_text
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"Medical Report for Patient ID {self.patient_id} (Timestamp: {self.timestamp}): {self.report_text}"

reports = []

def generate_report(patient_id, report_text):
    report = Report(patient_id, report_text)
    reports.append(report)
    return report

def search_medication_history(patient_id):
    patient_reports = [report for report in reports if report.patient_id == patient_id]
    return patient_reports

def drug_interaction(medications):
    # Implement the logic to check for drug interactions among the provided medications
    interaction_message = "No potential drug interactions found."
    return interaction_message
