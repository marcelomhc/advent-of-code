import sys

def part1(filepath):
    inst = 0
    with open(filepath, 'r') as f:
        lines = f.readlines()
        codes = [-1 for _ in range(16)]
        funcs = [addr, addi, muli, mulr, bani, banr, bori, borr, gtir, gtri, gtrr, eqri, eqir, eqrr, setr, seti]
        for i in range(0,len(lines),4):
            bef = lines[i]
            inp = lines[i+1]
            aft = lines[i+2]
            reg_bef = [int(bef[9]), int(bef[12]), int(bef[15]), int(bef[18])]
            reg_aft = [int(aft[9]), int(aft[12]), int(aft[15]), int(aft[18])]
            inp = [int(k) for k in inp.split(' ')]
            a = int(inp[1])
            b = int(inp[2])
            c = int(inp[3])

            total = 0
            for func in funcs:
                res = int(func(a,b,c,reg_bef) == reg_aft[c])
                if res == 1:
                    select = func
                total += res

#            total = int(addr(a,b,c,reg_bef) == reg_aft[c]) + int(addi(a,b,c,reg_bef) == reg_aft[c]) + int(mulr(a,b,c,reg_bef) == reg_aft[c]) + int(muli(a,b,c,reg_bef) == reg_aft[c]) + int(banr(a,b,c,reg_bef) == reg_aft[c]) + int(bani(a,b,c,reg_bef) == reg_aft[c]) + int(borr(a,b,c,reg_bef) == reg_aft[c]) + int(bori(a,b,c,reg_bef) == reg_aft[c]) + int(setr(a,b,c,reg_bef) == reg_aft[c]) + int(seti(a,b,c,reg_bef) == reg_aft[c]) + int(gtir(a,b,c,reg_bef) == reg_aft[c]) + int(gtri(a,b,c,reg_bef) == reg_aft[c]) + int(gtrr(a,b,c,reg_bef) == reg_aft[c]) + int(eqrr(a,b,c,reg_bef) == reg_aft[c]) + int(eqri(a,b,c,reg_bef) == reg_aft[c]) +int(eqir(a,b,c,reg_bef) == reg_aft[c])
            if (total > 2):
                inst += 1
            elif(total == 1):
                codes[inp[0]] = select
                funcs.remove(select)

    with open('input/day16_2.data', 'r') as f2:
        regs = [0, 0, 0, 0]
        lines = f2.readlines()
        for inp in lines:
            ins = [int(k) for k in inp.split(' ')]
            ex = codes[ins[0]]
            regs[ins[3]] = ex(ins[1], ins[2], ins[3], regs)


    print(inst)
    print(codes)
    print(regs[0])


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




def parse(filepath):
    with open(filepath, 'r') as f:
        f.readlines()

if __name__ == "__main__":
    part1(sys.argv[1])