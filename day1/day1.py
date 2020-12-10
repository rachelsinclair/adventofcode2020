import unittest

#%% part 1
goal = 2020
num_list = []
with open('input.txt') as input_file:
    for line in input_file:
        num_list.append(int(line))

filtered_values = [value for value in num_list if value <= goal - min(num_list)]

for value in filtered_values:
    complement = goal - value
    try:
        filtered_values.index(complement)
        print(value * complement)
        break
    except ValueError:
        pass
# %%
sum(sorted(filtered_values)[0:2])
# %%
sorted_list = sorted(num_list)
i,j = [0,len(sorted_list)-1]
while i < j:
    val1 = sorted_list[i]
    val2 = sorted_list[j]
    total = val1 + val2
    if total == goal:
        print(f"Goal hit! Values are {val1} and {val2}, product is {val1 * val2}")
        break
    elif total < goal:
        print("Total too low, increasing left pointer")
        i += 1
    elif total > goal:
        print("Total too high, decreasing right pointer")
        j -= 1
# %%
max_idx = len(sorted_list)-1
i = 0
triple_found = False
while (not triple_found):
    val1 = sorted_list[i]
    j = i + 1
    k = max_idx
    while j < k:
        val2 = sorted_list[j]
        val3 = sorted_list[k]
        total = val1 + val2 + val3
        if total > goal:
            k -= 1
        elif total < goal:
            j += 1
        else:
            print(f"Goal hit! Values are {val1}, {val2} and {val3}, product is {val1 * val2 * val3}")
            triple_found = True
            break
    i += 1
# %%

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()