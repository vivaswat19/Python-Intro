inp = int(input())

for i in range(1, inp+1):
    for j in range(1, i+1):
        print(j,end="")
    for j in range(0, inp-i):
        print("*",end="")
    print()