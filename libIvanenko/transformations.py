from libIvanenko.util import *
def dft(x):
    core = generateFourierCore(len(x))
    X = [sum([core[i][j]*x[j] for j in range(len(x))]) for i in range(len(x))]
    return X

def dht(x):
    core = generateHartleyCore(len(x))
    X = [sum([core[i][j]*x[j] for j in range(len(x))]) for i in range(len(x))]
    return X

def dht2dphys(m):
    m = [dht(x) for x in m]
    for i in range(len(m[0])):
        col = dht([m[-j-1][i] for j in range(len(m))])
        for j in range(len(m)):
            m[-j-1][i] = col[j]
    return m

def dft2dphys(m):
    m = [dft(x) for x in m]
    for i in range(len(m[0])):
        col = dft([m[-j-1][i] for j in range(len(m))])
        for j in range(len(m)):
            m[-j-1][i] = col[j]
    return m

def dht2dalg(m):
    m = [dht(x) for x in m]
    for i in range(len(m[0])):
        col = dht([m[j][i] for j in range(len(m))])
        for j in range(len(m)):
            m[j][i] = col[j]
    return m

def dft2dalg(m):
    m = [dft(x) for x in m]
    for i in range(len(m[0])):
        col = dft([m[j][i] for j in range(len(m))])
        for j in range(len(m)):
            m[j][i] = col[j]
    return m

def invdft(x):
    return [a.conjugate()/len(x) for a in dft([b.conjugate() for b in x])]

def invdht(x):
    return [a/len(x) for a in dht(x)]

def harmonicAmp(x, n):
    return abs(dft(x)[n])/len(x)


