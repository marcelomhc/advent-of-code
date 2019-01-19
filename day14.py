
def part1(n):
    DELTA = 10
    recipes = [3,7]

    idx1 = 0
    idx2 = 1

    while (len(recipes) < n + DELTA):
        new = recipes[idx1] + recipes[idx2]

        if(new > 9):
            recipes.append(1)
            new = new % 10
        
        recipes.append(new)

        idx1 = (idx1 + 1 + recipes[idx1]) % len(recipes)
        idx2 = (idx2 + 1 + recipes[idx2]) % len(recipes)
        
    rec = recipes[-DELTA:]
    print ''.join(str(p) for p in rec) 

def part2(n):
    n = [int(x) for x in str(n)]
    recipes = [3,7]

    idx1 = 0
    idx2 = 1

    while (len(recipes) < len(n) or (recipes[-len(n):] != n and recipes[-len(n)-1:-1] != n)):
        new = recipes[idx1] + recipes[idx2]

        if(new > 9):
            recipes.append(1)
            new = new % 10
        
        recipes.append(new)

        idx1 = (idx1 + 1 + recipes[idx1]) % len(recipes)
        idx2 = (idx2 + 1 + recipes[idx2]) % len(recipes)
        
    print(len(recipes) - len(n) - int(recipes[-len(n)-1:-1] == n))

if __name__ == "__main__":
    part1(5)
    part1(9)
    part1(18)
    part1(2018)
    part1(360781)
    print()
    part2(51589)
    part2('01245')
    part2(92510)
    part2(59414)
    part2(360781)