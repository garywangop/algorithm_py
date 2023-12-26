from collections import deque

if __name__ == '__main__':
    dq = deque([1,2,3])
    dq.popleft()
    print(dq)