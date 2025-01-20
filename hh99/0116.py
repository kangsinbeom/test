import sys
# 뜨거운 붕어빵 브론즈 4

"""
문제 해설
주어진 입력값에 대해서 좌 우로 뒤집힌 모양으로 출력하는 것이다.
"""

# N,M = map(int, input().split(" "))

# def solution_1(string):    
#     return "".join(reversed(list(string)))


# for _ in range(N):
#     string = input()
#     print(solution_1(string))
"""
Runtime Error
sys.stdin.readline().strip() 을 사용했더니 runtimeError가 나왔다 왜 일까?
입력 데이터가 비어있거나 원하는 형식이 아닌 경우에 런타임에러를 유발할 수 있단다 그래서 if문으로
string이 비어있는지 확인하는 구문을 추가한 것을 보았다.
"""

# 기타 레슨 실버 1

"""
강의의 순서가 바뀌면 안된다 -> 순서 보장 혹시 stack?
특정 수학 공식을 알아야할 것 같다 단순 구현 문제가 아닌 것 같다.
어떻게 주어진 M개의 값이 근사치로 비슷한지 알아야한다.
이건 답을 보고 수학 공식을 참고해야할 듯
"""
N, M = map(int, input().split(" "))

