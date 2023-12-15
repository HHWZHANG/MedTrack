# doctor/__init__.py
from .prescription import Prescription, Prescrptn_db
from .report import Report

current_did = 0


class Doctor:
    def __init__(self, name, address, email, phoneNumber):
        global current_did
        current_did += 1
        self.id = current_did
        self.name = name
        self.address = address
        self.email = email
        self.phoneNumber = phoneNumber

    def __str__(self):
        return f"{self.id}-{self.name} {self.address} {self.email} {self.phoneNumber} "

    def update_doctor(self, new_name=None, new_address=None, new_phoneNumber=None, new_email=None):
        if new_name is not None:
            self.name = new_name
        if new_address is not None:
            self.address = new_address
        if new_email is not None:
            self.email = new_email
        if new_phoneNumber is not None:
            self.phoneNumber = new_phoneNumber
        return True
