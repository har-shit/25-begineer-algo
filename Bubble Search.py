from random import randint

L1 = []
for i in range(10):
    x = randint(0, 100)
    L1.append(x)
print(" List of random elements :", L1)

def BubbleSort(list):
    length = len(list)
    for i in range(length-1):
        sorted = False
        for j in range(length-1-i):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                sorted = True
        if not sorted:
            break


BubbleSort(L1)
print("After Sorting :", L1)