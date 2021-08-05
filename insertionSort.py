def insertionSort(arr):
    for i in range(len(arr)):
        for j in range(i,0,-1):
            if arr[j]< arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

def printArray(arr):
    for element in arr:
        print(element, end=" ")           
    print()

arr = [4,3,5,2,1]
print("Array before sorting:")
printArray(arr)
insertionSort(arr)
print("Array after sorting:")
printArray(arr)