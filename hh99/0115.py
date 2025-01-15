# 문자열 반복 2675 브론즈 2

def solution_1():
    n = int(input())
    for _ in range(n):
        k, string = input().split(" ")
        k = int(k)
        answer = ''
        for i in string:
            answer += i * k
        print(answer)
# solution_1()

# 선분 위의 점 11663 실버 3

# 이분탐색 함수를 만들어보자.
def bineary_search(target, lst):
    start = 0
    end = len(lst) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return


def solution_2():
    spot, line = map(int, input().split(" "))
    lines = list(map(int, input().split(" ")))
    for _ in range(line):
        start, end = map(int, input().split(" "))
        #  이분탐색 먼저 오름차순의 배열을 만든다.
        array = sorted(lines)
        # index = 0
        # while start - lines[index] > 0:
        #     index += 1
        # while array[-1] - end > 0:
        #     array.pop()           
        # print(len(array[index:]))
        
        '''
        array_start, array_end, half = 0, len(array), len(array) // 2
        lastValue = array[array_end - 1]
        firstValue = array[array_start]

        while lastValue > end or firstValue < start:
            if array[half] > end:
                array = array[:half]
            elif end == array[half]:
                array = array[:half + 1]
            elif array[half] >= start:
                array = array[half:]
            else:
                print(array)
                break
        # 시불 이분탐색 제대로 공부하고 오자
        '''
        
         


        
        

solution_2()
# 시간초과가 뜬다 이분탐색 방법을 한 번 써서 해결을 해보자
