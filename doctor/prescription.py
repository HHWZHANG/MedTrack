# doctor/prescription.py
from datetime import datetime

class Prescription:

    def __init__(self, rx_id, patient_id, doctor_id, med_name, strength, frequency, date, expiry_date):
        self.rx_id = rx_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.med_name = med_name
        self.strength = strength
        self.frequency = frequency
        self.date = date
        self.expiry_date = expiry_date

    def __str__(self):
        return f"Prescription(patient_id:{self.patient_id}, doctor_id:{self.doctor_id}, " \
               f"med_name:{self.med_name}, strength:{self.strength}, frequency:{self.frequency}, " \
               f"date:{self.date}, expiry_date:{self.expiry_date})"

    sample_freq = {
        'daily': 'Every day',
        'every other day': 'Every other day',
        'BID': 'Twice a day',
        'b.i.d.': 'Twice a day',
        'TID': 'Three times a day',
        't.i.d.': 'Three times a day',
        'QID': 'Four times a day',
        'q.i.d.': 'Four times a day',
        'QHS': 'Every bedtime',
        'Q4h': 'Every 4 hours',
        'Q4-6h': 'Every 4 to 6 hours',
        'QWK': 'Every week'
    }

    def update_prescription(self):
        self.strength = input("New prescription strength: ") or self.strength
        self.frequency = input("New frequency: ") or self.frequency
        expiry_date_input = input("Enter new expiry date (yyyy-mm-dd): ")
        self.expiry_date = datetime.strptime(expiry_date_input, "%Y-%m-%d") or self.expiry_date
        return True

    def expiry_alert(self, threshold_days=7):
        current_date = datetime.now()
        days_until_expiry = (self.expiry_date - current_date).days

        if days_until_expiry <= threshold_days:
            print(f"Prescription with ID {self.rx_id} for medication '{self.med_name}' is expiring soon. "
                  f"Expiry Date: {self.expiry_date}, Days Left: {days_until_expiry}")
            return True
        else:
            print("Prescription is still valid.")
            return False


class Prescrptn_db(Prescription):

    def __init__(self):
        self.prescrptn_array = []

    def is_exist(self, rx_id):
        for prescrptn in self.prescrptn_array:
            if prescrptn.rx_id == rx_id:
                return True
        return False

    def add_prescription(self):
        rx_id = input("Enter prescription ID (start with RX): ")
        if self.is_exist(rx_id):
            print("Prescription already exists")
            return False
        patient_id = input("Enter patient ID: ")
        doctor_id = input("Enter doctor ID: ")
        med_name = input("Enter medication name: ")
        strength = input("Enter medication strength (e.g., 50mg): ")
        print(f'Common frequencies abbreviations: {Prescription.sample_freq}')
        frequency = input("Enter frequency: ")
        date = datetime.now().date()
        expiry_date_input = input("Enter expiry date (yyyy-mm-dd): ")
        expiry_date = datetime.strptime(expiry_date_input, "%Y-%m-%d")
        prescription = Prescription(rx_id, patient_id, doctor_id, med_name, strength, frequency, date, expiry_date)
        self.prescrptn_array.append(prescription)
        return prescription

    def remove_prescription(self, n):
        for prescription in self.prescrptn_array:
            if prescription.rx_id==n:
                self.prescrptn_array.remove(prescription)
                print(f"prescription:{prescription.rx_id}has been removed")
            else:
                print("prescription not exist")
        return True

    def warning(self):
        date_input = input("Enter now time (yyyy-mm-dd): ")
        now_time = datetime.strptime(date_input, "%Y-%m-%d")
        flag=True
        for prescrptn in self.prescrptn_array:
            if prescrptn.expiry_date < now_time:
                flag=False
                print(f"prescrptn:{prescrptn.rx_id} expiry")
                print("")
        if flag==True:
            print("have no prescrptn expiry")


