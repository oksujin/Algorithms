Enc = input()

mod = 1000000

dp = []
dp.append(1) # 0

'''
    Solution
    만약 이전 인덱스의 문자 + 현재 문자 가 10~26 사이의 수라면 : dp[i] = dp[i-1] + dp[i-2]
                                            아니라면 : dp[i] = dp[i-1]
    * 주요 예외처리 *
    1. 0 만 입력된 경우 : 경우의 수 0
    2. 0 이 첫 자리에 있을 경우 : 경우의 수 0
'''
for i in range(0, len(Enc)):

    if int(Enc[i]) != 0 :
        dp.append(dp[i])
    else : 
        dp.append(0)

    if i>=1 :
        tmp = int(Enc[i-1] + Enc[i])
        if 10 <= tmp and tmp <= 26 :
            dp[i+1] = (dp[i+1] + dp[i-1]) % mod

print(dp)
if Enc == "0" :
    print(0)
else :
    print(dp[len(Enc)])