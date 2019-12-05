import sys

def fill_panel(filepath, panel, initial):
    # For part 2
    intersections = []

    # Both
    with open(filepath, "r") as f:
        line_num = 0
        for line in f:
            line_num += 1
            step_count = 0
            pos = initial
            instructions = map(lambda k: (k[0], int(k[1:])), line.split(','))
            for direction, steps in instructions:
                dx = dy = 0
                (posX, posY) = pos
                if(direction=='R'):
                   dx = 1
                elif(direction=='L'):
                    dx = -1
                elif(direction=='U'):
                    dy = 1
                else:
                    dy = -1

                if(dx != 0):
                    for i in range(posX+dx, posX+dx*(steps+1), dx):
                        step_count += 1
                        pos = (i,posY)
                        if(panel.get(pos) != None and panel.get(pos)[1] != line_num):
                            intersections.append(step_count + int(panel.get(pos)[0]))
                            panel[pos] = 'X'
                        else:
                            panel[pos] = (str(step_count), line_num)
                if(dy != 0):
                    for j in range(posY+dy, posY+dy*(steps+1), dy):
                        step_count += 1
                        pos = (posX, j)
                        if(panel.get(pos) != None and panel.get(pos)[1] != line_num):
                            intersections.append(step_count + int(panel.get(pos)[0]))
                            panel[pos] = 'X'
                        else:
                            panel[pos] = (str(step_count), line_num)
    #print_panel(panel)
    print(min(intersections))
    return panel

def find_intersections(panel, initial):
    min_dist = 999999
    for key in panel.keys():
        if(panel.get(key)=='X'):
            dist = get_dist(key, initial)
            min_dist = min(min_dist, dist)
    print(min_dist)

def get_dist(point, reference):
    return abs(point[0]-reference[0]) + abs(point[1]-reference[1])

def print_panel(panel):
    keys = panel.keys()
    maxX = max(keys, key=lambda k: k[0])
    minX = min(keys, key=lambda k: k[0])
    maxY = max(keys, key=lambda k: k[1])
    minY = min(keys, key=lambda k: k[1])

    for j in range(maxY[1]+1, minY[1]-1, -1):
        for i in range(minX[0], maxX[0]+1):
            print (panel.setdefault((i,j), '.'), end='')
        print('')

if __name__ == "__main__":
    panel = dict()
    initial = (0,0)
    panel[initial] = 'o'
    panel = fill_panel("input/day3.data", panel, initial)
    intersections = find_intersections(panel, initial)