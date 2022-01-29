from libIvanenko.transformations import *
def interpolate(x, n):
    dhtx = dht(x)
    harmonics = (len(x)-1)//2
    middleNeeded = len(x) % 2 == 0
    middle = 0 if not middleNeeded else dhtx[len(x)//2]/2
    interpolated = [dhtx[0]*n]
    interpolated += [dhtx[i+1]*n for i in range(harmonics)]
    interpolated += [middle*n] if middleNeeded else []
    interpolated += [0]*(len(x)*n-(harmonics*2+middleNeeded*2+1))
    interpolated += [middle*n] if middleNeeded else []
    interpolated += [dhtx[1+harmonics+middleNeeded+i]*n for i in range(harmonics)]
    return invdht(interpolated)

def thin(x, n):
    dhtx = dht(x)
    harmonics = (len(x)//n - 1) // 2
    middleNeeded = (len(x)//n) % 2 == 0
    middle = (dhtx[1+harmonics]+dhtx[-1-harmonics])
    thinned = [dhtx[0]/n]
    thinned += [dhtx[i+1]/n for i in range(harmonics)]
    thinned += [middle/n] if middleNeeded else []
    thinned += [dhtx[-harmonics+i]/n for i in range(harmonics)]
    return invdht(thinned)

