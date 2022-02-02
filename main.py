from libIvanenko import *
import random
if __name__ == '__main__':
    x = random.choices(range(2**8), k = 3*5*7)
    y = [1, 2, 6, 3]
    print(sectionConvo(x, y))
    print(lconvo(x, y))

def main2():
    x, y = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 3, 2, 1]]
    a, b = [dft(x), dft(y)]
    m = [a[i]*b[i] for i in range(7)]
    print(invdft(m))
    print(rconvo(x, y))


def rconvo2dphysviadft():
    x, y = [[random.choices(range(0, 2**8), k=16) for j in range(16)] for i in range(2)]
    a = dft2dphys(x)
    b = dft2dphys(y)
    m = [[a[i][j] * b[i][j] for j in range(16)] for i in range(16)]
    print(m)
    m = [invdft(m[i]) for i in range(16)]
    for i in range(len(m[0])):
        col = invdft([m[-j-1][i] for j in range(len(m))])
        for j in range(len(m)):
            m[-j-1][i] = col[j]
    print(m)
    print(rconvo2dphys(x, y))