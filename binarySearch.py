def search(arr, low, high, key):
    if high >= low:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return search(arr, low, mid-1, key)
        else:
            return search(arr,mid+1, high, key)
    return -1

arr = [2,5,8,10,15,20,30]
result = search(arr,0,len(arr)-1,3)
if result==-1:
    print("Element not found")
else:
    print("element found at position {}".format(result+1))
