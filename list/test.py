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
    # print(l1 == l2)
    l = [1,2,3]
    m = Counter(l)
    # print(m)
    l3 = [0] * 3
    print(l3)

    l4 = [1,2,3]
    print(sum(l4))

    t = (1,2, 3)
    print(t[0])

    print([[0]] * 3)
    print([[0] for _ in range(3)])
    print([[0] * 3])

    a = b = []
    a.append('a')
    print(b)

    a, b, c = [1, 2, 3], [4, 5, 6], [7, 8, 9]
    l = [[x, y, z] for x in a for y in b for z in c]
    print(l)

    l1 = [1,2,3]
    l2 = [4,5,6]
    print(l1 + l2)