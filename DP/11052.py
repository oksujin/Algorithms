N = int(input())
p = list(map(int,input().split()))
p.insert(0,0)

dp = []
dp.append(0)

for i in range(1, N+1):
    if i==1:
        dp.append(p[1])
    elif i==2:
        dp.append(max(2*p[1], p[2]))
    else:
        tmp = 0
        for j in range(1, i+1):
            tmp = max(tmp, p[j] + dp[i-j])
        dp.append(tmp)
print(max(dp))