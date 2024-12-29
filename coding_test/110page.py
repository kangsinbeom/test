# mock_answer = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# patterns = ['12345', '21232425', '3311224455']
# def solution(answer, str):
#     str_lst = [int(x) for x in str]
#     str_len = len(str_lst)
#     index = 0
#     count = 0
#     result = 0
#     while len(answer) > (str_len * count) + index:
#         if (index + 1 > len(str_lst)):
#             index = 0
#             count += 1
#         if str_lst[index] == answer[(str_len * count) + index]:
#             result += 1
#         index += 1
#     return result

# results = [solution(mock_answer, x) for x in patterns]
# max = max(results)
# indices = [index + 1 for index, value in enumerate(results) if value == max]
# print(indices)
answers = [1, 2, 3, 4, 5]
patterns = [
    [1, 2, 3, 4, 5],
    [1, 2, 1, 2,]
]
scores = [0] * 3
for i, answer in enumerate(answers):
    for j, pattern in enumerate(patterns):
        if answer == pattern[i % len(pattern)]:
            scores[j] += 1