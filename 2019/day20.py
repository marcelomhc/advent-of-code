
def parse(filepath, recursion=False):
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()

        grid = dict()
        portals = dict()

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                char = lines[y][x]
                if(char == '.'):
                    grid[(x,y)] = []
                    neighboors = get_neighboors((x,y))
                    for x2,y2 in neighboors:
                        nb = lines[y2][x2]
                        if(nb == '.'):
                            grid[(x,y)].append((x2,y2,0))
                        elif('A' <= nb <= 'Z'):
                            second = lines[y2*2-y][x2*2-x]
                            portal = nb + second if x2 > x or y2 > y else second + nb
                            jump = portals.get(portal, None)
                            if (jump):
                                grid[(x,y)].append(jump)
                                grid[(jump[0], jump[1])].append((x,y, jump[2]*-1))
                            else:
                                if(recursion):
                                    if(portal == 'AA' or portal == 'ZZ'):
                                        portals[portal] = (x,y,0)
                                    elif(x2 == 1 or y2 == 1 or x2 == len(lines[y])-2 or y2 == len(lines)-2):
                                        portals[portal] = (x,y,1)
                                    else:
                                        portals[portal] = (x,y,-1)
                                else:
                                    portals[portal] = (x,y, 0)
    return grid, portals['AA'], portals['ZZ']

def get_neighboors(position):
    x,y = position
    return [(x-1,y), (x+1, y), (x, y-1), (x,y+1)]

def maze():
    grid, src, dst = parse("input/day20.data")
    bfs(grid, src, dst)

def bfs(board, src, dst):
    queue = list()
    queue.append((0, src))
    visited = set()

    while(src != dst):
        steps, src = queue.pop(0)
        if (src not in visited):
            visited.add(src)
            sx,sy,sz = src
            for nx,ny,nz in board[(sx,sy)]:
                if(nz+sz >= 0):
                    queue.append((steps + 1, (nx,ny,nz+sz)))
    print(steps)

def recursion():
    grid, src, dst = parse("input/day20.data", True)
    bfs(grid, src, dst)


if __name__ == "__main__":
    maze()
    recursion()
