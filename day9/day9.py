import unittest

def is_sum_of_two_elements_in_list(number_list: list, number: int):
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

def is_valid_next_number_in_sequence(sequence: list, preamble_length: int, number_to_test: int):
    return is_sum_of_two_elements_in_list(sequence[-preamble_length:], number_to_test)

def get_first_invalid_number_in_sequence(sequence: list, preamble_length: int):
    sequence_without_preamble = sequence[preamble_length:]
    return next((number for (index, number) in enumerate(sequence_without_preamble) if not is_valid_next_number_in_sequence(sequence[index:index+preamble_length],preamble_length,number)), None)

def get_puzzle_input():
    with open('input.txt') as input_file:
        return [int(line) for line in input_file.read().splitlines()]

def part_1(puzzle_input: list,preamble_length: int):
    puzzle_input = get_puzzle_input()
    xmas_preamble = 25
    return get_first_invalid_number_in_sequence(puzzle_input, xmas_preamble)

def get_contiguous_set_that_sums_to_given_total(number_list: list, total: int):
    for start_index in range(0,len(number_list)):
        for end_index in range(1,len(number_list)+1):
            subset = number_list[start_index:end_index]
            sum_of_subset = sum(subset)
            if sum_of_subset == total:
                return subset
            elif sum_of_subset > total:
                break
    return None

def part_2(puzzle_input: list, target: int):
    list_summing_to_target = get_contiguous_set_that_sums_to_given_total(PUZZLE_INPUT, target)
    return min(list_summing_to_target) + max(list_summing_to_target)

PUZZLE_INPUT = get_puzzle_input()
PREAMBLE_LENGTH = 25

part_1_solution = part_1(PUZZLE_INPUT, PREAMBLE_LENGTH)
print(f"Solution to part 1: {part_1_solution}")
part_2_solution = part_2(PUZZLE_INPUT, part_1_solution)
print(f"Solution to part 2: {part_2_solution}")

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
    
class TestGetContiguousSetThatSumsToGivenTotal(unittest.TestCase):

    def test_return_none_if_no_valid_result(self):
        self.assertEqual(get_contiguous_set_that_sums_to_given_total([1, 2, 3], 10), None)
    
    def test_return_whole_list_if_it_sums_to_total(self):
        self.assertEqual(get_contiguous_set_that_sums_to_given_total([1, 2, 3], 6), [1, 2, 3])

    def test_return_correct_result_for_subset_at_start_of_list(self):
        self.assertEqual(get_contiguous_set_that_sums_to_given_total([1, 2, 3, 4], 3), [1, 2])
    
    def test_return_correct_result_for_subset_in_middle_of_list(self):
        self.assertEqual(get_contiguous_set_that_sums_to_given_total([1, 2, 3, 4], 5), [2, 3])

    def test_return_correct_result_for_subset_at_end_of_list(self):
        self.assertEqual(get_contiguous_set_that_sums_to_given_total([1, 2, 3, 4], 7), [3, 4])

if __name__ == "__main__":
    unittest.main()