import sys

freqs = dict()

def parse_program(filepath):
    with open(filepath, "r") as f:
        program = map(int, f.readline().split(','))
    return program

def air_conditioning(program):

    pos = 0
    while(program[pos] != 99):
        command = program[pos]
        instruction = command % 100
        command = command // 100
        mode1 = command % 10
        command = command // 10
        mode2 = command % 10

        n_instructions = 0
        if(instruction == 1):
            var1 = get_var(program[pos+1], mode1, program)
            var2 = get_var(program[pos+2], mode2, program)
            result = program[pos+3]
            program[result] = var1 + var2
            n_instructions = 4
        elif(instruction == 2):
            var1 = get_var(program[pos+1], mode1, program)
            var2 = get_var(program[pos+2], mode2, program)
            result = program[pos+3]
            program[result] = var1 * var2
            n_instructions = 4
        elif(instruction == 3):
            #input
            program[program[pos+1]] = 5
            n_instructions = 2
        elif(instruction == 4):
            var1 = get_var(program[pos+1], mode1, program)
            n_instructions = 2
            print(var1)
        elif(instruction == 5):
            var1 = get_var(program[pos+1], mode1, program)
            var2 = get_var(program[pos+2], mode2, program)
            if (var1 != 0):
                pos = var2
            else:
                n_instructions = 3
        elif(instruction == 6):
            var1 = get_var(program[pos+1], mode1, program)
            var2 = get_var(program[pos+2], mode2, program)
            if (var1 == 0):
                pos = var2
            else:
                n_instructions = 3
        elif(instruction == 7):
            var1 = get_var(program[pos+1], mode1, program)
            var2 = get_var(program[pos+2], mode2, program)
            result = program[pos+3]
            if(var1 < var2):
                program[result] = 1
            else:
                program[result] = 0
            n_instructions = 4
        elif(instruction == 8):
            var1 = get_var(program[pos+1], mode1, program)
            var2 = get_var(program[pos+2], mode2, program)
            result = program[pos+3]
            if(var1 == var2):
                program[result] = 1
            else:
                program[result] = 0
            n_instructions = 4



        pos += n_instructions
    
    return program[0]

def get_var(var, mode, program):
    if (mode == 0):
        return program[var]
    return var

def int_computer(program):
    #Part 1
    air_conditioning(list(program))

    #Part 2
    


if __name__ == "__main__":
    data = parse_program("input/day5.data")
    int_computer(data)