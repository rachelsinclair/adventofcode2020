import re
import unittest

class BoardingPass:
    
    def __init__(self, value):
        self.value = value
        if(not re.fullmatch('[FB]{7}[LR]{3}$',self.value)):
            raise ValueError("Value not in correct format")

    def get_row(self):
        row_indicator = self.value[:7].replace("F","0").replace("B","1")
        row_number = int(row_indicator,2)
        return row_number

    def get_column(self):
        column_indicator = self.value[7:].replace("L","0").replace("R","1")
        column_number = int(column_indicator,2)
        return column_number

    def get_seat_id(self):
        return self.get_row() * 8 + self.get_column()

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

if __name__ == '__main__':
    unittest.main()