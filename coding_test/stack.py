import myReadline
        
# 문제 10 괄호 회전하기
def solution_10(string):
    result = 0
    s = list(string)
    for i in range(len(s)):
        stack = [] # 빈배열은 False 값이다.
        for j in range(len(s)):
            if not stack:
                stack.append(s[j])
            else:
                if s[j] == ']' and stack[-1] == '[': stack.pop()
                elif s[j] == '}' and stack[-1] == '{': stack.pop()
                elif s[j] == ')' and stack[-1] == '(': stack.pop()
                else: stack.append(s[j])

        if not stack:
            result += 1
        s.append(s.pop(0))
        
    return result

# examples_10 = myReadline.get_example("stack_10.txt")

# for example in examples_10.values():
#     print(solution_10(example))

def solution_11(string):
    stack = []
    for i in string:
        if len(stack) != 0 and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    return int(not len(stack) > 0)

# examples_11 = myReadline.get_example("stack_11.txt")

# for example in examples_11.values():
#     print(solution_11(example))
    

# examples_11 = myReadline.get_example("stack_11.txt")

# for example in examples_11.values():
#     print(solution_11(example))

def solution_12(prices):
    n = len(prices)
    answer = [0] * n
    stack = [0]
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = n - 1- j                
    return answer

# examples_12 = myReadline.get_example("stack_12.txt")

# for example in examples_12.values():
#     lst = example.split(" ")
#     int_lst = [int(x) for x in lst]
#     # print(solution_12(int_lst))
#     print(solution_12(int_lst))


# 문제 13 크레인 인형 뽑기 게임
def solution_13():
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]
    result = 0
    stack = []
    for move in moves:
        for i in range(len(board)):
            dol = board[i][move - 1]
            if dol != 0:
                if stack and stack[-1] == dol:
                    print(stack, stack[-1], dol)
                    stack.pop()
                    result += 2
                stack.append(dol)
                board[i][move - 1] = 0
    return result
# print(solution_13())

n = 8
k = 2
cmd = ["D 2", 'C', "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]

def solution_14(n, k, cmd):
    result = "O" * n
    delete = []
    for i in range(len(cmd)):
        if len(cmd[i]) > 1:
            action, count = cmd[i].split(" ")
            if action == "D":
                k += int(count)
            else: 
                k -+ int(count)
        else:
            if cmd[i] == "C":
                if k == n:
                    result = result[:-1] + "X"
                else:
                    result = result[:k] + "X" + result[k + 1:]
                delete.append(k)
            else:
                result = result[:delete[-1]] + "O" + result[delete[-1] + 1:]
                delete.pop()
    return result
print(solution_14(n, k, cmd))