

def solution():
    len = int(input())
    string = input()
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sum = 0
    for i in range(len):
        index = alpha.index(string[i])
        sum += (index + 1) * (31 ** i)         
    return sum

print(solution())