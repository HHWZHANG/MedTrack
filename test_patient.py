
import unittest
import unittest.mock
from unittest.mock import Mock
from unittest import mock
from unittest.mock import patch

from patient.reminder import Reminder
from patient import Patient
from patient import reminder
from patient.medication import Medication, Med_db

from datetime import datetime, timedelta


class TestPatient(unittest.TestCase):

    def setUp(self):
        self.patient = Patient("John Doe", "Male", "Single", "1990-01-01", "123 Main St", "1234567890", "johndoe@example.com")
        self.patient = Patient("John Doe", "Male", "Single", "1990-01-01", "123 Main St", "1234567890",
                               "johndoe@example.com")
        self.medication_1 = Medication("Paracetamol", "Tablet", "500mg", "Daily", False)
        self.medication_2 = Medication("Aspirin", "Pill", "100mg", "Twice a day", True)
        self.reminder_1 = Reminder(self.medication_1, "08:00", 2, datetime.now(), datetime.now() + timedelta(days=10))

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    def test_patient_init(self):
        patient = Patient("Alice", "Female", "Married", "1980-05-15", "456 Oak St", "9876543210", "alice@example.com")
        self.assertEqual(patient.name, "Alice")
        # Check other attributes here...

    def test_init(self):
        self.assertEqual(self.patient.name, "John Doe")
        self.assertEqual(self.patient.sex, "Male")
        self.assertEqual(self.patient.marital_status, "Single")
        self.assertEqual(self.patient.dob, "1990-01-01")
        self.assertEqual(self.patient.address, "123 Main St")
        self.assertEqual(self.patient.phoneNumber, "1234567890")
        self.assertEqual(self.patient.email, "johndoe@example.com")

    class TestPatientInit(unittest.TestCase):
        def test_patient_init(self):
            patient = Patient("Alice", "Female", "Married", "1980-05-15", "456 Oak St", "9876543210",
                              "alice@example.com")
            self.assertEqual(patient.name, "Alice")
            self.assertEqual(patient.sex, "Female")
    def test_str(self):
        expected_string = "26-John Doe Male Single 1990-01-01 123 Main St 1234567890 johndoe@example.com"
        self.assertEqual(str(self.patient), expected_string)

    @patch('builtins.input', side_effect=["Jane Doe", "Female", "Married", "1985-02-02", "456 Elm St", "0987654321", "janedoe@example.com"])
    def test_update_patient(self, mock_inputs):
        self.patient.update_patient()
        self.assertEqual(self.patient.name, "Jane Doe")
        self.assertEqual(self.patient.sex, "Female")
        self.assertEqual(self.patient.marital_status, "Married")
        self.assertEqual(self.patient.dob, "1985-02-02")
        self.assertEqual(self.patient.address, "456 Elm St")
        self.assertEqual(self.patient.phoneNumber, "0987654321")
        self.assertEqual(self.patient.email, "janedoe@example.com")

    def test_add_medication(self):
        medication = Medication("Paracetamol", "Tablet", "500mg", "Daily", False)
        self.patient.add_medication(medication)
        self.assertIn(medication, self.patient.med_array)

    def test_remove_medication(self):
        medication = Medication("Paracetamol", "Tablet", "500mg", "Daily", False)
        self.patient.add_medication(medication)
        with patch('patient.Patient.select_medication', return_value=medication):
            self.patient.remove_medication()
        self.assertNotIn(medication, self.patient.med_array)

    def test_update_medication(self):
        medication = Medication("Paracetamol", "Tablet", "500mg", "Daily", False)
        self.patient.add_medication(medication)
        with patch('patient.Patient.select_medication', return_value=medication):
            with patch('patient.medication.Medication.update_medication') as mock_update:
                self.patient.update_medication()
        mock_update.assert_called_once()

    def test_is_medication_exist_in_reminder(self):
        # Ensure empty reminder list returns False
        self.assertFalse(self.patient.is_medication_exist_in_reminder(self.medication_1))

        # Add a reminder and check if the medication exists in reminders
        self.patient.reminders.append(self.reminder_1)
        self.assertTrue(self.patient.is_medication_exist_in_reminder(self.medication_1))

        # Ensure another medication doesn't exist in reminders
        self.assertFalse(self.patient.is_medication_exist_in_reminder(self.medication_2))

    def test_show_reminders(self):
        # Create a Patient instance
        patient = Patient("John Doe", "Male", "Single", "1990-01-01", "123 Main St", "1234567890",
                          "johndoe@example.com")

        # Create mock reminders
        mock_reminder_1 = Mock(spec=Reminder)
        mock_reminder_2 = Mock(spec=Reminder)

        # Mock the show_reminder method for reminders
        mock_reminder_1.show_reminder.return_value = "Reminder 1 info"
        mock_reminder_2.show_reminder.return_value = "Reminder 2 info"

        # Add mock reminders to the patient
        patient.reminders = [mock_reminder_1, mock_reminder_2]

        # Test show_reminders method
        with patch('builtins.print') as mock_print:
            patient.show_reminders()

            # Check if the mock reminder info was printed
            expected_calls = [mock.call("-" * 10, "Today's Reminder", "-" * 10, sep=""),
                              mock.call("-" * (20 + len("Today's Reminder")), sep="")]
            mock_print.assert_has_calls(expected_calls)

    def test_show_medication_with_index_empty(self):
        # Create an empty Patient instance
        patient = Patient("John Doe", "Male", "Single", "1990-01-01", "123 Main St", "1234567890",
                          "johndoe@example.com")

        # Mock print function to capture output
        with unittest.mock.patch('builtins.print') as mock_print:
            result = patient.show_medication_with_index()

            # Check if the function prints "No medications found"
            mock_print.assert_called_once_with("No medications found")
            self.assertFalse(result)

    def test_show_medication_with_index_non_empty(self):
        # Create a Patient instance with medications
        patient = Patient("John Doe", "Male", "Single", "1990-01-01", "123 Main St", "1234567890",
                          "johndoe@example.com")
        medication1 = Medication("Paracetamol", "Tablet", "500mg", "Daily", False)
        medication2 = Medication("Aspirin", "Pill", "100mg", "Twice a day", True)
        patient.med_array = [medication1, medication2]

        # Mock print function to capture output
        with unittest.mock.patch('builtins.print') as mock_print:
            result = patient.show_medication_with_index()

            # Check if the function prints the medications with index
            expected_calls = [unittest.mock.call('1. Paracetamol (Tablet, 500mg, Daily)'),
                              unittest.mock.call('2. Aspirin (Pill, 100mg, Twice a day)')]
            mock_print.assert_has_calls(expected_calls)
            self.assertTrue(result)
    @patch('builtins.input', side_effect=["10:00", 1, "2023-01-01", "2023-01-10"])
    def test_add_reminder(self, mock_inputs):
        medication = Medication("Paracetamol", "Tablet", "500mg", "Once a day", False)
        self.patient.add_medication(medication)
        with patch('patient.Patient.select_medication', return_value=medication):
            self.patient.add_reminder()
        self.assertEqual(len(self.patient.reminders), 1)

    @patch('builtins.input', return_value=1)
    def test_delete_reminder(self, mock_input):
        self.patient.delete_reminder()
        self.assertEqual(len(self.patient.reminders), 0)


