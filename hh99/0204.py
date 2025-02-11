import sys
input = sys.stdin.readline
# 막대기 브론즈 2

def begginer():
    N = int(input())
    sticks = set()
    count = 0
    
    for i in range(N):
        curr_stick = int(input())
        sticks.add(curr_stick)
    last_stick = sticks[-1]
    for i in sticks:
        if i >= last_stick:
            count += 1
    return count

print(begginer())