# doctor/__init__.py

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
        return f"Doctor(id:{self.id}, name:'{self.name}', address:'{self.address}', " \
               f"email:'{self.email}', phoneNumber:'{self.phoneNumber}')"

    def update_doctor(self):
        self.name = input("New doctor name: ") or self.name
        self.address = input("New address: ") or self.address
        self.phoneNumber = input("New phone number: ") or self.phoneNumber
        self.email = input("New email: ") or self.email
        return True
