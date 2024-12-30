N = 5
stages = [2, 1, 2, 6 ,2, 4, 3, 3]

def solution(N, stages):
    challenger = [0] * (N + 2)
    for stage in stages:
        challenger[stage] += 1

    fails = {}
    total = len(stages)

    for i in range(1, N + 1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]
    return sorted(fails, key=lambda x : fails[x], reverse=True)

print(solution(N, stages))

"""
N번째 스테이지를 클리어한 사용자는 N +1에 위치한다
그 소리는 6스테이지 클리어한 사람은 7에 있다 당연하지
challenger라는 거는 이제 도전자가 위치한 곳을 나타내는 곳이구나.
그러면 0 ~ 7까지 나오는 경우엔는 N + 1까지로 해서 하면 되잖아 근데 0스테이지라는 것을 1스테이지로 표현하는 것보다 1을 1스테이지로 나타내는 것이
메모리를 0 하나만 사용하면서 내가 편하니깐 이렇게 하는 거다 라고 하는 거구나.
"""