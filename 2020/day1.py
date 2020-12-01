def parse_program(filepath):
    with open(filepath, "r") as f:
        program = [x for x in map(int, f.read().split('\n'))]
    return program

def find_sum(expenses, total):

    for i in range(len(expenses)):
        for j in range(i, len(expenses)):
            if(expenses[i]+expenses[j] == total):
                print(expenses[i]*expenses[j])

def find_triple_sum(expenses, total):

    expenses.sort()
    
    for i in range(len(expenses)):
        for j in range(i, len(expenses)):
            for k in range(j, len(expenses)):
                if(expenses[i]+expenses[j]+expenses[k] == total):
                    print(expenses[i]*expenses[j]*expenses[k])
                if(expenses[i]+expenses[j]+expenses[k] > total):
                    break

if __name__ == "__main__":
    data = parse_program("input/day1.data")
    find_sum(data, 2020)
    find_triple_sum(data, 2020)