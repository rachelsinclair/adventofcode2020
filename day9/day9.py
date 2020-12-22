import unittest

def is_sum_of_two_elements_in_list(number_list, number):
    # oh look, some code lifted from day 1!
    sorted_list = sorted(number_list)
    left_pointer,right_pointer = [0,len(sorted_list)-1]
    while left_pointer < right_pointer:
        sum_of_pair = sorted_list[left_pointer] + sorted_list[right_pointer]
        if sum_of_pair == number:
            #print(f"{number}")
            return True
        elif sum_of_pair < number:
            left_pointer += 1
        elif sum_of_pair > number:
            right_pointer -= 1
    return False

def is_valid_next_number_in_sequence(sequence, preamble_length, number_to_test):
    return is_sum_of_two_elements_in_list(sequence[-preamble_length:], number_to_test)

def get_first_invalid_number_in_sequence(sequence, preamble_length):
    sequence_without_preamble = sequence[preamble_length:]
    return next((number for (index, number) in enumerate(sequence_without_preamble) if not is_valid_next_number_in_sequence(sequence[index:index+preamble_length],preamble_length,number)), None)

def part_1():
    with open('input.txt') as input_file:
        puzzle_input = [int(line) for line in input_file.read().splitlines()]

    xmas_preamble = 25
    answer = get_first_invalid_number_in_sequence(puzzle_input, xmas_preamble)
    print(f"Solution to part 1: {answer}")

part_1()

class TestIsSumOfTwoElementsInListMethod(unittest.TestCase):

    def test_number_that_is_sum_of_two_elements_is_valid(self):
        self.assertTrue(is_sum_of_two_elements_in_list([35, 20, 15, 25, 47], 40))
    
    def test_number_that_is_not_sum_of_two_elements_is_invalid(self):
        self.assertFalse(is_sum_of_two_elements_in_list([35, 20, 15, 25, 47], 36))

class TestIsValidNextNumberInSequence(unittest.TestCase):

    def test_sequence_with_length_equal_to_preamble_and_valid_number(self):
        self.assertTrue(is_valid_next_number_in_sequence([1,2,3,4,5], 5, 6))

    def test_sequence_with_length_equal_to_preamble_and_invalid_number(self):
        self.assertFalse(is_valid_next_number_in_sequence([1,2,3,4,5], 5, 10))
    
    def test_sequence_longer_than_preamble_with_invalid_number(self):
        self.assertFalse(is_valid_next_number_in_sequence([1,2,3,4,5], 3, 3))

class TestGetFirstInvalidNumberInSequence(unittest.TestCase):

    def test_when_invalid_number_exists_in_sequence_it_is_returned(self):
        self.assertEqual(get_first_invalid_number_in_sequence([35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576], 5), 127)

    def test_when_all_numbers_in_sequence_are_valid_none_is_returned(self):
        self.assertEqual(get_first_invalid_number_in_sequence([35, 20, 15, 25, 47, 40, 62, 55, 65], 5), None)

if __name__ == "__main__":
    unittest.main()