count 1s in a string (e.g. "001100"")

`ones = s.count("1")`

substring [start, end): `s[start: end]`

split:
```
s = 'a,b,c'
s.split(',')
```

string comparison: 
s1 = '0', s2 = '00'
Python是可以直接比较这样的string的。
此时s2 > s1，因为先比较第一位，两个都是0；再比较第二位，s1没有第二位，那s2就比较大

a = 'abc'，我可以用a * 3直接得到一个'abcabcabc'的string

对一个string使用Count方法，可以生成一个key = s[i], value = s[i] count的dict
```
from collections import Counter
my_map = Counter('abc')
```

如何取chr的ASCII：`ord('c')`

