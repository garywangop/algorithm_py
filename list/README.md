Python的list是非常flexible的，可以添加不同type的item到list里
array需要import，array中的item需要是同一type

i = 1
如果想要i = i + 1
`i += 1`

max(1,2,3,4,5) -> 5

add一个item到list里去可以用append或者extend，我觉得用append比较靠谱

append是把whatever一大坨加到list里去

```
l1 = [1, 2, 3]
l2 = [4,5]
l1.append(l2) 
print(l1)
```

--> `[1,2,3, [4,5]]`

extend会自动iterate加进去的item，然后一个个添加
```
l1 = [1,2,3]
l2 = abc
l1.extend(l2)
print(l1)
```
--> `[1,2,3,'a','b','c']`

建立一个matrix with row and col (LC 867)
```
matrix = [[0] * col for _ in range(row)]
```

List comprehension:
`newlist = [item expression for item in iterable if condition == True]`
例子：
```
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits if 'a' in x]
```


