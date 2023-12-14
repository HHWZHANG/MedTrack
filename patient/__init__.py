# patient/__init__.py

from .medication import Medication, Med_db
from .reminder import Reminder

from datetime import datetime, timedelta

current_id = 0

class Patient:
    def __init__(self, name, sex, marital_status, dob, address, phoneNumber, email):
        global current_id
        current_id += 1
        self.id = current_id
        self.name = name
        self.sex = sex
        self.marital_status = marital_status
        self.dob = dob
        self.address = address
        self.phoneNumber = phoneNumber
        self.email = email
        self.med_array = []
        self.reminders = []

    def __str__(self):
        return f"{self.id}-{self.name} {self.sex} {self.marital_status} {self.dob} {self.address} {self.phoneNumber} {self.email}"
    
    def update_patient(self):
        self.name = input("New patient name: ") or self.name
        self.sex = input("New sex:") or self.sex
        self.marital_status = input("New marital status: ") or self.marital_status
        self.dob = input("New date of birth: ") or self.dob
        self.address = input("New address: ") or self.address
        self.phoneNumber = input("New phone number: ") or self.phoneNumber
        self.email = input("New email: ") or self.email
        return True
    
    def add_medication(self, medication):
        self.med_array.append(medication)
        return True
    
    def remove_medication(self):
        medication = self.select_medication()
        if medication is None:
            return False
        self.med_array.remove(medication)
        return True
    
    def update_medication(self):
        medication = self.select_medication()
        if medication is None:
            return False
        medication.update_medication()
        return True
    

    def is_medication_exist_in_reminder(self, medication):
        for reminder in self.reminders:
            if reminder.medication == medication:
                return True
        return False

    def add_reminder(self):
        medication = self.select_medication()
        if medication is None:
            return False
        if self.is_medication_exist_in_reminder(medication):
            print("Reminder already exists")
            return False

        try:
            time_input = input("Enter time of reminder (e.g., 10:00): ")
            time = datetime.strptime(time_input, "%H:%M")
            repeat = int(input("Enter repeat interval (in days): "))
            start_date_input = input("Enter start date (e.g., 2020-01-01): ")
            start_date = datetime.strptime(start_date_input, "%Y-%m-%d")
            end_date_input = input("Enter end date (e.g., 2020-01-01): ")
            end_date = datetime.strptime(end_date_input, "%Y-%m-%d")
            reminder = Reminder(medication, time, repeat, start_date, end_date)
            self.reminders.append(reminder)
        except ValueError as v:
            print(v)
            return False
        return True
    
    def delete_reminder(self):
        for i, r in enumerate(self.reminders):
            print(f"{i+1}. {r}")
        try:
            reminder_index = int(input("Enter reminder index: "))
        except ValueError:
            print("Invalid reminder index")
            return False
        if reminder_index > len(self.reminders) or reminder_index < 1:
            print("Invalid reminder index")
            return False
        reminder = self.reminders[reminder_index-1]
        self.reminders.remove(reminder)
        return True
    
    def show_reminders(self):
        print("-"*10, "Today's Reminder", "-"*10, sep="")
        for reminder in self.reminders:
            reminder.show_reminder()
        print("-"*(20+len("Today's Reminder")), sep="")
        return True
        
    def show_medication_with_index(self):
        if len(self.med_array) == 0:
            print("No medications found")
            return False
        for i, med in enumerate(self.med_array):
            print(f"{i+1}. {med}")
        return True
    
    def select_medication(self):
        if self.show_medication_with_index():
            try:
                medication_index = int(input("Enter medication index: "))
            except ValueError:
                print("Invalid medication index")
                return None
            if medication_index > len(self.med_array) or medication_index < 1:
                print("Invalid medication index")
                return None
            return self.med_array[medication_index-1]
        else:
            return None
    
