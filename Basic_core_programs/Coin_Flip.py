import random

toss_num = int(input("Enter the number of flips : "))
tail = 0
head = 0

for value in range(toss_num):
    toss = random.random()
    if toss < 0.5:
        print("Tail")
        tail += 1
    else:
        print("Head")
        head += 1

# Calculating the percentage of tails and heads.

tail_percentage = (tail*100)/toss_num;
head_percentage = 100 - tail_percentage

print("Percentage of head is ",head_percentage,"\npercentage of tail is ",tail_percentage)
