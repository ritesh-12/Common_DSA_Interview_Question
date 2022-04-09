# Binary Search in python

#  Iterative method
def binarySearcIt(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high: #low=0,high=7

        mid = low + (high - low)//2
          #mid = 3  [3, 4, 5, 6, 7, 8, 9,10] x=4  T(n) = T(n/2)+C

           #  4+1=5       mid = (low+high)//2        
        if array[mid] == x: 
            return mid

        elif array[mid]< x:
            low = mid + 1

        else:
            high = mid - 1 #high=2

    return -1


# Recursive approachs
def binarySearchR(array, x, low, high): #[3, 4, 5, 6, 7, 8, 9]

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearchR(array, x, low, mid-1) #high=2

        # Search the right half
        else:
            return binarySearchR(array, x, mid + 1, high)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
#array.sort()
x = 10       #int(input())

#result = binarySearchR(array, x, 0, len(array)-1)
result = binarySearcIt(array, x, 0, len(array)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
