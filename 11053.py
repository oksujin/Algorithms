N = int(input())
a = list(map(int,input().split()))
# 입력받은 값을 int형 list로 만들어줌
a.insert(0,0) # index를 1부터 하기위해 앞에 0을 넣어줌

dp = []
dp.append(0)# index를 1부터 하기위해 앞에 0을 넣어줌

for i in range(1, N+1):
    # 현재까지 최대 부분수열 길이
    # 새로운 i로 바뀔 때마다 초기화
    tmp = 0 
    """
    if 현재 저장된 원소(a[i])가 
    비교하는 원소(a[j])보다 더 크면
    저장되어있는 부분수열의 합(dp[j])를 넣어주고
    
    이전에 저장된 부분수열의 합(tmp)가 더 크면
    그 값을 넣어준다.

    마지막에 앞까지 저장된 부분수열의 합에
    새로 추가된 개수 1을 더해서 dp에 넣어준다.
    """
    for j in range(1, i):
        if a[i] > a[j]:
            tmp = max(tmp, dp[j])
    dp.append(tmp + 1)
       
print(max(dp))