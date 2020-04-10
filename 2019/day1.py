import sys

freqs = dict()

def module_fuel(filepath):
    fuel = 0
    with open(filepath, "r") as f:
        for line in f:
            module_fuel = (int(line)/3) - 2
            fuel += total_fuel(module_fuel)
        print("Total fuel = " + str(fuel))
    return fuel

def total_fuel(fuel):
    additional_fuel = fuel/3 - 2
    while (additional_fuel > 0):
        fuel += additional_fuel
        additional_fuel = additional_fuel/3 - 2
    return fuel

if __name__ == "__main__":
    fuel = module_fuel(sys.argv[1])