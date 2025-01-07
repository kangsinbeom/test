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


def solution_12(array):
    
    return array



examples_12 = myReadline.get_example("stack_12.txt")

for example in examples_12.values():
    print(list(example))
