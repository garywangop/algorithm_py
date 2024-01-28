三元运算 ternary condition operation:

`
a = 1 if xxx else xxx
`

Tuple和list类似，区别是tuple is immutable

== vs is:
==比较的是value
is比较的是memory reference
Python中的None是唯一的，所以如果要check None的话，要用is来check

# Generate random number:
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

# enumerate
在for loop循环东西的时候，可以用enumerate method同时拿到index和item
```
for index, item in enumerate(string/list/etc.)
```
# 不可变object:
- int
- float
- str
- tuple
- frozenset

# inner function调用outer function的变量
inner function不可以直接调用outer function的不可变对象(int, float, str, tuple, frozenset)
```
def outer():
    a = 1
    def inner():
        a += 1
```
这样会报错。在执行a += 1操作的时候，这实际上创建了一个新的整数对象，并将a指向新对象。inner function无法指向新对象
如果想在inner调用outer的变量，有两种方法：
1. 使用self
```
   def outer():
    self.a = 1
    def inner():
        self.a += 1
```
2. 使用nonlocal
```
def outer():
    a = 1
    def inner():
        nonlocal a
        a += 1
```
# unpack:
```
a, b = [1, 2]
```
这样a和b可以被unpack成1和2
# Return 多个变量: lc1120
```return 1, 2```
