import sys
# stack 실버 4
def beginner():
    N = int(input())
    stack = []
    for _ in range(N):
        action = sys.stdin.readline().split()
        
        # push
        if len(action) > 1:
            _, value = action
            stack.append(value)
        
        #  top
        elif 'top' in action:
            if len(stack) == 0:
                print(-1)
            else: print(stack[len(stack) - 1])
        
        # size
        elif 'size' in action:
            print(len(stack))
        
        # empty
        elif 'empty' in action:
            print(int(len(stack) == 0))

        # pop
        else:
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
beginner()
    