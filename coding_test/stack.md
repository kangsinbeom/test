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

### 문제

- 문제 10 괄호 회전하기.
  ![스크린샷 2025-01-03 오전 8 36 47](https://github.com/user-attachments/assets/86091ab7-41eb-437c-9535-caeb1437a8ea)
