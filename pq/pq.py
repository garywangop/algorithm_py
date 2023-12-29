import heapq

if __name__ == '__main__':
    l = [3, 5, 1, 2, 4]
    # heapq.heapify(l)
    heapq.heappush(l, 19)
    print(heapq.heappop(l))
    print(l)
