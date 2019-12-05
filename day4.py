import sys

def criteria1(number):
    digits = str(number)
    for i in range(len(digits)-1):
        if(digits[i] == digits[i+1]):
            return True
    return False

def criteria1b(number):
    digits = str(number)
    matching = 1
    for i in range(len(digits)-1):
        if(digits[i] == digits[i+1]):
            matching += 1
        elif(matching == 2):
            return True
        else:
            matching = 1
    if(matching == 2):
        return True
    return False

def criteria2(number):
    digits = str(number)
    for i in range(len(digits)-1):
        if(int(digits[i]) > int(digits[i+1])):
            return False
    return True

if __name__ == "__main__":
    total = total2 = 0
    for i in range (240920, 789857+1):
        if (criteria1(i) and criteria2(i)):
            total += 1
        if (criteria1b(i) and criteria2(i)):
            total2 += 1

    print(total)
    print(total2)