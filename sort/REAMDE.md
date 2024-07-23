当我要sort一个list时，list = [[1,2], [2,3], [2, 4]]

in place sort: `list.sort()`
这样会根据item的第一个元素从小到大排列
如果要从大到小sort: `list.sort(reverse=True)`

如果我要不想in place sort，想要sort完之后return一个新的list:
`new_list = sorted(list)`
如果要从大到小sort: `new_list = sorted(reverse=True)`

如果我想要自定义排序的方法，不管是使用lambda还是在别的地方写排序方法，目标都是要把排序规则通过tuple传到sort方法里的key里去

简单的sort用lambda就好了：
升序+降序

`my_list = [[7, 4], [8, 7], [9, 9], [9, 7]]`

# 使用lambda函数定义排序规则，先按a升序，如果a一样的话，就按b降序
`sorted_list = sorted(my_list, key=lambda item: (item[0], -item[1]))`

升序+升序

`my_list = [[7, 4], [8, 7], [9, 9], [9, 7]]`

# 使用lambda函数定义排序规则，先按a升序，如果a一样的话，就按b升序
`sorted_list = sorted(my_list, key=lambda item: (item[0], item[1]))`

稍微复杂一点的，把key写出去，用helper function弄出一个tuple

# 定义排序规则，先按a升序，如果a一样的话，就按b降序
```
def custom_sort(item):
    return (item[0], -item[1])
```

# 使用sorted函数进行排序，key参数指定排序规则
`sorted_list = sorted(my_list, key=custom_sort)`

# 例子
一个list里都是str，按以下规则排序：
1. 按str的长度从小到大
2. 长度一样的话按字母顺序

写法：
`sorted(l, key=lambda x: (len(x), x))`

或者(使用cmp_to_key，这样的原始写法更加容易理解):
```
from functools import cmp_to_key

def custom_compare(x, y):
    # 先按长度排序，长度相同则按字典顺序排序
    len_diff = len(x) - len(y)
    if len_diff != 0:
        return len_diff
    else:
        return 1 if x > y else -1

sorted_list = sorted(my_list, key=cmp_to_key(custom_compare))
```

# dict的话，能直接用sorted去sort dict的key

