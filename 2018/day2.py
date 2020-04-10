import sys

def CalculateFileCheckSum(filepath):
    twos = 0
    threes = 0
    with open(filepath, "r") as f:
        for line in f:
            two, three = CalculateCheckSum(line)
            twos = twos + two
            threes = threes + three
    
    print("Twos: " + str(twos))
    print("Threes: " + str(threes))
    print("Checksum: " + str(twos*threes))

def CalculateCheckSum(word):
    letters = dict()
    two = 0
    three = 0
    for letter in word:
        count = letters.setdefault(letter, 0)
        letters[letter] = count + 1
        if (count == 1):
            two = two + 1
        if (count == 2):
            three = three + 1
            two = two - 1

    return int(two > 0), int(three > 0)

def FindWords(filepath):
    words = []
    with open(filepath, "r") as f:
        for line in f:
            words.append(line)
    for i in range(0, len(words)):
        wordi = words[i]
        for j in range(i+1, len(words)):
            wordj = words[j]
            diff = 0
            for k in range(0, len(wordj)):
                if(wordi[k] != wordj[k]):
                    diff += 1
                    pos = k
            if (diff == 1):
                print("Word 1: " + wordi)
                print("Word 2: " + wordj)
                print("Pos: " + str(pos))
                print("Common: " + wordi[0:pos] + wordi[pos+1:len(wordi)])
        

if __name__ == "__main__":
    CalculateFileCheckSum(sys.argv[1])
    FindWords(sys.argv[1])