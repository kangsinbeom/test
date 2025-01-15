import time
# 시간 측정 함수
def measure_time(func, arr):
    start_time =  time.time()
    result = func(arr)
    end_time = time.time()
    return end_time - start_time, result
# 이거는 배열이랑 같이 줘야하니깐 함수만 집어넣어도 걸리는 시간 측정하도록 리팩토링할 줄 알아야 함...

#  이분 탐색 함수 (반복문)
def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return