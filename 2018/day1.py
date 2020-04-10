import sys

freqs = dict()

def UpdateFrequency(frequency, filepath):
    with open(filepath, "r") as f:
        for line in f:
            frequency = frequency + int(line)
            if(freqs.get(frequency)):
                print("Repeated frequency = " + str(frequency))
                return
            freqs[frequency] = True

        print("Final frequency = " + str(frequency))

    UpdateFrequency(frequency, filepath)

if __name__ == "__main__":
    freqs[0] = True
    UpdateFrequency(0, sys.argv[1])