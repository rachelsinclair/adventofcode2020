#%%
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open('input.txt') as input_file:
    passports = [passport.replace("\n"," ") for passport in input_file.read().split("\n\n")]

def is_valid_passport(passport):
    return all(field in passport for field in required_fields)


count_of_valid_passports = sum(is_valid_passport(passport) for passport in passports)
print(count_of_valid_passports)
# %%
