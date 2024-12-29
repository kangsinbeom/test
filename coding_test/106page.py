# 배열 받고, 중복값 제거, 내림차순

def solution(arr):
    newArr = list(set(arr))
    newArr.sort(reverse=True)
    return newArr

print(solution([3, 4, 2, 1, 1, 1, 1]))

"""
내림차순 정렬하는 방법에서 sort()가 가진 매개변수가 reversed가 아닌 reverse인 것을 기억하자!
set()을 통해서 만들어지는 결과물을 list로 감싼다라...
"""
