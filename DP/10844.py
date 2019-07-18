n = int(input())

dp = []
dp.append([])

for i in range(1, n+1):
    if i==1:
        dp.append([1,1,1,1,1,1,1,1,1,1])
    else :
        tmp = []
        # 0은 다음에 나올 수 있는 수가 1뿐이다.
        tmp.append(dp[i-1][1])

        # 1부터 8까지는 뒤에 나오는 숫자가 +1, -1모두 가능하다.
        for j in range(1,9):
            tmp.append(dp[i-1][j-1] + dp[i-1][j+1])

        # 9는 다음에 나올 수 있는 수가 8뿐이다.
        tmp.append(dp[i-1][8])
        
        # 값을 모아놓은 tmp를 dp에 넣는다.
        dp.append(tmp)
 
sum = 0
for i in range(1,10):
     sum = sum + dp[n][i]
    
print(sum%1000000000)