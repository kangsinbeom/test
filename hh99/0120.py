# 백준 27160 할리갈리 브론즈 2

'''
종을 쳐야하는 상황을 알아보자. 일단 같은 특정 value의 key가 5가 되면 ok라는 느낌이니깐
set을 이용해서 문제를 풀어보자 -> 아니다 이거 set을 이용하면 리스트에서 중복값을 없애는 느낌으로 써야하고
이때는 dict를 사용해서 key value로 나타내보자
'''

N = int(input())

def solution_1(N):
    dict_1 = {}
    for i in range(N):
        fruit, amount = input().split(" ")
        amount = int(amount)
        keys = dict_1.keys()
        if fruit in keys:
            dict_1[fruit] += amount
        else:
            dict_1[fruit] = amount
    if 5 in dict_1.values(): 
        return 'YES' 
    return 'NO'

# print(solution_1(N))

# 백준 1260 DFS 와 BFS 실버 2