class TestMedication(unittest.TestCase):

    def setUp(self):
        self.medication = Medication("Aspirin", "Pill", "100mg", "Twice a day", True)

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    @patch('builtins.input', return_value='2')  # Simulate user input
    def test_select_medication_valid_input(self, mock_input):
        # Create a Patient instance with medications
        patient = Patient("John Doe", "Male", "Single", "1990-01-01", "123 Main St", "1234567890",
                          "johndoe@example.com")
        medication1 = Medication("Paracetamol", "Tablet", "500mg", "Daily", False)
        medication2 = Medication("Aspirin", "Pill", "100mg", "Twice a day", True)
        patient.med_array = [medication1, medication2]

        selected_medication = patient.select_medication()

        # Check if the correct medication was selected
        self.assertEqual(selected_medication, medication2)

    @patch('builtins.input', return_value='invalid')  # Simulate invalid user input
    def test_select_medication_invalid_input(self, mock_input):
        # Create a Patient instance with medications
        patient = Patient("John Doe", "Male", "Single", "1990-01-01", "123 Main St", "1234567890",
                          "johndoe@example.com")
        medication1 = Medication("Paracetamol", "Tablet", "500mg", "Daily", False)
        patient.med_array = [medication1]

        selected_medication = patient.select_medication()

        # Check if the method returns None for invalid input
        self.assertIsNone(selected_medication)
    def test_medication_init(self):
        self.assertEqual(self.medication.name, "Aspirin")
        self.assertEqual(self.medication.med_type, "Pill")
        self.assertEqual(self.medication.strength, "100mg")
        self.assertEqual(self.medication.frequency, "Twice a day")

    def test_medication_str(self):
        expected_string = "Aspirin (Pill, 100mg, Twice a day)"
        self.assertEqual(str(self.medication), expected_string)

    @patch('builtins.input', side_effect=["Liquid", "200mg", "Daily"])
    def test_update_medication(self, input):
        self.medication.update_medication()
        self.assertEqual(self.medication.med_type, "Liquid")
        self.assertEqual(self.medication.strength, "200mg")
        self.assertEqual(self.medication.frequency, "Daily")


