import sys, re

class Node(object):
    def __init__(self, id):
        self.id = id
        self.dep = 0
        self.next = list()
        self.start = 0
        self.dur = ord(id) - 4

    def add_dependency(self, node):
        self.dep += 1
        node.next.append(self)

def create_graph(filepath):
    nodes = dict()
    final = Node("Z")
    final.id = "ZZ"
    final.dur = 0
    with open(filepath, 'r') as f:
        for line in f.readlines():
            create_dependency(nodes, line[5], line[36])

    for node in nodes.values():
        final.add_dependency(node)

    nodes["ZZ"] = final
    return nodes

def create_dependency(nodes, first, second):
    f = nodes.setdefault(first, Node(first))
    s = nodes.setdefault(second, Node(second))
    s.add_dependency(f)

def part1(nodes):
    available = sorted(nodes.values(), key=lambda node: (node.dep, node.id))
    while len(available) > 1:
        curr = available[0]
        sys.stdout.write(curr.id)
        for node in curr.next:
            node.dep -= 1
        available = sorted(available[1:], key=lambda node: (node.dep, node.id))
    print('')

def part2(nodes, n):
    available = sorted(nodes.values(), key=lambda o: (o.dep, o.id))
    workers = [0 for _ in range(n)]
    while len(available) > 0:
        if(available[0].id == "ZZ"):
            print("Total time: " + str(available[0].start))

        workers = sorted(workers)
        update_next(available[0], workers)

        available = sorted(available[1:], key=lambda node: (node.dep, node.id))

def part2_fix(nodes, n):
    workers = [0 for _ in range(n)]
    while len(nodes.values()) > 0:

        availables = filter(lambda node: node.dep == 0, nodes.values())
        
        tot = min(n, len(availables))
        for _ in range(tot):
            workers = sorted(workers)
            work_avail = filter(lambda node: node.start <= workers[0], availables)
            if(len(work_avail) > 0):
                work_avail = sorted(work_avail, key=lambda node: node.id)
            else:
                work_avail = sorted(availables, key=lambda node: (node.start, node.id))

            curr = work_avail[0]
            if(curr.id == "ZZ"):
                print("Total time: " + str(curr.start))    
            
            update_next(curr, workers)
            availables.remove(curr)
            nodes.pop(curr.id)

def update_next(node, workers):
    worker_time = workers[0]
    node.start = max(worker_time, node.start)
    workers[0] = node.start + node.dur
    for n in node.next:
        n.dep -= 1
        n.start = max(n.start, node.start+node.dur)

if __name__ == "__main__":
    nodes = create_graph(sys.argv[1])
    part1(nodes)
    nodes = create_graph(sys.argv[1])
    part2_fix(nodes, int(sys.argv[2]))