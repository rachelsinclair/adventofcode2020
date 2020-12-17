def get_instructions():
    with open('input.txt') as input_file:
        instructions = [line.rstrip().split(" ") for line in input_file.readlines()]
    return instructions

def run_instruction(instruction, pointer, accumulator, program_is_running):
    operation = instruction[0]
    argument = int(instruction[1])
    if (operation == 'nop'):
        pass
    elif (operation == 'acc'):
        accumulator = accumulator + argument
    elif (operation == 'jmp'):
        pointer = pointer + argument - 1
    elif (operation == 'xxx'):
        program_is_running = False
    return (pointer, accumulator, program_is_running)

def part_1():
    instructions = get_instructions()
    pointer = 0
    accumulator = 0
    program_is_running = True
    while (program_is_running):
        current_instruction: list = instructions[pointer]
        (pointer, accumulator, program_is_running) = run_instruction(current_instruction, pointer, accumulator, program_is_running)
        current_instruction[0] = 'xxx'
        pointer = pointer + 1
    print(f"loop broken, acc = {accumulator}")

def part_2():
    instructions = get_instructions()
    inst_length = len(instructions)
    print(inst_length)
    for index, instruction in instructions:
        if instruction[0] == "nop" and index + int(instruction[1]) == inst_length:
            print(index, instruction)
            
part_1()
part_2()