# 백준 아 맞다 마늘 브론즈 2

"""

"""
def 이분탐색(lst1, lst2):
    start = 0
    end = len(lst1) - 1
    while start <= end:
        half = (end + start) // 2
        if half >= len(lst2) or lst1[half] != lst2[half]:
            end = half - 1
        else:
            start = half + 1
    return start


def solution1():
    N = int(input())
    total = sorted(input().split(" "))
    use = sorted(input().split(" "))
    return total - use
print(solution1())