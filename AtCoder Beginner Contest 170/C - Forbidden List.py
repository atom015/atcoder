X,N = map(int,input().split())
arr = list(map(int,input().split()))
if X not in arr:
    print(X)
    exit()
sx = X+1
mx = X-1
ans = []
while 1:
    if sx not in arr:
        ans.append(sx)
        break
    sx += 1
while 1:
    if mx not in arr:
        ans.append(mx)
        break
    mx -= 1
if abs(ans[0]-X) < abs(ans[1]-X):
    print(ans[0])
elif abs(ans[0]-X) < abs(ans[1]-X):
    print(ans[1])
else:
    print(min(ans))
