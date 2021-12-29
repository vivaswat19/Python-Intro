n = int(input())
flag = False
ans = True
last = 1000000000000
for _ in range(n):
    a = int(input())

    if(a >= last):
        flag = True
    elif(a < last and flag == True):
        ans = False
        break
    elif(a == last):
        ans = False
        break
    last = a

print(ans)
