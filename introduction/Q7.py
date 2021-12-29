t = int(input())
maxInt = 0
lst = []
for _ in range(t):
    a, b = input().split()
    a = int(a)
    b = int(b)
    maxInt = max(b, maxInt)
    lst.append((a, b))

prime = list([True]*(maxInt+1))

if(len(prime) >= 2):
    for i in range(2, maxInt+1):
        if(prime[i]):
            for j in range(i+1, maxInt+1):
                if(j%i == 0):
                    prime[j] = False

for x in lst:
    for i in range(max(x[0], 2), x[1] + 1):
        if(prime[i]):
            print(i,end=" ")
    print()