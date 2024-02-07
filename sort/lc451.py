from collections import Counter


class Solution:
    # custom comparator
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)

        def custom_sort(x):
            return (-cnt[x], x)

        return "".join(sorted(s, key=custom_sort))

    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)

        return "".join(sorted(s, key=lambda x: (-cnt[x], x)))
