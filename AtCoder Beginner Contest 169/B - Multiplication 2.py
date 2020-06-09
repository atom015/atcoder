N = int(input())
arr = list(map(int,input().split()))

if 0 in arr:
    print(0)
else:
    r = 1
    for i in arr:
        if r*i > 10**18:
            print(-1)
            exit()
        r *= i
    print(r)
    
