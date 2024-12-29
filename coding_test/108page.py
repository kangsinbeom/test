
def solution():
    numbers = [5, 4, 3, 2, 1]
    result = []
    new_numbers = sorted(set(numbers))
    print(new_numbers)
    for i in range(len(new_numbers)):
        for j in range(i + 1, len(new_numbers)):
            sum = new_numbers[i] + new_numbers[j]
            if sum not in result:
                result.append(sum)
    return result
print(solution())

"""
이중 반복문을 통해서 지금 숫자를 제외한 나머지를 다 더하는 방식으로
값이 result 안에 없으면 추가 있으면 continue를 해볼까?
"""
