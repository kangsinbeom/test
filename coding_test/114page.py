#행렬의 곱셈
"""
행렬의 곱셈을 구하는 방법은 알고 있어야 한다.
arr1, arr2가 주어졌을 때
행렬의 크기를 구하는 방법: arr1 = m * n, arr2 = n, p라면 arr3 = m * p 첫번째 열의 개수와 두번째 행의 개수가 같아야 하는 조건!
값을 구하는 방법은 (i, j)에서 i는 arr1의 행과 arr2의 열을 곱해서 다 더하면 된다.
ex) [[2, 3, 2], [4, 2, 4], [3, 1, 4]]랑 [[5, 4, 3], [2, 4, 1], [3, 1, 1]]이 두 배열이 주어졌을 때
2 * 5 + 3 * 2 + 2 * 3해서 22가 첫번째 (0, 0) 위치의 값이 된다
이는 arr1[0]과 arr2의 배열의 첫번째 값을 곱해서 더한 값이다. 
"""

def solution(arr1, arr2):
    #행렬을 각각 구해보자 여기서 r1과 c2는 같은 값이다.
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])
    result = [[0] * c2 for _ in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += arr1[i][k] * arr2[k][j]
    return result
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1]]))

