'''
def search(arr, x):
	if x in arr:
        return True
    return -1
'''
arr = [3,40,30,2,40,45]
x=int(input())
#y = search(arr,40)
if x in arr:
    print("present")
else:
    print("not present")

#for loop
arr = [3,40,30,2,40,45.......n] # T(n) = O(n), T(n) = O(1), (n+1)/2=n/2+1/2=O(n)
x=int(input())
for i in range(len(arr)):#0-->5
    if arr[i] == n:
        flag =1
        break
       
if flag == 1:
    print("Present")
else:
    print("not present")
