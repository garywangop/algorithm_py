Python的hash map是dictionary
如果要添加一个item
`my_map['a'] = 1`或者`my_map.update({'a': 1})`

要get一个item
`my_map['a']`或者`my_map.get('a')`

用get比较靠谱，如果key 'a'不存在的时候，`my_map['a']`会直接报错，但是`my_map.get('a')`会返回None

iterate keys:
`for i in my_map.keys()`
iterate values: 
`for i in my_map.values()`
