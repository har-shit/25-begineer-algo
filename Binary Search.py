#Creating a list with 1000 random elements
from random import randint, choice
arr = []
for i in range(100):
    x = randint(-100, 100)
    arr.append(x)

#selecting a random element from the digit to search for. 
vf = choice(arr)

#sorting the list to perform binary search
arr.sort()

#printing the list and the element to find after sorting the list
print(arr)
print(f"Value to find is {vf}")

        
#Defining the Binary Search algorithm
def BS(arr, vf):

    L = 0
    H = len(arr)-1
    found = False    

    while L <= H and not found:
        mid = (L+H)//2
        if vf == arr[mid]:
            found = True
        elif vf > arr[mid]:
            L = mid+1
        else:
            H = mid-1
    if found == True:
        print(f"Desired Value {vf} Found on index {mid}")
    else:
        print("Not Found") 



#envoking the binary search function
BS(arr, vf)
