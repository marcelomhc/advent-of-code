a = b= c = d = e = 0
loop = list()
while(True):
    c = d | 65536
    d = 6152285
    while(True):
        b = c & 255
        d = d + b
        d = d & 16777215
        d = d * 65899 
        d = d & 16777215
        if(256 > c):
            if (d in loop):
                print(loop[0])
                print(loop[-1])
                exit(0)
            loop.append(d)
            break
        b = 0
        c = c //256