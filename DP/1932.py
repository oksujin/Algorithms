# 백준 19332 정수 삼각형

n = int(input())
tri = []
tri.append([])
# 2차원 배열을 만들고, index가 1부터 시작하게 하는 부분

# 띄어쓰기 기준으로 라인을 나눠서 리스트 5에 넣음
# int형이 아니라 str형으로 들어가는 것 알아두기!!
for i in range(1, n+1):
    tri.append(input().split())

dp = []
dp.append([0])
# 0값을 넣어줘야 가져와서 쓸 수 있는거 명심하기!!

"""
i는 index가 1부터, j는 index가 0부터 시작
tmp : 모든 케이스에 동일하게 더해지는 tri[i][j] 말고
윗줄에서 최대값을 확인하여 저장하는 리스트
=> dp에서 값을 가져온다는거 명심하기!!

1)j==0 : 맨 왼쪽에서 타고 내려오는 경우
2)j==i-1 : 맨 오른쪽에서 타고 내려오는 경우
3)else : 그 외의 가운데를 계산하는 부분
"""
for i in range(1, n+1):
    tmp = []
    for j in range(0, i):
        if j==0:
            tmp.append(dp[i-1][0])
        elif j==i-1:
            tmp.append(dp[i-1][j-1])
        else:
            tmp.append(max(dp[i-1][j-1], dp[i-1][j]))
        tmp[j] = tmp[j] + int(tri[i][j])
        # 32line에서 최대값 + 현재 tri값 계산
        # tri는 str이라 int형으로 바꿔줘야하는 것 알아두기!!
    dp.append(tmp)
    
# dp 리스트 내에서 최대값 출력
print(max(dp[n]))