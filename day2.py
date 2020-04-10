import sys

freqs = dict()

def parse_program(filepath):
    with open(filepath, "r") as f:
        program = map(int, f.readline().split(','))
    return program

def gravity_assist(program, noun, verb):
    program[1] = noun
    program[2] = verb

    pos = 0
    while(program[pos] != 99):
        instruction = program[pos]
        var1 = program[pos+1]
        var2 = program[pos+2]
        result = program[pos+3]

        if(instruction == 1):
            program[result] = program[var1] + program[var2]
        elif(instruction == 2):
            program[result] = program[var1] * program[var2]

        pos += 4
    
    return program[0]

def int_computer(program):
    #Part 1
    print(gravity_assist(list(program), 12, 2))

    #Part 2
    for noun in range(0,99):
        for verb in range(0,99):
            value = gravity_assist(list(program), noun, verb)
            if(value == 19690720):
                print(100*noun + verb)
                break


if __name__ == "__main__":
    data = parse_program("input/day2.data")
    int_computer(data)