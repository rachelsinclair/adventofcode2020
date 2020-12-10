import re
import unittest

class BoardingPass:
    
    def __init__(self, value):
        self.value = value
        if(not re.fullmatch('[FB]{7}[LR]{3}$',self.value)):
            raise ValueError("Value not in correct format")

    def get_row(self):
        return get_number_from_binary_string(self.value[:7],"B","F")

    def get_column(self):
        return get_number_from_binary_string(self.value[7:],"R","L")

    def get_seat_id(self):
        return self.get_row() * 8 + self.get_column()

def get_number_from_binary_string(str, ones, zeros):
    """ Takes a string that is an encoded binary number and returns the number in base 10.

    Keyword arguments:
    str -- The string to decode
    ones -- The character representing 1
    zeros -- The character representing 0
    """
    return int(str.replace(ones,"1").replace(zeros,"0"),2)

class TestBoardingPassMethods(unittest.TestCase):

    def test_boarding_pass_constructor(self):
        self.assertEqual(BoardingPass("FBFBBFFRLR").value, "FBFBBFFRLR")
        with self.assertRaises(ValueError):
            BoardingPass("test")

    def test_get_row(self):
        self.assertEqual(BoardingPass("FBFBBFFRLR").get_row(), 44)
        self.assertEqual(BoardingPass("BFFFBBFRRR").get_row(), 70)
        self.assertEqual(BoardingPass("FFFBBBFRRR").get_row(), 14)
        self.assertEqual(BoardingPass("BBFFBBFRLL").get_row(), 102)

    def test_get_column(self):
        self.assertEqual(BoardingPass("FBFBBFFRLR").get_column(), 5)
        self.assertEqual(BoardingPass("BFFFBBFRRR").get_column(), 7)
        self.assertEqual(BoardingPass("FFFBBBFRRR").get_column(), 7)
        self.assertEqual(BoardingPass("BBFFBBFRLL").get_column(), 4)

    def test_get_seat_id(self):
        self.assertEqual(BoardingPass("FBFBBFFRLR").get_seat_id(), 357)
        self.assertEqual(BoardingPass("BFFFBBFRRR").get_seat_id(), 567)
        self.assertEqual(BoardingPass("FFFBBBFRRR").get_seat_id(), 119)
        self.assertEqual(BoardingPass("BBFFBBFRLL").get_seat_id(), 820)

class TestOtherMethods(unittest.TestCase):
    def test_get_number_from_binary_string(self):
        self.assertEqual(get_number_from_binary_string("F","B","F"), 0)
        self.assertEqual(get_number_from_binary_string("B","B","F"), 1)

if __name__ == '__main__':
    unittest.main()