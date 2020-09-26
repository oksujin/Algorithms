##### 조건문 #####
## 기본구조 
# if ~ elif ~ else : 들여쓰기는 스페이스바 4번이 표준

## pass
# 조건문에서 아무것도 처리하고 싶지 않을 때 사용
score = 85

if score >= 80 :
    pass # pass했기 때문에 아무 처리하지 않고 넘어간다.
elif score >= 70 :
    print("B학접입니다")
else : 
    print("C학점입니다")

print("프로그램을 종료합니다.\n")

## 조건부 표현식(Conditional Expression)
result = "Sucess" if score >=80 else "Fail"
print(result)

## list 컴프리헨션에서 사용된다.
# 특정한 값의 원소를 모두 제거하는 방법
# remove_set을 지정하고, 여기 포함되어있지 않을 때만
# 새로운 리스트 변수에 넣어주도록 한다.
a = [1, 2, 2, 3, 3, 4, 5, 5, 6]
remove_set = [3, 5]

# 리스트 컴프리헨션 사용해서
# i가 a에 포함되지 않을 때만, array에 담아준다.
array = [i for i in a if i not in remove_set]
print(array, '\n')

####################################################
##### 반복문 #####
## 기본구조
# 1. while문
# 2. for문

## while문
# 조건문이 참일 떄에 한해서 반복적으로 코드 수행
i = 1
result = 0

while i <= 9 :
    if i % 2 == 1 :
        result = result + i
    i = i + 1

print("1~9까지 홀수만 더한 값 = ", result)


## for문
 
# 위와 동일한 예시
result = 0
for i in range(1, 10) :
    if i%2 == 1 :
        result = result + i
        
# range에 숫자 1개만 쓰면, 자동으로 시작값은 0
print("1~9까지 홀수만 더한 값 = ", result, "\n")

# continue : 반복문 안에서 continue를 만나면 반복문 처음으로 돌아간다 
# 2번, 4번 학생은 블랙리스트라 점수가 놓아도 불합격
scores = [90, 85, 77, 65, 97]
blacklist = [2, 4]

for i in range(1, 6) :
    if i in blacklist :
        continue
    if scores[i-1] >= 80 :
        print (i, "번 학생 통과입니다.")

####################################################
##### 함수 #####
# 함수란 동일한 알고리즘을 반복적으로 수행해야할 때, 코드를 함수화

## 함수 밖의 변수 데이터를 변경해야 하는 경우 사용법
# 전역변수 a
a = 0

def func():
    global a # 전역변수 a를 지역변수로 사용하겠다는 의미
    a += 1

for i in range(10):
    func()

print("\n함수 실행 결과 = ", a, "\n")

## 람다 표현식 (lambda express)
# 함수를 한 줄에 작성하는 방법
def add(a, b):
    return a+b

print("일반적인 함수 = ", add(3,7))
print("람다 표현식으로 구현한 add() 메서드 = ", (lambda a, b : a+b)(3, 7), "\n")

####################################################
##### 입력 #####

## (1) 입력을 위한 전형적인 소스코드
# 입력 예시 : 학생의 성적 데이터가 주어지고 이를 내림차순으로 정렬한 결과를 출력 하라는 문제
# 5
# 65 90 75 34 99

# 데이터의 개수 입력
print("\n데이터의 개수를 입력하시오 : ")
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
# input()으로 입력받은 문자역을 split()을 이용해서 공백으로나눈 리스트로 변환
# 그 후, map을 이용하여 해당 리스트의 모든 원소에 int 함수 적용
# 치종적으로 그 결과를 list로 다시 바꿈으로서 입력받은 문자열을 띄어쓰기로 구분해 각각 숫자형으로 저장
print("\n모든 데이터를 개수에 맞춰 입력하시오 :")
data = list(map(int, input().split()))

data.sort(reverse=True)
print("\n입력예시 : ", data)

## 참고 : map이란
# map은 리스트의 요소를 지정된 함수로 처리해주는 함수
# 기존 리스트를 변경하지 않고 새 리스트를 생성한다.

## (2) 적은 수의 데이터 입력
# 입력 예시 : 3개의 데이터만을 공백을 기준으로 받기
print("\n3개의 데이터를 공백을 기준으로 입력하시오 : ")
n, m, k = map (int, input().split())
print(n, m, k)

## (3) 입력 개수가 많은 데이터를 입력받는 법
# input() 함수는 동작속도가 느려서 시간 초과가 될 수 있다.
# 이럴 때는 파이썬의 sys 라이브러리의 함수를 사용한다.
# input() 함수와 같이 한 줄씩 입력받기 위해 사용한다.
import sys

# 한줄 입력 후, rstip() 함수를 꼭 호출해야 한다.
# readline()으로 입력하면입력 후 엔터가 입력되는데, 이걸 제거하기 위해 필요하다
print("\n데이터를 입력하세요 :")
data = sys.stdin.readline().rstrip()
print(data)

####################################################
##### 출력 #####
## print : 출력 후 줄바꿈을 수행하기 때문에, 사용할 때마다 줄이 변경된다.
## 문자열과 숫자를 동시에 출력하고 싶은 경우 방법 4가지
answer = 7
print("정답은 " + str(answer) + "입니다.")
print("정답은 ", str(answer), "입니다.")
print("정답은 ", answer, "입니다.")
print(f"정답은 {answer} 입니다.")