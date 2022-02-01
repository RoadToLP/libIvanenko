from libIvanenko import *
import random
if __name__ == '__main__':
    s = random.choices(range(1, 4), k=4)
    print(fastDft(s))
    print("fastDft Ok")
    print(dft(s))
    print("dft Ok")
