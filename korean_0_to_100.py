from korean_number import korean_number
import unittest

class TestkoreanNumber(unittest.TestCase):
    def test_0(self):
        self.assertEqual(korean_number(0),'영')
    def test_1(self):
        self.assertEqual(korean_number(1),'일')
    def test_27(self):
        self.assertEqual(korean_number(27),'이십칠')
    def test_40(self):
        self.assertEqual(korean_number(40),'사십')
    def test_15(self):
        self.assertEqual(korean_number(15),'십오')
if __name__ == '__main__':
    print(unittest.main())
