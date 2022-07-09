harmonic_range = int(input("Enter the range to calculate Nth Harmonic number "))
harmonic_number = 0 # initial value

# Start iteration from 1 to given range
for i in range(1,harmonic_range+1):
    # harmonic series. i.e. 1 + 1/2 +1/3 +1/4...
    if harmonic_range == 0:
        print("Enter the valid range")
    else:
        harmonic_number += 1 / i
print("The Nth Harmonic number is ", harmonic_number)