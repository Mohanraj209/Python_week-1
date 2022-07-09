import cmath  # provides access to mathematical operations for complex members..
def Quadratic(a,b,c):
     # defining a func.. 
    
        delta= (b*b)-(4*a*c)  
        root1= (-b + cmath.sqrt(delta))/(2*a)
        root2= (-b - cmath.sqrt(delta))/(2*a)

      # to print the roots..  
        print(delta)
        print(root1)
        print(root2)

try:   # Tests a block of code for errors..
    a=int(input('enter value of a: '))
    b=int(input('enter value of b: '))
    c=int(input('enter value of c: '))
    Quadratic(a,b,c)
except Exception as e:   # exicution takes place when error in "try" block..
    print("invalid input", e)