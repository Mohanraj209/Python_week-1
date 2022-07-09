
def WindCalculation(t,v):
     # defining a func..
    try:  # Tests a block of code for errors..
        w=35.74+(0.6215*t)+((0.4275*t)-35.75)*pow(v,0.16)
        # calculation part
        print('calculated windchill is :',w)
    except Exception as e: # this block handles the error..
        print("invalid", e)    

def userinput():
         temp= int(input('enter the value of temperature in Fahrenheit less then 50: '))
         vel= int(input('enter wind speed in miles per hour from 3 to 120: '))
         return temp,vel

t,v = userinput()  # t = temp  and v = wind speed..
if(v > 120 or v < 3 or t > 50 ):
    print("Can't get WindChill at this Parameters")
else:
    WindCalculation(t,v)