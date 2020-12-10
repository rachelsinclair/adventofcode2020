#%% part 1
valid_password_count = 0
line_count = 0
with open('input.txt') as input_file:
    for line in input_file:
        line_count += 1
        (pass_policy, password) = line.split(': ')
        (letter_usage_range, letter) = pass_policy.split(' ')
        (min_allowed, max_allowed) = map(int,letter_usage_range.split('-'))
        letter_count = password.count(letter)
        is_valid_password = letter_count in range(min_allowed,max_allowed+1)
        if is_valid_password:
            valid_password_count += 1
        # print(password, letter, letter_count, min_allowed, max_allowed, is_valid_password)
print(line_count, valid_password_count)

# %% part 2
def is_char_at_position(password, letter, pos):
    """
    docstring
    """
    return letter == password[pos]

valid_password_count = 0
line_count = 0
with open('input.txt') as input_file:
    for line in input_file:
        line_count += 1
        (pass_policy, password) = line.split(': ')
        (position_str, letter) = pass_policy.split(' ')
        positions_to_check = map(int,position_str.split('-'))
        valid_positions = sum(is_char_at_position(password, letter, x-1) for x in positions_to_check)
        if valid_positions == 1:
            valid_password_count += 1
print(valid_password_count)
# %%
