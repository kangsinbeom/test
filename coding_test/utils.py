import time
# 시간 측정 함수
def measure_time(func, arr):
    start_time =  time.time()
    result = func(arr)
    end_time = time.time()
    return end_time - start_time, result
# 이거는 배열이랑 같이 줘야하니깐 함수만 집어넣어도 걸리는 시간 측정하도록 리팩토링할 줄 알아야 함...