import random


class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        self.list[self.map[val]] = self.list[len(self.list) - 1]
        self.map[self.list[len(self.list) - 1]] = self.map[val]
        self.list.pop()
        self.map.pop(val)
        return True

    def getRandom(self) -> int:
        return self.list[random.randint(0, len(self.list) - 1)]


if __name__ == '__main__':
    sol = RandomizedSet()
    sol.insert(0)
    sol.insert(1)
    sol.remove(0)
    sol.insert(2)
    sol.remove(1)
    sol.getRandom()