import unittest
import KL_Healthcare
import datetime

class TestApp(unittest.TestCase):
    
    def test_year(self):
        result = KL_Healthcare.year
        today = datetime.date.today()
        self.assertGreaterEqual(result, today.year)

    def test_month(self):
        result = KL_Healthcare.month
        today = datetime.date.today()
        self.assertGreaterEqual(result, today.month)
    
    def test_day(self):
        result = KL_Healthcare.day
        today = datetime.date.today()
        self.assertGreaterEqual(result, today.day)

    def test_data(self):
        result = KL_Healthcare.rows
        self.assertIs(type(result), int)

    def test_dataStructure(self):
        result = KL_Healthcare.data_array
        self.assertEqual(type(result), list)


if __name__ == '__main__':
    unittest.main()