# 몸풀기 문제

"""
조건:
정수 배열의 길이는 2 이상 10^5 이하
정수 배열의 각 데이터 값은 -100,000 ~ 100,000
정수를 배열해서 반환하는 함수를 만들어라.
"""
# Q.1 문제를 받고 풀기 부분에서 제한 시간이 3초라면 O(N^2)을 사용하지 못한다는데 어떻게 구했누?

def solution(lst):
    return sorted(lst)
answer = solution([1, 3, 2])
print(answer)

"""
느낀점:
간단하게 배열하는 sort()를 아는지에 대한 문제인데 원본배열을 변화시키는 lst.sort()를 사용했기에
위와 같이 나온다.
def solution(lst):
    return sorted(lst)
이것도 가능

chatGPT왈 list라고 하지말고 lst라고 해라!
"""