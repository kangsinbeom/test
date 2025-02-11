# 이분탐색 뿌수기

"""
수찾기 1920 실버 4
"""

# 시간 복잡도를 만족해야하는 내용인 듯

def 이분탐색(array, goal):
    left = 0
    right = len(array) - 1
    # 여기서 / 만 하면 소수자리 값이 나오니깐 정수나누기 사용해야 함
    
    # 여기서 return문 사용되니깐 걍 탈출 조건을 안 넣었었는데 그러면 안된다고 한다.
    while left <= right:
        half = (right + left) // 2
        if array[half] > goal:
            right = half - 1
        elif array[half] < goal:
            left = half + 1
        elif array[half] == goal:
            return 1
    """
    기존에는 while문 안에 있었는데 도달할 수 없는 조건이라고 해서 while문 밖으로 옮김
    이러면 while문에서 만족하지 못했을 때 0을 return하도록 설계가 된다.
    """
    return 0


def sol1920():
    N = int(input())
    arrayN = sorted([int(x) for x in input().split()])
    M = int(input())
    arrayM = [int(x) for x in input().split()]
    for i in range(M):
        print(이분탐색(arrayN, arrayM[i]))

# sol1920()


"""
숫자 카드 2 10816 실버 4
"""

def sol10816():
    N = int(input())
    dict1 = {}
    """
    for i in [int(x) for x in input().split()]:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    """
    # 너무나도 간단하게 바뀔 수 있는 구문
    for i in map(int, input().split()):
        dict1[i] = dict1.get(i, 0) + 1
    arrayN = sorted(dict1.keys())
    result = []
    N = int(input())
    for j in map(int, input().split()):
        if 이분탐색(arrayN, j):
             result.append(str(dict1[j]))
        else:
            result.append('0')
    print(" ".join(result))

sol10816()