import sys

test_n = int(input())

a, b, c, d = [sys.stdin.readline().split('\n')[0] for _ in range(test_n * 4)]

    

def solution(a, b, c, d):
    a, b, c, d = int(a), set(map(int, b.split(" "))), int(c), list(map(int, d.split(" ")))
    print(a, b, c, d)
    for i in d:
        if i in b:
            print(1)
        else:
            print(0)

solution(a, b, c, d)