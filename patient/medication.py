# patient/medication.py



class Medication:
    def __init__(self, name, med_type, strength, frequency,is_prescription):
        self.name = name
        self.med_type = med_type
        self.strength = strength
        self.frequency = frequency
        self.is_prescription = is_prescription

    def __str__(self):
        return f"{self.name} ({self.med_type}, {self.strength}, {self.frequency})"
    
    def update_medication(self):
        self.med_type = input("New medication type: ") or self.med_type
        self.strength = input("New medication strength: ") or self.strength
        self.frequency = input("New frequency of intake: ") or self.strength
        return True

    def is_prescription(self):
        prescription_input = input("Is this a prescription medication? (yes/no): ")
        is_prescription = prescription_input.strip().lower() == 'yes'
        self.is_prescription = is_prescription


class Med_db(Medication):
    def __init__(self):
        self.med_array = []


    def is_exist(self, name):
        for med in self.med_array:
            if med.name == name:
                return True
        return False

    def add_medication(self):
        name = input("Enter medication name: ")
        if self.is_exist(name):
            print("Medication already exists")
            return None
        med_type = input("Enter medication type (e.g., tablet, syrup): ")
        strength = input("Enter medication strength (e.g., 500mg): ")
        frequency = input("Enter frequency of medication intake: ")
        is_prescription = input("Is this a prescription medication? (y/n): ")
        is_prescription = is_prescription.strip().lower() == 'y'
        medication = Medication(name, med_type, strength, frequency, is_prescription)
        self.med_array.append(medication)
        return medication


    def search_medication_CLI(self):
        name = input("Enter medication name: ")
        med_ret_list = []
        for med in self.med_array:
            if name in med.name:
                med_ret_list.append(med)
        if len(med_ret_list) == 0:
            print("No medication found")
            return None
        else:
            print("Medication found:")
            for i in range(len(med_ret_list)):
                print(f"{i+1}. {med_ret_list[i]}")
            choice = input("Enter your choice: ")
            choice = int(choice)
            return med_ret_list[choice-1]
        
    # def del_medication(self):
    #     print("Remove Medication")
    #     medication_name = input("Enter the name of the medication to remove: ")

    #     # Find the medication by name
    #     medication_to_remove = None
    #     for med in self.med_array:
    #         if med.name.lower() == medication_name.lower():
    #             medication_to_remove = med
    #             break

    #     # Remove the medication if found
    #     if medication_to_remove:
    #         self.med_array.remove(medication_to_remove)
    #         print(f"Medication '{medication_name}' removed successfully.")
    #         return True
    #     else:
    #         print(f"Medication '{medication_name}' not found.")
    #         return False
        
    # def update_medication_for_patient(self):
    #     if not patient.med_array:
    #         print("No medications found.")
    #         return

    #     print("Select a medication to update:")
    #     for idx, medication in enumerate(patient.med_array, 1):
    #         print(f"{idx}. {medication}")

    #     choice = int(input("Enter the number of the medication to update: ")) - 1

    #     if 0 <= choice < len(patient.med_array):
    #         selected_medication = patient.med_array[choice]

    #         # Get updated medication details
    #         new_med_type = input(f"Enter new medication type (current: {selected_medication.med_type}): ") or selected_medication.med_type
    #         new_strength = input(f"Enter new medication strength (current: {selected_medication.strength}): ") or selected_medication.strength
    #         new_frequency = input(f"Enter new frequency of intake (current: {selected_medication.frequency}): ") or selected_medication.frequency

    #         # Update medication details
    #         selected_medication.med_type = new_med_type
    #         selected_medication.strength = new_strength
    #         selected_medication.frequency = new_frequency

    #         print("Medication updated successfully.")
    #     else:
    #         print("Invalid selection. Please try again.")
            
        
