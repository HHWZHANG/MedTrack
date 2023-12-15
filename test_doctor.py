import unittest
import unittest.mock
from doctor import Doctor
from doctor.report import Report
from doctor.prescription import Prescription, Prescrptn_db
from unittest.mock import patch
from datetime import datetime, timedelta


class TestDoctor(unittest.TestCase):

    def setUp(self):
        self.doctor = Doctor("Dr. House", "123 Street", "house@example.com", "1234567890")

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    def test_init(self):
        self.assertEqual(self.doctor.name, "Dr. House")
        self.assertEqual(self.doctor.address, "123 Street")
        self.assertEqual(self.doctor.email, "house@example.com")
        self.assertEqual(self.doctor.phoneNumber, "1234567890")

    def test_str(self):
        expected_str = "2-Dr. House 123 Street house@example.com 1234567890 "
        self.assertEqual(str(self.doctor), expected_str)

    def test_update_doctor(self):
        with unittest.mock.patch('builtins.input',
                                 side_effect=["Dr. Watson", "456 Avenue", "7890123456", "watson@example.com"]):
            self.doctor.update_doctor("Dr. Watson", "456 Avenue", "7890123456", "watson@example.com")
        self.assertEqual(self.doctor.name, "Dr. Watson")
        self.assertEqual(self.doctor.address, "456 Avenue")
        self.assertEqual(self.doctor.phoneNumber, "7890123456")
        self.assertEqual(self.doctor.email, "watson@example.com")


class TestPrescription(unittest.TestCase):
    def setUp(self):
        self.prescription = Prescription("RX001", "P001", "D001", "Medicine", "50mg", "daily", datetime.now(),
                                         datetime.now() + timedelta(days=10))

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    def test_init(self):
        self.assertEqual(self.prescription.rx_id, "RX001")
        self.assertEqual(self.prescription.patient_id, "P001")
        self.assertEqual(self.prescription.doctor_id, "D001")
        self.assertEqual(self.prescription.med_name, "Medicine")
        self.assertEqual(self.prescription.strength, "50mg")
        self.assertEqual(self.prescription.frequency, "daily")

    def test_str(self):
        expected_str = f"Prescription(patient_id:P001, doctor_id:D001, med_name:Medicine, strength:50mg, frequency:daily, date:{self.prescription.date}, expiry_date:{self.prescription.expiry_date})"
        self.assertEqual(str(self.prescription), expected_str)

    @patch('builtins.input', side_effect=["100mg", "BID", "2023-12-31"])
    def test_update_prescription(self, input):
        self.prescription.update_prescription()
        self.assertEqual(self.prescription.strength, "100mg")
        self.assertEqual(self.prescription.frequency, "BID")
        self.assertEqual(self.prescription.expiry_date, datetime.strptime("2023-12-31", "%Y-%m-%d"))

    def test_expiry_alert(self):
        self.assertEqual(self.prescription.expiry_alert(), False)
        self.prescription.expiry_date = datetime.now() + timedelta(days=7)
        self.assertEqual(self.prescription.expiry_alert(8), True)


class TestPrescrptn_db(unittest.TestCase):

    def setUp(self):
        self.db = Prescrptn_db()
        self.prescription = Prescription("RX001", "P001", "D001", "Medicine", "50mg", "daily", datetime.now(),
                                         datetime.now() + timedelta(days=10))
        self.db.prescrptn_array.append(self.prescription)

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    def tearDown(self):
        return super().tearDown()

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    def test_is_exist(self):
        self.assertTrue(self.db.is_exist("RX001"))
        self.assertFalse(self.db.is_exist("RX002"))

    def test_add_prescription(self):
        with unittest.mock.patch('builtins.input',
                                 side_effect=["RX002", "P002", "D002", "Medicine2", "100mg", "BID", "2023-12-31"]):
            self.db.add_prescription()
        self.assertTrue(self.db.is_exist("RX002"))

    def test_remove_prescription(self):
        self.db.remove_prescription(self.prescription.rx_id)
        self.assertFalse(self.db.is_exist("RX001"))


class TestReport(unittest.TestCase):

    def setUp(self):
        self.report = Report("P001", "Report content")
        self.prescription = Prescription("RX001", "P001", "D001", "Medicine", "50mg", "daily", datetime.now(),
                                         datetime.now() + timedelta(days=10))
        self.pre_db = Prescrptn_db()
        self.pre_db.prescrptn_array.append(self.prescription)

    def tearDown(self):
        self.pre_db.prescrptn_array = []

    def test_init(self):
        self.assertEqual(self.report.patient_id, "P001")
        self.assertEqual(self.report.report_text, "Report content")

    def test_str(self):
        expected_str = f"Medical Report for Patient ID {self.report.patient_id} (Timestamp: {self.report.timestamp}): {self.report.report_text}"
        self.assertEqual(str(self.report), expected_str)

    def test_generate_report(self):
        self.report.generate_report(self.pre_db)
        expected_report_content = f"Prescription History for Patient ID {self.report.patient_id}:\n"
        expected_report_content += "---------------------------------------------------------\n"
        expected_report_content += f"Prescription ID: {self.prescription.rx_id}\n"
        expected_report_content += f"Medication Name: {self.prescription.med_name}\n"
        expected_report_content += f"Strength: {self.prescription.strength}\n"
        expected_report_content += f"Frequency: {self.prescription.frequency}\n"
        expected_report_content += f"Date: {self.prescription.date}\n"
        expected_report_content += f"Expiry Date: {self.prescription.expiry_date}\n"
        expected_report_content += "---------------------------------------------------------\n"
        self.assertEqual(self.report.report_text, expected_report_content)

    def test_check_drug_interactions(self):
        prescription2 = Prescription("RX002", "P001", "D001", "Aspirin", "100mg", "BID", datetime.now(),
                                     datetime.now() + timedelta(days=10))
        prescription3 = Prescription("RX003", "P001", "D001", "Ibuprofen", "200mg", "TID", datetime.now(),
                                     datetime.now() + timedelta(days=10))
        self.pre_db.prescrptn_array.append(prescription2)
        self.pre_db.prescrptn_array.append(prescription3)
        interactions = self.report.check_drug_interactions(self.pre_db)
        self.assertEqual(len(interactions), 1)
        self.assertEqual(interactions[0][0], ("Aspirin", "Ibuprofen"))
        self.assertEqual(interactions[0][1], "Increased risk of gastrointestinal bleeding")

    def test_search_medication_history(self):
        medication_records = self.report.search_medication_history("Medicine", self.pre_db)
        self.assertEqual(len(medication_records), 1)
        self.assertEqual(medication_records[0]['Prescription_ID'], "RX001")
        self.assertEqual(medication_records[0]['Medication_Name'], "Medicine")
        self.assertEqual(medication_records[0]['Strength'], "50mg")
        self.assertEqual(medication_records[0]['Frequency'], "daily")


if __name__ == '__main__':
    unittest.main()



