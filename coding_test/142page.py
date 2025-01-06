# 10진수를 받아 2진수로 변환하기

"""
10진수를 2진수로 표현하는 증명된 방법
10진수 N을 2로 나눈 나머지가 0이될 때까지 계속 2로 나눈다.
나누면서 나오는 몫을 순서대로 저장해서 출력한다.
"""
number = 12

def solution(number):
    stack = []
    while number:
        stack.append(number % 2)
        number //= 2
    
    return "".join([str(x) for x in stack])
    # return bin(number)[2:] 이렇게 풀면되지만 수학적으로 접근하는 방법도 있다.

print(solution(number))

# 