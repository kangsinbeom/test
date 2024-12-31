# STACK

### _사용하는 경우_

1. 최근에 삽입한 데이터를 대상으로 무언가를 해야하는 경우 -> Stack

### _Stack 구현하기_

```
stack = []
max_size = 10

def isFull(stack):
    return len(stack) == max_size

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    if isFull(stack):
        print('스택이 가득핬습니다.')
    else:
        stack.append(item)
        print('데이터 추가 완료')
def pop(stack, item):
    if isEmpty(stack):
        print('스택이 비었습니다.')
    else:
        stack.pop(item)
        print("데이터 제거 완료")
```
