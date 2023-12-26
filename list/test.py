from collections import Counter

def iterate1():
    arr = [1, 2, 3]
    for i in range(len(arr)):
        print(arr[i])


def iterate2():
    arr = [1, 2, 3]
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i])


if __name__ == '__main__':

    l1 = l2 = [0 for _ in range(27)]
    s, t = "cat", "rat"
    for i in range(len(s)):
        l1[ord(s[i]) - ord('a')] += 1
        l2[ord(t[i]) - ord('a')] += 1
    print(l1 == l2)
    l = [1,2,3]
    m = Counter(l)
    print(m)


