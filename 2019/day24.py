def parse_infinity(filepath):
    grid = {}
    with open(filepath, "r") as f:
        y = 0
        bio = 1
        lines = f.read().splitlines()
        for line in lines:
            x = 0
            for char in line:
                grid[(x,y, 0)] = 1 if char == '#' else 0
                x+=1
                bio*=2
            y +=1
    return grid

def cycle(grid):
    bios = set()
    bio = biodiversity(grid)
    while(not bio in bios):
        bios.add(bio)
        position_list = grid.keys()
        grid = get_next_gen(grid, position_list, get_plain_neighboors)
        bio = biodiversity(grid)
    print(bio)

def get_next_gen(grid, position_list, func):
    next_gen = dict()
    for key in position_list:
        value = grid.get(key, 0)
        next_gen[key] = evaluate_life(value, get_neighboors_count(grid, key, func))
    return next_gen

def get_neighboors_count(grid, key, func):
    n = 0
    for neighboor in func(key):
        n += grid.get(neighboor, 0)
    return n

def evaluate_life(value, n):
    if(value == 1 and n != 1):
        return 0
    elif(value == 0 and (n == 1 or n == 2)):
        return 1
    else:
        return value

def get_plain_neighboors(position):
    x,y,z = position
    return [(x-1,y,z), (x+1, y,z), (x, y-1,z), (x,y+1,z)]

def biodiversity(grid):
    return sum([bug*(pow(2,x+5*y)) for (x,y,z),bug in grid.items()])

def print_gen(grid):
    zs = sorted(set([z[2] for z in grid.keys()]))
    for z in zs:
        print("Depth: " + str(z))
        for y in range(5):
            for x in range(5):
                print('.' if(grid.get((x,y,z),0)) == 0 else '#', end='')
            print('')
        print('')

def infinity(minutes):
    grid = parse_infinity("input/day24.data")

    for _ in range(minutes):
        neighboors = list(grid.keys())
        for key in grid.keys():
            neighboors += dimensional_neighboors(key)
        grid = get_next_gen(grid, set(neighboors), dimensional_neighboors)
    print(sum(grid.values()))

def dimensional_neighboors(position):
    neighboors = get_plain_neighboors(position)
    x,y,z = position
    if(x == 0):
        neighboors.remove((-1,y,z))
        neighboors.append((1,2,z+1))
    elif(x == 4):
        neighboors.remove((5,y,z))
        neighboors.append((3,2,z+1))
    if(y == 0):
        neighboors.remove((x,-1,z))
        neighboors.append((2,1,z+1))
    elif(y == 4):
        neighboors.remove((x,5,z))
        neighboors.append((2,3,z+1))
    if((2,2,z) in neighboors):
        neighboors.remove((2,2,z))
        neighboors += [(c,int(y>2)*4,z-1) if x==2 else (int(x>2)*4,c,z-1) for c in range(5)]
    #print([position] + neighboors)
    return neighboors


if __name__ == "__main__":
    grid = parse_infinity("input/day24.data")
    cycle(grid)
    infinity(200)