ans = [0]*4
for i in range(int(input())):
    S = input()
    if S == "AC":
        ans[0] += 1
    elif S == "WA":
        ans[1] += 1
    elif S == "TLE":
        ans[2] += 1
    else:
        ans[3] += 1
print("AC x {}\nWA x {}\nTLE x {}\nRE x {}".format(*ans))
