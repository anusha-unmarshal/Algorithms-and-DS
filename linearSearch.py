def search(arr, key):
    for element in arr:
        if element == key:
            return arr.index(element)
    return -1

arr = [2, 7, 10, 4, 8]
index = search(arr, 3)
if index >=  0:
    print("Element found at position {}".format(index + 1))
else:
    print("Element not found in the array")
