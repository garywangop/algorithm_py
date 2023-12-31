from collections import Counter, defaultdict
from typing import List


def test_map():
    my_map = {
        "a": 1,
        "b": 2
    }
    operation(my_map)
    print(f"check my_map: {my_map}")


def operation(map):
    value = map.get('a')
    value -= 1
    print(map)


def test():
    l = [1 for _ in range(3)]
    test2(l)


def test2(l: list[int]):
    ll = l
    ll[0] += 1
    print(ll)
    print(l)


def default_value():
    return "some default values"


if __name__ == '__main__':
    my_map = {chr(i): 0 for i in range(ord('z'), ord('a') - 1, -1)}
    print(my_map)
    s = "12341"
    print(s.count("23"))
    # m = defaultdict(lambda: "abcd")
    m = defaultdict(default_value)
    print(m['abc'])
    print(m)

    if "a" not in m:
        print("no")
    else:
        print("yes")