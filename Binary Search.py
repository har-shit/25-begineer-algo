arr = [1, 3, 8, 9, 13, 21, 25, 27, 28, 32, 38, 44, 48, 49, 56, 59, 61, 62, 66, 77, 79, 83, 86, 88, 94, 99]

def BS(List, vf):

    L = 0
    H = len(arr)-1

    while L <= H:
        mid = (L+H)//2
        if vf == arr[mid]:
            print(f"Value Found At {arr.index(mid)}")
            break
        elif vf < arr[mid]:
            H = (mid-1)
        else:
            L = mid+1
    

VF = int(input("Input The Value To Find :"))

BS(arr, VF)