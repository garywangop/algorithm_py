在Python中，可以用list来表示queue/stack，也可以用deque来表示queue/stack
用deque比较好，因为用list表示的queue在pop是不efficient，pop完之后剩下的item要往前移

1. 用list
queue：

add: `l.append(item)`
pop: `l.pop(0)`

stack:

add: `l.append(item)`
pop: `l.pop()`

2. 用deque
先import: 
```
from collections import deque
dq = deque()
```
可以直接传list到deque里初始化: `dq = deque([1,2,3])`

queue:
add: `dq.append(item)`
pop: `dq.popleft()`

stack:
add: `dq.append(item)`
pop: `dq.pop()`

判断deque是不是empty，可以直接用`len(dq)`，也可以用`if dq`