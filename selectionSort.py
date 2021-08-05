def selectionSort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def printArray(arr):
    for element in arr:
        print(element, end=" ")           
    print()

arr = [4,3,5,2,1]
print("Array before sorting:")
printArray(arr)
selectionSort(arr)
print("Array after sorting:")
printArray(arr)