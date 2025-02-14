# 백준 2805번 나무 자르기 실버 2

def sol2805():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    start = 0
    end = max(trees)
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2
        for i in trees:
            if i > mid:
                total += i - mid
        if total < M:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result
sol2805()