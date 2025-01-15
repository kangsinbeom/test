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
def solution_16(progresses, speeds):
    result = []
    while progresses:
        
        pass
    return result
# print(solution_16([93, 30, 55], [1, 30, 5]))

def solution_17():
    cards1 = deque(['i', 'drink', 'want'])
    cards2 = deque(['water', 'to'])
    goal = deque(['i', 'want', 'to', 'drink', 'water'])
    while goal:
        if goal[0] == cards1[0]:
            goal.popleft()
            cards1.popleft()
        elif  goal[0] == cards2[0]:
            goal.popleft()
            cards2.popleft()
        else:
            return 'No'
    
    return 'Yes'

print(solution_17())