import Passport
import PassportValidator

def get_all_passports():
    with open('input.txt') as input_file:
        return [Passport.Passport(passport) for passport in input_file.read().split("\n\n")]

passports = get_all_passports()
validator = PassportValidator.PassportValidator()

pass_dicts = []
for passport in passports:
    pass_dicts.append(dict(passport.fields))

count_of_passports_with_required_fields = sum(validator.has_all_required_fields(passport.get_all_field_names()) for passport in passports)
print(f"Valid passport count for part 1: {count_of_passports_with_required_fields}")
count_of_valid_passports = sum(validator.is_valid_passport(pass_dict) for pass_dict in pass_dicts)
print(f"Valid passport count for part 2: {count_of_valid_passports}")