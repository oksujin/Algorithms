n = int(input())

dp = []
dp.append(0) #0
dp.append(0) #1

for i in range(2, n+1):
    """
    우선 dp에 1을 뺀 수의 최솟값을 대입하고
    2로 나눠지면 1로 뺀 수의 최솟값 vs 2로 나눈수의 최소값
    둘 중 어느 루트로 와야 최솟값인지 계산

    2,3으로 모두 나눠질 수도 있기 때문에
    elif 쓰지 않고 둘 다 if로 사용

    즉, i-1, 2, 3 세가지 모두 고려 가능
    """
    dp.append(dp[i-1])

    if i%2 == 0:
        dp[i] = min(dp[i//2], dp[i])
        
    if i%3 == 0:
        dp[i] = min(dp[i//3], dp[i])
    
    dp[i] = dp[i] + 1

print(dp[n])