class TestMed_db(unittest.TestCase):

    def setUp(self):
        self.med_db = Med_db()
        self.medication = Medication("Amoxicillin", "Capsule", "500mg", "Daily", True)
        self.med_db.med_array.append(self.medication)

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    def test_is_exist(self):
        self.assertTrue(self.med_db.is_exist("Amoxicillin"))
        self.assertFalse(self.med_db.is_exist("Ibuprofen"))

    @patch('builtins.input', side_effect=["Ibuprofen", "Pill", "150mg", "Monthly", 'n'])
    def test_add_medication(self, mock_input):
        self.med_db.add_medication()
        self.assertTrue(self.med_db.is_exist("Ibuprofen"))

    @patch('builtins.input', side_effect=["Paracetamol"])
    def test_search_medication_CLI(self, mock_input):
        medication = Medication("Paracetamol", "Tablet", "500mg", "Daily", True)
        self.med_db.med_array.append(medication)
        result = self.med_db.search_medication_CLI()
        self.assertIsNotNone(result)
        self.assertEqual(result[-1].name, "Paracetamol")


class TestReminder(unittest.TestCase):

    def setUp(self):
        self.medication = Medication("Paracetamol", "Tablet", "500mg", "Daily", False)
        self.start_date = datetime.now()
        self.end_date = self.start_date + timedelta(days=10)
        self.reminder = Reminder(self.medication, "08:00", 2, self.start_date, self.end_date)

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    def test_init(self):
        self.assertEqual(self.reminder.medication, self.medication)
        self.assertEqual(self.reminder.time, "08:00")
        self.assertEqual(self.reminder.repeat, 2)
        self.assertEqual(self.reminder.start_date, self.start_date)
        self.assertEqual(self.reminder.end_date, self.end_date)
        self.assertFalse(self.reminder.taken)

    def test_str(self):
        self.assertEqual(str(self.reminder), f"Reminder for {self.medication.name} at 08:00. Status: Not taken yet")

    @patch('reminder.datetime')
    def test_show_reminder(self, mock_datetime):
        mock_datetime.now.return_value = self.start_date
        mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw)
        self.assertTrue(self.reminder.show_reminder())

    def test_taken_reminder(self):
        self.reminder.taken_reminder()
        self.assertTrue(self.reminder.taken)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestPatient))
    suite.addTest(unittest.makeSuite(TestMedication))
    suite.addTest(unittest.makeSuite(TestMed_db))
    suite.addTest(unittest.makeSuite(TestReminder))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
