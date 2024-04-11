import math
def zad2(a,n):
    result = "|"
    for i in range(2,n+1):
       result += str(math.log(a,i)) + "|" #логарифм из a по основанию i
    return result

print(zad2(8,4))
