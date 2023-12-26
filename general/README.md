三元运算 ternary condition operation:

`
a = 1 if xxx else xxx
`

Tuple和list类似，区别是tuple is immutable

== vs is:
==比较的是value
is比较的是memory reference
Python中的None是唯一的，所以如果要check None的话，要用is来check

Generate random number:
```
import random
print(random.random())
```
Or 
```
from random import random
print(random())
```
这样生成的是一个小于1的float，如果想要[1, 10]的正整数
```
import random
print(random.randInt(1, 10))
```

Python也是pass by reference，所以如果要把param传到别的地方去，不想修改原param的话，可以建立一个shallow copy: 
```
import copy
new_param = copy.copy(param)
```
如果param是个list，更简单的写法: `new_my_list = my_list[:]`