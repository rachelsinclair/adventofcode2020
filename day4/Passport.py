import unittest

class Passport:
    def __init__(self, value):
        cleaned_fields = value.replace("\n"," ")
        field_list = cleaned_fields.strip().split(" ")
        self.fields = [field.split(":") for field in field_list]

    def get_all_field_names(self):
        return [field[0] for field in self.fields]
    
    def get_field_value(self, field_name):
        for field in self.fields:
            if field_name == field[0]:
                return field[1]

class TestPassportMethods(unittest.TestCase):
    
    def test_get_all_field_names(self):
        passport = Passport("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm")
        self.assertEqual(passport.get_all_field_names(), ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'])

    def test_get_field_value(self):
        passport = Passport("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm")
        values = {'ecl': 'gry', 'pid': '860033327', 'eyr': '2020', 'hcl': '#fffffd', 'byr': '1937', 'iyr': '2017', 'cid': '147', 'hgt': '183cm'}
        for key, value in values.items():
            with self.subTest(key=key, value=value):
                self.assertEqual(passport.get_field_value(key),value)

if __name__ == '__main__':
    unittest.main()
