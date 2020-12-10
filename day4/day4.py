#%%
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

with open('input.txt') as input_file:
    passports = [passport.replace("\n"," ") for passport in input_file.read().split("\n\n")]

count_of_valid_passports = sum(all(field in passport for field in required_fields) for passport in passports)
print(count_of_valid_passports)
# %%
