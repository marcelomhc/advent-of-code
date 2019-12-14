def parse_input(filepath):
    with open(filepath, "r") as f:
        program = [char for char in f.readline()]
    return program

def count_zeros(data):
    x = 25
    y = 6
    n = x*y

    layers = [data[i * n:(i + 1) * n] for i in range((len(data) + n - 1) // n )]
    

    layer = min(layers, key=lambda l: l.count('0'))
    print(layer.count('0'), layer.count('1')*layer.count('2'))

def decode_image(data):
    w = 25
    h = 6

    layers = len(data)//(w*h)

    for y in range(h):
        for x in range(w):
            pixel = [data[(y*w + x)+i*w*h] for i in range(layers)]
            p = next(p for p in pixel if p != '2')
            print(p, end='')
        print('')




if __name__ == "__main__":
    data = parse_input("input/day8.data")
    count_zeros(data)
    decode_image(data)