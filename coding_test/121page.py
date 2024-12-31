dirs = 'ULURRDLLU'

def move_location(x, y, dir):
    if dir == 'U':
        x, y = x, y + 1
    elif dir == 'D':
        x, y = x, y - 1
    elif dir == 'L':
        x, y = x - 1, y
    elif dir == 'R':
        x, y = x + 1, y
    return x, y

def is_valid_move(x, y):
    return -5 <= x < 5 and -5 <= y < 5


def solution(dirs):
    x, y = 0, 0
    result = set()
    for i in dirs:
        nx, ny = move_location(x, y, i)
        if not is_valid_move(nx, ny):
            continue
        result.add((x, y, nx, ny))
        result.add((nx, ny, x, y))
        x, y = nx, ny
    return len(result) // 2

print(solution(dirs))

