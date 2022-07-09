def findTriplets(arr, n):
   # defining a func..      
    found = False  # Renew the var to false at the end of each loop..
    for i in range(0, n-2):
     
        for j in range(i+1, n-1):
         
            for k in range(j+1, n):
             
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
     
             
    # If no triplet with "sum = 0" found in array..
    if (found == False):
        print(" not exist ")
 
arr = [5, -1, 2, -4, 3]  # Elements in the array..
n = len(arr)  # length of an array..
findTriplets(arr, n) # Calling the func..