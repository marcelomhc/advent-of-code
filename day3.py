import sys
import re

class Claim(object):
    def __init__(self, id, x, y, width, height):
        self.id = int(id)
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)

    def left(self):
        return self.x

    def right(self):
        return self.x + self.width - 1

    def top(self):
        return self.y

    def bottom(self):
        return self.y + self.height - 1

def main(filepath):
    claims = parse_input(filepath)
    claims = sorted(claims, key=lambda obj: (obj.x, obj.y))
    overlaps, ids = get_overlaps(claims)
    max_width = max(overlaps, key=lambda obj: obj.right())
    max_height = max(overlaps, key=lambda obj: obj.bottom())
    matrix = [[0 for x in range(max_height.bottom()+1)] for y in range(max_width.right()+1)]

    for overlap in overlaps:
        for i in range(overlap.left(), overlap.right()+1):
            for j in range(overlap.top(), overlap.bottom()+1):
                matrix[i][j] = 1

    total = 0
    for row in matrix:
        for value in row:
            total = total + value
    
    print("Total of overlaps: " + str(total))

    for i in range(len(ids)):
        if (not ids[i]):
            print("Id without overlap: #" + str(i))
            break

def parse_input(filepath):
    claims = []
    with open(filepath, "r") as f:
        for line in f:
            result = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
            claim = Claim(result.group(1), result.group(2), result.group(3), result.group(4), result.group(5))
            claims.append(claim)
    return claims

def get_overlaps(claims):
    overlaps = list()
    ids = [False for i in range(len(claims)+1)]
    ids[0] = True
    for i in range(len(claims)):
        claim = claims[i]
        for j in range(i+1, len(claims)):
            claim2 = claims[j]
            if (claim2.left() > claim.right()):
                break      
            if(claim.top() > claim2.bottom() or claim2.top() > claim.bottom()):
                continue
            overlaps.append(
                Claim(
                    0, 
                    claim2.left(),
                    max(claim.top(), claim2.top()),
                    min(claim.right(), claim2.right()) - claim2.left() + 1,
                    min(claim.bottom(), claim2.bottom()) - max(claim.top(), claim2.top()) + 1
                )
            )
            ids[claim.id] = True
            ids[claim2.id] = True

    return overlaps, ids

# Quick answer
def get_total_overlaps(claims):
    matrix = [[0 for x in range(1000)] for y in range(1000)]
    for claim in claims:
        for i in range(claim.width):
            for j in range(claim.height):
                matrix[i+claim.left()][j+claim.top()] += 1
    
    total = 0
    for row in matrix:
        for value in row:
            total += int(value > 1)
    
    return total

if __name__ == "__main__":
    main(sys.argv[1])