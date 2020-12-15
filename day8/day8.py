with open('input.txt') as input_file:
    instructions = [line.rstrip().split(" ") for line in input_file.readlines()]

print(instructions[:5])

pointer = 0
accumulator = 0
program_is_running = True

def run_instruction():
    global pointer, instructions, accumulator, program_is_running
    current_instruction = instructions[pointer]
    operation = current_instruction[0]
    current_instruction[0] = "xxx"
    argument = int(current_instruction[1])
    print(f"Running line {pointer}: {operation} {argument}")
    if (operation == 'nop'):
        pass
    elif (operation == 'acc'):
        accumulator = accumulator + argument
    elif (operation == 'jmp'):
        pointer = pointer + argument - 1
    elif (operation == 'xxx'):
        program_is_running = False
    

while (program_is_running):
    run_instruction()
    pointer = pointer + 1
print(f"loop broken, acc = {accumulator}")