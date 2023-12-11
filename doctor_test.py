import unittest
import unittest.mock
from doctor import Doctor
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
        expected_str = "Doctor(id:2, name:'Dr. House', address:'123 Street', email:'house@example.com', phoneNumber:'1234567890')"
        self.assertEqual(str(self.doctor), expected_str)

    def test_update_doctor(self):
        with unittest.mock.patch('builtins.input', side_effect=["Dr. Watson", "456 Avenue", "7890123456", "watson@example.com"]):
            self.doctor.update_doctor()
        self.assertEqual(self.doctor.name, "Dr. Watson")
        self.assertEqual(self.doctor.address, "456 Avenue")
        self.assertEqual(self.doctor.phoneNumber, "7890123456")
        self.assertEqual(self.doctor.email, "watson@example.com")





class TestPrescription(unittest.TestCase):
    def setUp(self):
        self.prescription = Prescription("RX001", "P001", "D001", "Medicine", "50mg", "daily", datetime.now(), datetime.now() + timedelta(days=10))

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

class TestPrescrptn_db(unittest.TestCase):

    def setUp(self):
        self.db = Prescrptn_db()
        self.prescription = Prescription("RX001", "P001", "D001", "Medicine", "50mg", "daily", datetime.now(), datetime.now() + timedelta(days=10))
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

    @patch('builtins.input', side_effect=["RX002", "P002", "D002", "Medicine2", "100mg", "BID", "2023-12-31"])
    def test_add_prescription(self, input):
        self.db.add_prescription()
        self.assertTrue(self.db.is_exist("RX002"))

    def test_remove_prescription(self):
        self.db.remove_prescription(self.prescription)
        self.assertFalse(self.db.is_exist("RX001"))


if __name__ == '__main__':
    unittest.main()