import math
def Distance(a,b):
     # defining a func.. 
    distance= math.sqrt(pow(a,2)+pow(b,2)) # to cal the distance..
    print(distance)

try:
    a=int(input('enter a value: '))
    b=int(input('enter b value: '))
    Distance(a,b)
except Exception as e:
    print("invalid input",e)