import unittest

def is_valid_next_number_in_sequence(sequence, number):
    return min(sequence) <= number <= max(sequence) * 2

class TestIsNextValidNumberInSequenceMethod(unittest.TestCase):

    def test_number_that_is_sum_of_two_elements_is_valid(self):
        self.assertTrue(is_valid_next_number_in_sequence([35, 20, 15, 25, 47], 40))
    
    def test_number_less_than_minimum_value_is_invalid(self):
        self.assertFalse(is_valid_next_number_in_sequence([35, 20, 15, 25, 47], 10))
    
    def test_number_greater_than_double_of_maximum_value_is_invalid(self):
        self.assertFalse(is_valid_next_number_in_sequence([35, 20, 15, 25, 47], 95))
    
    def test_number_that_is_not_sum_of_two_elements_is_invalid(self):
        self.assertFalse(is_valid_next_number_in_sequence([35, 20, 15, 25, 47], 36))

if __name__ == "__main__":
    unittest.main()