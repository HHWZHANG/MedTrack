
import unittest
import unittest.mock
from medication import Medication
from reminder import Reminder
from patient.medication import Medication, Med_db
from unittest.mock import patch
from datetime import datetime, timedelta


class TestPatient(unittest.TestCase):

    def setUp(self):
        self.patient = Patient("John Doe", "Male", "Single", "1990-01-01", "123 Main St", "1234567890", "johndoe@example.com")

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    def test_init(self):
        self.assertEqual(self.patient.name, "John Doe")
        self.assertEqual(self.patient.sex, "Male")
        self.assertEqual(self.patient.marital_status, "Single")
        self.assertEqual(self.patient.dob, "1990-01-01")
        self.assertEqual(self.patient.address, "123 Main St")
        self.assertEqual(self.patient.phoneNumber, "1234567890")
        self.assertEqual(self.patient.email, "johndoe@example.com")

    def test_str(self):
        expected_string = "1-John Doe Male Single 1990-01-01 123 Main St 1234567890 johndoe@example.com"
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
        with patch('medication.Medication.update_medication') as mock_update:
            self.patient.update_medication()
    mock_update.assert_called_once()

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
        self.assertTrue(self.db.is_exist("Amoxicillin"))
        self.assertFalse(self.db.is_exist("Ibuprofen"))

    @patch('builtins.input', side_effect=["Ibuprofen", "Pill", "150mg", "Monthly", False])
    def test_add_medication(self, mock_input):
        self.med_db.add_medication()
        self.assertTrue(self.db.is_exist("Ibuprofen"))

    @patch('builtins.input', side_effect=["Paracetamol"])
    def test_search_medication_CLI(self, mock_input):
        medication = Medication("Paracetamol", "Tablet", "500mg", "Daily", True)
        self.med_db.med_array.append(medication)
        result = self.med_db.search_medication_CLI()
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Paracetamol")


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
