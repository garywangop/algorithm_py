`my_set = set()`

初始化：`my_set = {1, 2, 3}`

加一个元素:
`my_set.add(1)`

加多个元素:
`my_set.update([1,2,3])`

如果没有1的话会报错`my_set.remove(1)`
用discard来remove不会报错

检查元素是否存在:
`print(1 in my_set)`

遍历:
`for i in my_set`

放pair到set里时: LC1496
`my_set.add((x, y))`