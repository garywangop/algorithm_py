Python的数字类型有int, float, complex

Python是没有infinite int的，要表示无限大的话只能用float

`
a = float("inf")
`

或者`a = math.inf`，需要import math

除法用'/'的时候，如果不能整除会自动变成float
如果不想变成float，用'//'

指数表示方法 a^b: `a ** b`

计算平方根的话，用`math.sqrt(x)`，注意，平方根输出的一定是float。所以如果要判断计算结果是否为整数，要用`res.is_integer()`，如果为整数，就可以把计算结果转换成整数并输出`int(res)`
直接返回`math.sqrt(x).floor()`的话，可以用`math.isqrt(x)`