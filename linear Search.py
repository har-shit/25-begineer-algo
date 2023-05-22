# list of random elements
arr = [4, 65, 98, 34, 98, 21, 98, 9, 95, 27, 8,  7, 65, 4, 9 ,654, 89, 29, 83, 78, 32, 19, 79, 23, 64, 32]

#taking input value to find in list
value_to_find = int(input("Value to find :"))

#this loop covers all elements in the list until it finds the desired value to find and prints -
# the position of the value in list
for i in arr:
    if i == value_to_find:
        if (arr.index(i)+1)==1:
            print(f"Desired value is present in the list on {(arr.index(i))+1}st Position")
            break
        elif (arr.index(i)+1)==2:
            print(f"Desired value is present in the list on {(arr.index(i))+1}nd Position")
            break
        elif (arr.index(i)+1)==3:
            print(f"Desired value is present in the list on {(arr.index(i))+1}rd Position")
            break
        else:
            print(f"Desired value is present in the list on {(arr.index(i))+1}th Position")
            break
    elif i == arr[-1] and i != value_to_find:
        print("Not Found")
        break