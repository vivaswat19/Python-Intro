inp = int(input())

if(inp%2 == 0):
    print("Not Prime")
    exit()

for i in range(3, inp):
    if(inp%i == 0):
        print('Not Prime')
        exit()

print("Prime")
    