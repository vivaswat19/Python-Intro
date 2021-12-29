inp = int(input())

for i in range(inp):
    for j in range(inp - i):
        print(j+1,end=" ")
    if i == 0:
        print()
        continue
    for j in range(2*(i-1) + 1):
        print("*",end=" ")
    
    print()	