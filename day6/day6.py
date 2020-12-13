import unittest
from functools import reduce

def get_all_groups():
    with open("input.txt") as input_file:
        return [group.strip() for group in input_file.read().split("\n\n")]


def count_questions_to_which_anyone_answered_yes(group):
    return len(set(group.replace("\n","")))

def count_questions_to_which_everybody_answered_yes(group):
    individual_responses = group.split("\n")
    intersection_of_answers = reduce(lambda x,y: set(x).intersection(y), individual_responses)
    return len(intersection_of_answers)

groups = get_all_groups()
sum_of_part_1_group_counts = sum(count_questions_to_which_anyone_answered_yes(group) for group in groups)
sum_of_part_2_group_counts = sum(count_questions_to_which_everybody_answered_yes(group) for group in groups)
print(f"Answer to part 1: {sum_of_part_1_group_counts}")
print(f"Answer to part 2: {sum_of_part_2_group_counts}")

class TestDay6Methods(unittest.TestCase):
    
    def test_count_questions_to_which_anyone_answered_yes(self):
        test_groups = [["abc",3], ["a\nb\nc",3], ["ab\nac",3], ["a\na\na\na",1], ["b",1]]
        for case, result in test_groups:
            with self.subTest(case=case, result=result):
                self.assertEqual(count_questions_to_which_anyone_answered_yes(case),result)
    
    def test_count_questions_to_which_everybody_answered_yes(self):
        test_groups = [["abc",3], ["a\nb\nc",0], ["ab\nac",1], ["a\na\na\na",1], ["b",1]]
        for case, result in test_groups:
            with self.subTest(case=case, result=result):
                self.assertEqual(count_questions_to_which_everybody_answered_yes(case),result)

if __name__ == '__main__':
    unittest.main()
