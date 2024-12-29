a, b = input().split()
a = int(a)
b = int(b)

print(a + b)

a, b = map(int, input().split())

print(a + b)

# 동일한 결과값을 보여준다
# map 함수
# 여러 개의 입력값을 동시에 처리할 때 유용한 함수로 map(함수, 입력값들)의 형태를 띈다

# list 함수
# 여러 개의 값을 리스트에 담아서 출력할 수 있게 해준다 list(입력값들)의 형태를 띈다

# Question: 주석하는 방법 뭐지??

# sep, end 파라미터
# 출력 시 사용되는 파라미터 sep은 기본 값이 공백이며, end는 기본값이 \n이다
print(a + b, sep=", ")
print(a + b, end=" ")

# 빠른 입력하기
# input의 경우에는 많은 입력을 받을 경우에는 상당히 느리기에 시간초과 되는 경우도 있다
# 문자를 받는경우에는 enter까지 남아있기에 rstrip을 사용해야 한다.
import sys
input = sys.stdin.readline
a = input().rstrip()
print(a)

# string 모듈
# 대문자와 소문자를 쭉 가져오는 방법
import string
string.ascii_lowercase
string.ascii_uppercase

# 비트 wise 연산자
# 이진수 형태로 저장되어있는 내부 값을 비트 단위로 연산할 수 있게끔 해주는 연산자