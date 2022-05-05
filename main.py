import math
k = 0
suma = 0

def pole(x):
    if len(x) == 1:
        return pow(float(x[0]),2)*math.pi
    if len(x) == 2:
        return float(x[0]) * float(x[1])
    if len(x) == 3:
        p = (float(x[0])+float(x[1])+float(x[2]))/2
        return math.sqrt(p*(p-float(x[0]))*(p-float(x[1]))*(p-float(x[2])))

n= input()
n= int(n)
for i in range(0, n):
    temp=input()
    temp = temp.split()
    if len(temp) > 3:
        print("Błąd: można podać maksymalnie 3 liczby")
        k = 1
        break
    suma += pole(temp)
if k != 1:
    print(round(suma, 2))