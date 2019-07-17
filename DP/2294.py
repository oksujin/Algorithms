num = list(map(int,input().split()))
n = num[0]
k = num[1]

a = []

for i in range(0, n+1):
    if i==0:
        a.append(0)
    else:
        a.append(int(input()))

print(a)

dp = []


for i in range(0, k+1):
    tmp = 100001
    if(i==0):
        dp.append(0)  
        continue
    for j in range(1, len(a)):
        if(i-a[j]>=0):
            tmp = min(tmp, dp[i-a[j]])
    dp.append(tmp+1)

print(dp[k])



"""
tmp = 100,001을 넣어주고
만약 동전이 접근할 수 없는 경우에는 100,001이 들어가고
100001이 들어간 경우에는 마지막에 -1 출력
"""