import unittest
import re

class PassportValidator:
    def __init__(self):
        self.field_validators = {
            "iyr": self.is_valid_iyr,
            "byr": self.is_valid_byr,
            "eyr": self.is_valid_eyr,
            "hgt": self.is_valid_hgt,
            "hcl": self.is_valid_hcl,
            "ecl": self.is_valid_ecl,
            "pid": self.is_valid_pid
        }
    
    def is_valid_passport(self, input: dict):
        if not self.has_all_required_fields(input):
            return False
        for key in self.field_validators.keys():
            if (not self.field_validators.get(key)(input.get(key))):
                return False
        return True

    def has_all_required_fields(self, fields: list) -> bool:
        return all(key in fields for key in self.field_validators.keys())

    def is_valid_byr(self, value) -> bool:
        return bool(re.fullmatch('19[2-9][0-9]|200[0-2]',value))

    def is_valid_iyr(self, value) -> bool:
        return bool(re.fullmatch('20(1[0-9]|20)',value))

    def is_valid_eyr(self, value) -> bool:
        return bool(re.fullmatch('20(2[0-9]|30)',value))

    def is_valid_hgt(self, value) -> bool:
        cm_validator = '1([5-8][0-9]|9[0-3])cm'
        in_validator = '(59|6[0-9]|7[0-6])in'
        height_validator = cm_validator+'|'+in_validator
        return bool(re.fullmatch(height_validator,value))

    def is_valid_hcl(self, value) -> bool:
        return bool(re.fullmatch('#[0-9a-f]{6}',value))

    def is_valid_ecl(self, value) -> bool:
        return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def is_valid_pid(self, value) -> bool:
        return bool(re.fullmatch("\d{9}", value))

class TestPassportValidatorMethods(unittest.TestCase):

    def setUp(self):
        self.passport_validator = PassportValidator()

    def test_is_valid_passport(self):
        self.assertFalse(self.passport_validator.is_valid_passport({"eyr":"1972", "cid":"100", "hcl":"#18171d", "ecl":"amb", "hgt":"170", "pid":"186cm", "iyr":"2018", "byr":"1926"}))
        self.assertTrue(self.passport_validator.is_valid_passport({"pid":"087499704", "hgt":"74in", "ecl":"grn", "iyr":"2012", "eyr":"2030", "byr":"1980", "hcl":"#623a2f"}))

    def test_has_all_required_fields(self):
        self.assertTrue(self.passport_validator.has_all_required_fields(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]))
        self.assertFalse(self.passport_validator.has_all_required_fields(["byr", "eyr", "hgt", "hcl", "ecl", "pid"]))
        self.assertTrue(self.passport_validator.has_all_required_fields(["cid", "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]))
    
    def test_is_valid_byr(self):
        for year in range(1920, 2003):
            with self.subTest(year=year):
                self.assertTrue(self.passport_validator.is_valid_byr(str(year)))
        self.assertFalse(self.passport_validator.is_valid_byr('1919'))
        self.assertFalse(self.passport_validator.is_valid_byr('2003'))

    def test_is_valid_iyr(self):
        for year in range(2010, 2021):
            with self.subTest(year=year):
                self.assertTrue(self.passport_validator.is_valid_iyr(str(year)))
        self.assertFalse(self.passport_validator.is_valid_iyr('2009'))
        self.assertFalse(self.passport_validator.is_valid_iyr('2021'))

    def test_is_valid_eyr(self):
        for year in range(2020, 2031):
            with self.subTest(year=year):
                self.assertTrue(self.passport_validator.is_valid_eyr(str(year)))
        self.assertFalse(self.passport_validator.is_valid_eyr('2019'))
        self.assertFalse(self.passport_validator.is_valid_eyr('2031'))
    
    def test_is_valid_hgt(self):
        valid_heights = ["150cm", "193cm", "59in", "76in"]
        for height in valid_heights:
            with self.subTest(height=height):
                self.assertTrue(self.passport_validator.is_valid_hgt(height))
        invalid_heights = ["149cm", "194cm", "58in", "77in"]
        for height in invalid_heights:
            with self.subTest(height=height):
                self.assertFalse(self.passport_validator.is_valid_hgt(height))

    def test_is_valid_hcl(self):
        self.assertTrue(self.passport_validator.is_valid_hcl("#123abc"))
        self.assertFalse(self.passport_validator.is_valid_hcl("#123abz"))
        self.assertFalse(self.passport_validator.is_valid_hcl("123abz"))

    def test_is_valid_ecl(self):
        for eye_colour in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            with self.subTest(eye_colour = eye_colour):
                self.assertTrue(self.passport_validator.is_valid_ecl(eye_colour))
            self.assertFalse(self.passport_validator.is_valid_ecl("wat"))
    
    def test_is_valid_pid(self):
        self.assertTrue(self.passport_validator.is_valid_pid("000000001"))
        self.assertFalse(self.passport_validator.is_valid_pid("0123456789"))

if __name__ == '__main__':
    unittest.main()