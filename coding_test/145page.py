# 괄호 회전하기

"""
2개의 함수가 필요해보인다.
1. 괄호가 올바르게 구성되어있는 올바른 괄호 문자열인지 구분하는 함수
2. 몇 칸 이동해야 하는지 구하는 함수

예전에 풀었던 문제를 합치는 거니깐 기억을 더듬어보자
""" 

string = "[](){}"
def solution(string):
    stack = {
        'small': 0,
        'middle': 0,
        'large': 0
    }
    while string:
        if string[0] == '(':
            stack['small'] += 1
        string.pop(-1)
    return 

print(solution(string))