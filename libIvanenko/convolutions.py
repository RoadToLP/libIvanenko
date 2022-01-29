from libIvanenko.util import *
from libIvanenko.transformations import *



def rconvo(x, h):
    return [sum([x[j]*h[i-j] for j in range(len(x))]) for i in range(len(h))]

def lconvo(x, h):
    return [sum([x[j]*linearExtract(h, i-j) for j in range(len(x))]) for i in range(len(h)+len(x)-1)]

def rconvo2dphys(x, h):
    y = []
    for m in range(len(x)):
        part = []
        for n in range(len(x[0])):
            part.append(sum([x[l][k] * h[m-l][n-k] for k in range(len(x[0])) for l in range(len(x))]))
        y.insert(0, part)
    return y

def lconvo2dphys(x, h):
    y = []
    for m in range(len(x[0]) + len(h) - 1):
        part = []
        for n in range(len(x) + len(h[0]) - 1):
            part.append(sum([x[l][k] * linearExtract2d(h, m-l, n-k) for k in range(len(x[0])) for l in range(len(x))]))
        y.append(part)
    return y

def rconvo2dalg(x, h):
    y = []
    for m in range(len(x)):
        part = []
        for n in range(len(x[0])):
            part.append(sum([x[k][l] * h[m - k][n - l] for k in range(len(x)) for l in range(len(x[0]))]))
        y.append(part)
    return y

def lconvo2dalg(x, h):
    y = []
    for n in range(len(x[0]) + len(h[0]) - 1):
        part = []
        for m in range(len(x) + len(h) - 1):
            part.append(sum([x[k][l] * linearExtract2d(h, m-k, n-l) for k in range(len(x)) for l in range(len(x[0]))]))
        y.append(part)
    return y

def sectionConvo(x, h):
    if (len(h) % len(x)) != 0:
        raise ArithmeticError("asdasd")
    l = len(x)*2-1
    out = [0]*(len(x)+len(h)-1)
    for i in range(0, len(h), len(x)):
        for j, n in enumerate(lconvo(x, h[i:i+len(x)])):
            out[i+j] += n

    return out

def lconvoviaR(x, h):
    x += [0]*(len(h)-1)
    h += [0] * (len(x) - len(h))
    return rconvo(x, h)

def rconvoviadft(x, h):
    return invdft([i*j for i, j in zip(dft(x), dft(h))])

def lconvoviadft(x, h):
    x += [0] * (len(h) - 1)
    h += [0] * (len(x) - len(h))
    return rconvoviadft(x, h)

