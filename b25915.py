# start = input()

# # 받은 input을 password앞에 붙인다면 if-else문이 필요가 없다
# password = start + 'ILOVEYONSEI'
# # password = 'ILOVEYONSEI'

# current = ord(start)
# answer = 0

# for i in password:
#     answer += abs(ord(i) - current)
#     current = ord(i)

# print(answer)

# 또 다른 풀이

c = input()
a = c
n = len(a)
res = 0

for i in range(1, n):
    x = ord(a[i - 1])
    y = ord(a[i])
    res += abs(x - y)

print(res)