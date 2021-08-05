arr = [6,10,3,8,2,5]
N = len(arr)-1

def maxheap(arr,i):
    global N
    left = 2*i
    right = 2*i +1
    max=i
    if left <= N and arr[left]>arr[i]:
        max = left
    if right <= N and arr[right] > arr[max]:
        max=right
    if max != i:
        arr[i], arr[max] = arr[max], arr[i]
        maxheap(arr,max)

def heapify(arr):
    N= len(arr)-1
    for i in range(N//2, -1, -1):
        maxheap(arr,i)
    
def sort(arr):
    global N
    heapify(arr)
    for i in range(N,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        N = N-1
        maxheap(arr,0)

def printArray(arr):
    for element in arr:
        print(element, end=" ")           
    print()

print("Array before sorting:")
printArray(arr)
sort(arr)
print("Array after sorting:")
printArray(arr)