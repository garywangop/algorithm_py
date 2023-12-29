优先队列有两种
1. heapq: `import headq`
2. PriorityQueue: `from queue import PriorityQueue`

两者的区别是:
1. heapq是module不是class，这个module里有堆操作函数。PriorityQueue是一个class，里面除了堆操作，还有很多别的东西
2. heapq lightweight，其实就是一个普通的list
3. PriorityQueue是线程安全的

时间复杂度:
- heapify的时间复杂度是O(n)
- 添加n个元素到优秀队列里时间复杂度是O(n log n)
- pop一个元素是O(log n)

刷题的时候应该用heapq比较合适

heapq的add, pop, peek, isEmpty:
`minHeap = [] # 从这里也可以看出，heapq就是对一个list不断的操作`
- add: `heapq.heappush(minHeap, num)`
- pop: `heapq.heappop(minHeap)` -> 会return被pop掉的元素
- peek: `minHeap[0]`
- isEmpty: `if not minHeap`

Python中不管是heapq还是PriorityQueue都没有最大堆，要用最大堆的话那就只能在添加元素的时候全部取负数，在pop的时候再取反
