def partition(arr,low,high):
    pivot = arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def sort(arr, low, high):
    if low<high:
        partitionIndex = partition(arr,low,high)
        sort(arr,low,partitionIndex-1)
        sort(arr, partitionIndex+1, high)

def printArray(arr):
    for element in arr:
        print(element, end=" ")           
    print()

arr = [4,3,5,2,1]
print("Array before sorting:")
printArray(arr)
sort(arr,0,len(arr)-1)
print("Array after sorting:")
printArray(arr)