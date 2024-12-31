# 짝이 있는 경우인데 이게 정상적인지 알 수 있는 경우
str = '()())()()()()()()'

def valid_str(str, stack):
    if str == '(':
        stack += 1
    if str == ')':
        stack -= 1
    return stack

def solution(str):
    stack = 0
    for i in str:
        stack = valid_str(i, stack)
        print(stack)
        if stack < 0:
            break
    return stack >= 0

print(solution(str))