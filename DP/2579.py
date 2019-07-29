n = int(input())
num = [0]
for i in range (n):
    num.append(int(input()))

dp = [0]
for i in range(1, n+1):
    # 1과 2의 경우에는 초기화를 직접 해줘야한다.
    if i==1:
        dp.append(num[1])
    elif i==2:
        dp.append(num[1]+num[2])
    else:
        """
        세 칸을 연속으로 밟을 수 없기 때문에
        한칸 전에서 오는 경우에는(한칸 전과 현재칸 무조건 두칸 연속으로 밟음)
        세칸 전에서 온다는 것을 함께 나타내야 한다.
        따라서, 세 칸 전의 최대값 + 한칸 전의 값 이렇게 명시해야한다.

        두칸 전에서 오는 경우에는 상관이 없기 때문에 
        두칸 전의 최대값을 바로 넣어준다.
        """
        tmp = max(num[i-1]+dp[i-3], dp[i-2])
        
        # 현재칸의 최대값을 나타낼 때는 num[i]도 더해줘야한다.
        tmp = tmp + num[i] 
        dp.append(tmp)

print(dp[n])
