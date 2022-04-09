rows = int(input("Enter number of rows: "))
k = 0
#this loop for number of rows just
for i in range(1, rows+1):
    #this loop for print the space
    for space in range(1, (rows-i)+1): 
        print(end="  ")
    #this loop for rint the star K!=(2*i-1)--> remember this condition for print star 
    while k!=(2*i-1): 
        print("* ", end="")
        k += 1
   
    k = 0
    print()