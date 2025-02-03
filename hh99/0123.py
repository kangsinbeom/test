# 백준 31562 전주 듣고 노래 맞히기 브론즈 1

def solution1():
    N, M = [int(x) for x in input().strip().split(" ")]
    obj1 = {}
    result = ''
    for _ in range(N):
        info = input().strip().split(" ")
        obj1[info[1]] = "".join(info[2:5])
    for _ in range(M):
        correct = 0
        target = ''
        question = input().replace(" ", "")
        for targetKey, targetValue in obj1.items():
            if targetValue == question:
                target = targetKey
                correct += 1
        if correct == 0:
            print("!")  
        elif correct > 1:
            print("?")  
        else:
             print(target)  
solution1()
