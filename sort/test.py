from collections import Counter


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
