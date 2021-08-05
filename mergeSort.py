def merge(arr,low,mid,high):
    temp=[0]*(high+1)
    for i in range(0,high+1):
        temp[i] = arr[i]
    i=low
    j=mid+1
    k=low
    while i<=mid and j<=high:
        if temp[i]<temp[j]:
            arr[k] = temp[i]
            i+=1
        else:
            arr[k] = temp[j]
            j+=1
        k+=1
    while i<=mid:
        arr[k] = temp[i]
        i+=1
        k+=1
    while j<=high:
        j+=1
        k+=1

def mergeSort(arr,low, high):
    if (low<high):
        mid = (low+high)//2
        mergeSort(arr,low, mid)
        mergeSort(arr,mid+1,high)
        merge(arr,low,mid,high)

def printArray(arr):
    for element in arr:
        print(element, end=" ")           
    print()

arr = [4,3,5,2,1]
print("Array before sorting:")
printArray(arr)
mergeSort(arr,0,len(arr)-1)
print("Array after sorting:")
printArray(arr)