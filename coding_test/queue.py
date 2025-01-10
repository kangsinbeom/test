from collections import deque

# 문제 15 요세푸스 문제
def solution_15(n, k):
    people = deque(range(1, n + 1))
    count = 1
    
    while len(people) > 1:
        if (count == k):
            people.popleft()
            count = 1
        else:
            people.append(people.popleft()) 
            count += 1
        print(people)
    return people.popleft()

# print(solution_15(5, 2))

# 문제 16 기능 개발
def solution_16():
    
    return
print(solution_16())