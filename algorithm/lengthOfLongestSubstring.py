def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0

    l, r, res, my_set = 0, 1, 1, set()
    my_set.add(s[l])

    while r < len(s):
        if s[r] not in my_set:
            res = max(res, r - l + 1)
            my_set.add(s[r])
            r += 1
        else:
            while l < r and s[l] != s[r]:
                my_set.remove(s[l])
                l += 1

            l += 1
            r += 1

    return res


if __name__ == '__main__':
    s1 = 'abcabcbb'
    s2 = 'pwwkew'
    print(lengthOfLongestSubstring(s1))
    print(lengthOfLongestSubstring(s2))

    my_set = {1, 2, 3, 3}
    my_set.add(3)
    print(my_set)

