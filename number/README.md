Python的数字类型有int, float, complex

Python是没有infinite int的，要表示无限大的话只能用float

`
a = float("inf")
`

或者`a = math.inf`，需要import math

除法用'/'的时候，如果不能整除会自动变成float
如果不想变成float，用'//'