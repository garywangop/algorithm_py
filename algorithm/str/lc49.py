from collections import defaultdict
from typing import List

'''
这题主要是注意：
1. str可以直接被sort
2. dict的key需要hashable，不能直接把list作为dict的key，需要把list变为str然后作为map的key
'''
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    letters, res = defaultdict(list), []

    for i in strs:
        s = str(sorted(i))
        letters[s].append(i)

    return list(letters.values())
