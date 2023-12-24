if __name__ == '__main__':
    my_set = set()
    my_set.add(1)
    my_set.update([1, 2, 3])
    my_set.discard(4)
    print(my_set.add(4))

    print(my_set)
