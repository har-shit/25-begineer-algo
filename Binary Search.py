#Creating a list with 1000 random elements
from random import randint
arr = []
for i in range(100):
    x = randint(-100, 100)
    arr.append(x)


        
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
        print(f"Desired Value {vf} Found on index {arr.index(vf)}")
    else:
        print("Not Found") 



   
#Driver code
arr.sort()
vf = int(input("Input The Value To Find in the random list :"))
BS(arr, vf)
