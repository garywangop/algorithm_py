class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age


if __name__ == '__main__':
    p1 = Person("a", 1)
    p2 = Person("b", 2)
    print(p1 < p2)

    set = set()
    set.add(1)
    set.add('abc')
    print(set)
