import random
stake=100
goal=200
win=0
loose=0
while (stake>0 and stake<goal):
   # using while loop.. 
    gamble=random.randint(0,1) # Randint is a built-in func of "random" module..
    if gamble==0: 
        stake-=1   # Substraction assignment operator..
        loose+=1   # Addition assignment operator..
    else:
        stake+=1
        win+=1

print("number of wins: ",+win)    # gives num of wins..
winPercentage=(win*100)/(win+loose)
losspercentage=100-winPercentage
print("win percentage is: ",+winPercentage)
print("Loss percentage is: ", +losspercentage)