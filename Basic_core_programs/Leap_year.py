print("Enter a year")
year=int(input())
# Above func is used to get the input and cast it to int..
if(year%100 == 0) and (year%400 == 0) or (year%4 == 0):  # using logical operators..
    print("Leap Year")
else:
    print("Not a Leap year")