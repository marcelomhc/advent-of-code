from collections import defaultdict

def terrain_of(pos):
    return erosion[(pos[0],pos[1])] % 3

def erosion_of(pos):
    return (geo_idx[(pos[0],pos[1])] + depth) % 20183

def gi_of(pos):
    x,y = pos
    if(y == target[1] and x == target[0]):
        return 0
    elif(y == 0):
        return x*16807
    elif(x == 0):
        return y*48271
    else:
        return erosion[(x-1,y)] * erosion[(x,y-1)]

depth = 4845
target = (6,770)
geo_idx = dict()
erosion = dict()
terrain = dict()
time = dict()

def part1():
    risk = 0
    #prefill()
    for x in range(target[0]+1):
        for y in range(target[1]+1):
            risk += terrains((x,y))

    print(risk)

def part2bfs():
    queue = list()
    minutes = float('inf')
    visited = dict()

    queue.append(((0,0), 0, 1))

    while(len(queue) > 0):
        ((x,y), time, gear) = queue.pop(0)
        prev = visited.setdefault((x,y,gear),9999999)
        if(prev <= time):
            continue
        visited[(x,y,gear)] = time
        if(time >= minutes):
            continue
        if((x,y) == target and gear == 1):
            minutes = min(minutes, time)
            print(minutes)
            continue

        for (dx,dy) in [(0,-1),(-1,0),(1,0),(0,1)]:
            xx = x+dx
            yy = y+dy
            if(xx < 0 or yy < 0):
                continue
            
            ttype = terrains((xx,yy))
            if(ttype != gear):
                queue.append(((xx,yy), time+1, gear))
        new_gear = change_gear(terrains((x,y)), gear)
        queue.append(((x,y), time+7, new_gear))
    
    print(max(visited.keys(), key=lambda l: l[0]))
    print(max(visited.keys(), key=lambda l: l[1]))
    print(minutes)

def change_gear(region, gear):
    #0 = rocky, neither
    #1 = wet, torch
    #2 = narrow, climbing

    if(region == 0):
        return gear % 2 + 1
    elif(region == 1):
        return int(gear == 0) * 2 
    else:
        return (gear+1) % 2

def terrains(pos):
    if (terrain.get(pos) == None):
        terrain[pos] = erosion_level(pos) % 3
    return terrain[pos]

def erosion_level(pos):
    if( erosion.get(pos) == None):
        gi = geologic_index(pos)
        erosion[pos] = (gi + depth) % 20183
    return erosion[pos]

def prefill(a,b):
    for x in range(a+1):
        for y in range(b+1):
            erosion_level((x,y))

def geologic_index(pos):
    (x,y) = pos
    if (geo_idx.get(pos) == None):
        if(x == 0 and y == 0):
            geo_idx[pos] = 0
        elif(x == target[0] and y == target[1]):
            geo_idx[pos] = 0
        elif(y == 0):
            geo_idx[pos] = x*16807
        elif(x == 0):
            geo_idx[pos] = y*48271
        else:
            geo_idx[pos] = erosion_level((x-1,y)) * erosion_level((x,y-1))
    return geo_idx[pos]


if __name__ == "__main__":
    part1()
    part2bfs()