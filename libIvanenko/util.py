import math
def genCorePart(n, k):
    angle = 2 * math.pi / n
    return complex(math.cos(-k*angle), math.sin(-k*angle))


def generateFourierCore(n):
    res = []
    angle = 2*math.pi/n
    for i in range(n):
        part = []
        for j in range(n):
            part.append(complex(math.cos(-i*j*angle), math.sin(-i*j*angle)))
        res.append(part)
    return res

def generateHartleyCore(n):
    res = []
    angle = 2*math.pi/n
    for i in range(n):
        part = []
        for j in range(n):
            part.append(math.cos(i*j*angle) + math.sin(i*j*angle))
        res.append(part)
    return res

def linearExtract(x, n):
    return 0 if n >= len(x) or n < 0 else x[n]

def linearExtract2d(x, n, m):
    return 0 if (n >= len(x) or n < 0 or m >= len(x[0]) or m < 0) else x[n][m]

# def roundError(n):
#     if abs(round(n)-n) < 0.001:
#         return [round(n), True]
#     else:
#         return [n, False]
#
# def findPretty(n):
#     sqrt2 = n/(2**(0.5))
#     sqrt3 = n/(3**(0.5))
#     if roundError(sqrt2)[1]:
#         return f"{roundError(sqrt2)[0]}√2"
#     if roundError(sqrt3)[1]:
#         return f"{roundError(sqrt3)[0]}√3"
#     return str(roundError(n)[0])
#
# def printArray(arr):
#     s = "["
#     for i, v in enumerate(arr):
#         re, im = roundError(v.real)[0], roundError(v.imag)[0]
#         if i:
#             s += ", "
#         if re != 0:
#             s += findPretty(re)
#         if im != 0:
#             s += ("+" if im > 0 and re != 0 else "") + findPretty(im) + "j"
#         if re == 0 and im == 0:
#             s += "0"
#     s += "]"
#     print(s)
#

