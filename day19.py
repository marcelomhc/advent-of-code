import sys

def part1(filepath):
    with open(filepath, 'r') as f:
        ip = int(f.readline()[4])
        regs = [0,0,0,0,0,0]
        program = list()
        for line in f.readlines():
            inst = line.split(' ')
            func = globals()[inst[0]]
            program.append((func, int(inst[1]), int(inst[2]), int(inst[3])))
        
        while(regs[ip] < len(program)):
            inst = program[regs[ip]]
            res = inst[0](inst[1], inst[2], 0, regs)
            regs[inst[3]] = res
            regs[ip] += 1
            #print(regs)
        print(regs[0])
        print(regs)

def part2(n):
    t=0
    for i in range(1, n+1):
        if n % i == 0:
            t += i
    print(t)

def addr(a,b,c,registers):
    return registers[a] + registers[b]

def addi(a,b,c,registers):
    return registers[a] + b
def mulr(a,b,c,registers):
    return registers[a] * registers[b]

def muli(a,b,c,registers):
    return registers[a] * b
def banr(a,b,c,registers):
    return registers[a] & registers[b]

def bani(a,b,c,registers):
    return registers[a] & b
def borr(a,b,c,registers):
    return registers[a] | registers[b]

def bori(a,b,c,registers):
    return registers[a] | b
def setr(a,b,c,registers):
    return registers[a]

def seti(a,b,c,registers):
    return a

def gtrr(a,b,c,registers):
    return int(registers[a] > registers[b])

def gtri(a,b,c,registers):
    return int(registers[a] > b)

def gtir(a,b,c,registers):
    return int(a > registers[b])

def eqrr(a,b,c,registers):
    return int(registers[a] == registers[b])

def eqri(a,b,c,registers):
    return int(registers[a] == b)

def eqir(a,b,c,registers):
    return int(a == registers[b])

if __name__ == "__main__":
    part1(sys.argv[1])
    part2(10551311)