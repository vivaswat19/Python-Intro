N = int(input())
for _ in range(N):
    A = int(input())

    for i in range(A+1):
        for j in range(i, A+1):
            if i**2 + j**2 == A:
                print("({}, {})".format(i, j), end = " ")
        
    print()