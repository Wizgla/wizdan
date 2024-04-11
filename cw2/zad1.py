import math
def zad1(x,y):
    if isinstance(x, int) == True and isinstance(y,int) == True:
        return x%y
    if isinstance(x, float) == True and isinstance(y,float) == True:
        return math.fmod(x,y)

print(zad1(11.1,10.2))
