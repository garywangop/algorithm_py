Python的hash map是dictionary

# 创建一个dict
```
from collections import defaultdict
my_map = defaultdict(default_value)
```
Note： 当get一个key时，如果key不存在，那么就会运行def_value

我们常常可以直接写`my_map = defaultdict(int/list/str)`，当key不存在时return 0/[]/""

如果想自定义return的内容，可以：
1. 用lambda: `my_map = defaultdict(lambda: "abc")`
2. 把default_value写在外面。注意：这些写的话，default_value method传进去的时候不要加括号
```
def default_value():
    return "some default values"
    
my_map = defaultdict(default_value)
```

# 如果要添加一个item
`my_map['a'] = 1`或者`my_map.update({'a': 1})`

可以使用类似于List comprehension的方法快速创建一个dict。比如我想要创建一个dict, key = 小写字母a - z， value是0
```
my_map = {chr(i): 0 for i in range(ord('a'), ord('z'))}
```

# 要get一个item
`my_map['a']`或者`my_map.get('a')`
get到的value是immutable的
get还可以传入第二个变量，如果get的key不存在，那么就返回第二个变量
`my_map.get('c', 1)` -> 'c'如果不存在的话就返回1

用get比较靠谱，如果key 'a'不存在的时候，`my_map['a']`会直接报错，但是`my_map.get('a')`会返回None

iterate keys:
`for i in my_map.keys()`
iterate values: 
`for i in my_map.values()`

Remove a key: 
`my_map.pop(key)`


