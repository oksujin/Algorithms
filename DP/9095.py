n = int(input())

dp=[]
for i in range (0, n+1):
    if i==0:
        dp.append(0)
    elif i==1 :
        dp.append(1)
    elif i==2 :
        dp.append(2)
    elif i==3 :
        dp.append(4)
    else:
        dp.append(dp[i-3]+dp[i-2]+dp[i-1])
print(dp)
print(dp[n])