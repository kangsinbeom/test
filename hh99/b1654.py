import sys

# 가지고 있는 랜선의 개수 k , 필요한 랜선의 개수 n

k, n = map(int, input().split(" "))
lines = []
for _ in range(k):
    line = int(input())
    lines.append(line)

def solution(lines, n):
    
    start, end = 1, max(lines)
    while start <= end:
        mid = (start + end) // 2
        line_cnt = 0
        for line in lines:
            line_cnt += line // mid
        if line_cnt >= n:
            start = mid + 1
        else:
            end = mid - 1
        pass
        
    return end

print(solution(lines, n))
# 239 ~ 