# patient/reminder.py

from .medication import Medication, Med_db

from datetime import datetime, timedelta

class Reminder:
    def __init__(self, medication: Medication, time, repeat, start_date, end_date):
        self.medication = medication
        self.time = time
        self.repeat = repeat
        self.start_date = start_date
        self.end_date = end_date
        self.taken = False

    def __str__(self):
        taken_status = "Taken" if self.taken else "Not taken yet"
        return f"Reminder for {self.medication.name} at {self.time}. Status: {taken_status}"


    def show_reminder(self):
        if not self.taken and self.start_date <= datetime.now() <= self.end_date:
            if (datetime.now() - self.start_date).days % self.repeat == 0:
                print(f"{self.medication.name} at {self.time.strftime('%H:%M')}")
                return True
        return False

    def taken_reminder(self):
        self.taken = True
        return True
