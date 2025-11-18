n=6
for j in range(n,0,-1):
    for i in range(1,j+1):
        print(i,end=" ")
    print( )

#2nd method
n=6
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()