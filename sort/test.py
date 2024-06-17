from collections import Counter, defaultdict
# from collections.abc import Set


# from typing import Set


def a():
    s = "cccbba"
    cnt = Counter(s)

    def custom_sort(item):
        return cnt[item]

    sss = sorted(s, key=custom_sort, reverse=True)
    return "".join(sss)


if __name__ == '__main__':
    s = "aabbcc"
    ss = sorted(s, reverse=True)
    print(list(s))
    print("".join(ss))
    print(f"run a: {a()}")
    m = defaultdict(set)
    m['a'].add(1)
    m['a'].add(2)
    print(m)
