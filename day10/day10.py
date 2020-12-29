import unittest
import itertools
import collections

# pairwise traversal of list
# see https://docs.python.org/3/library/itertools.html#itertools-recipes
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def get_puzzle_input():
    with open('input.txt') as input_file:
        return [int(line) for line in input_file.read().splitlines()]

def get_joltage_differences(adapter_joltages):
    if len(adapter_joltages) > 0:
        sorted_adapters = sorted(adapter_joltages+[0, max(adapter_joltages) + 3] )
        joltage_differences = [b-a for a,b in pairwise(sorted_adapters)]
        return joltage_differences

def part_1():
    adapter_list = get_puzzle_input()
    joltage_differences = get_joltage_differences(adapter_list)
    joltage_difference_counts = collections.Counter(joltage_differences)
    one_jolt_differences = joltage_difference_counts[1]
    three_jolt_differences = joltage_difference_counts[3]
    product_of_one_jolt_and_three_jolt_differences = one_jolt_differences * three_jolt_differences
    print(f"Answer to part 1: {product_of_one_jolt_and_three_jolt_differences}")

part_1()

def get_ones_sublist_lengths(input_list):
    return [len(list(group)) for key, group in itertools.groupby(input_list) if key == 1]

def get_distinct_arrangements(adapter_list):
    sublist_lengths_counter = collections.Counter(get_ones_sublist_lengths(get_joltage_differences(adapter_list)))
    permutations = {1: 1, 2: 2, 3: 4, 4: 7}
    distinct_permutations = 1
    for i in range(1,5):
        distinct_permutations *= pow(permutations[i], sublist_lengths_counter[i])
    return distinct_permutations

def part_2():
    adapter_list = get_puzzle_input()
    print(f"Answer to part 2: {get_distinct_arrangements(adapter_list)}")

part_2()

class TestGetJoltageDifferences(unittest.TestCase):

    def test_empty_adapter_list_returns_none(self):
        self.assertEqual(get_joltage_differences([]), None)
    
    def test_single_adapter_with_joltage_1(self):
        self.assertEqual(get_joltage_differences([1]), [1,3])
    
    def test_single_adapter_with_joltage_2(self):
        self.assertEqual(get_joltage_differences([2]), [2,3])

    def test_single_adapter_with_joltage_2(self):
        self.assertEqual(get_joltage_differences([1, 2]), [1,1,3])

class TestGetOnesSublistLengths(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(get_ones_sublist_lengths([1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]),[1, 3, 2, 1])

    def test_example_2(self):
        self.assertEqual(get_ones_sublist_lengths([1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 3, 1, 1, 3, 3, 1, 1, 1, 1, 3, 1, 3, 3, 1, 1, 1, 1, 3]),[4, 4, 3, 2, 4, 1, 4])

class TestGetDistinctArrangements(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(get_distinct_arrangements([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]), 8)

    def test_example_2(self):
        self.assertEqual(get_distinct_arrangements([28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]), 19208)

if __name__ == "__main__":
    unittest.main()

# [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4] => 1:7, 2:0, 3:5