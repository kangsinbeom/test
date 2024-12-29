input = list(input())
listA = [0] * 26

for x in input:
    index = ord(x) - 97
    listA[index] += 1

print(*listA)
# list를 풀어서 출력하는 방법
