import copy

class InfiniteLoopException(BaseException):
    pass

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
        raise InfiniteLoopException()
    return (pointer, accumulator, program_is_running)

def run_program(instruction_list):
    instructions = copy.deepcopy(instruction_list)
    pointer = 0
    accumulator = 0
    program_is_running = True
    executed_instructions = []
    while (program_is_running):
        try:
            current_instruction = instructions[pointer]
            executed_instructions.append((pointer, current_instruction.copy()))
            (pointer, accumulator, program_is_running) = run_instruction(current_instruction, pointer, accumulator, program_is_running)
            current_instruction[0] = 'xxx'
            pointer = pointer + 1
        except IndexError as error:
            raise IndexError(f"Escaped boot code, acc value: {accumulator}")
        except InfiniteLoopException as error:
            print(f"Infinite boot loop, acc value: {accumulator}")
            break
    return executed_instructions


def part_1():
    instructions = get_instructions()
    try:
        run_program(instructions)
    except InfiniteLoopException as error:
        pass

def part_2():
    instructions = get_instructions()
    relevant_instructions = run_program(instructions)
    for index, [operator, argument] in relevant_instructions:
        if operator == "jmp":
            modified_instructions = copy.deepcopy(instructions)
            modified_instructions[index][0] = "nop"
            try:
                run_program(modified_instructions)
            except IndexError as error:
                print(error)
                break
            except InfiniteLoopException as error:
                pass
        elif operator == "nop":
            modified_instructions = copy.deepcopy(instructions)
            modified_instructions[index][0] = "jmp"
            try:
                run_program(modified_instructions)
            except IndexError as error:
                print(error)
                break
            except InfiniteLoopException as error:
                pass

part_1()
part_2()