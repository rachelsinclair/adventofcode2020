import unittest

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


class Passport:

    def __init__(self, value):
        self.value = value.replace("\n"," ")
    
    def has_all_required_fields(self):
        return all(field in self.value for field in required_fields)

with open('input.txt') as input_file:
    passports = [Passport(passport) for passport in input_file.read().split("\n\n")]

count_of_passports_with_required_fields = sum(passport.has_all_required_fields() for passport in passports)
print(f"Valid passport count for part 1: {count_of_passports_with_required_fields}")

class TestPassportMethods(unittest.TestCase):
    def test_passport_constructor(self):
        raw_and_clean_passport_values = (
            (
                "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm",
                "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
            ),
            (
                "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929",
                "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929"
            ),
            (
                "hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm",
                "hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm"
            ),
            (
                "hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in",
                "hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in"
            )
        )
        for (raw_passport, clean_passport) in raw_and_clean_passport_values:
            with self.subTest():
                self.assertEqual(Passport(raw_passport).value, clean_passport)

    def test_has_all_required_fields(self):
        passport_values_and_results = (
            ("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm", True),
            ("iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929", False),
            ("hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm", True),
            ("hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in", False)
        )
        for (value, result) in passport_values_and_results:
            with self.subTest(value=value,result=result):
                self.assertEqual(Passport(value).has_all_required_fields(), result)

if __name__ == '__main__':
    unittest.main()