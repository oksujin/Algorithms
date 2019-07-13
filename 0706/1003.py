#백준 1003번 피보나치 함수

T = int(input())
N = []

for i in range(0, T):
    N.append(int(input()))

dp0 = []
dp1 = []

"""
n==0일 때 0은 1번, 1은 0번 나오고
n==1일 때 0은 0번, 1은 1번 나온다
"""
dp0.append(1) 
dp0.append(0)

dp1.append(0)
dp1.append(1)

#0부터 최대값 40까지의 각각 0의 개수와 1의 개수 계산
for i in range(2, 40):
    dp0.append(dp0[i-1]+dp0[i-2])
    dp1.append(dp1[i-1]+dp1[i-2])

#해당하는 개수 출력
for i in N:
    print(dp0[i], dp1[i])
 
