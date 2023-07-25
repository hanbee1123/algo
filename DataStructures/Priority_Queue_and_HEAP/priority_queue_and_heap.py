"""
Queue: FIFO

Priority Queue: 우선순위가 가장 높은 값이 먼저 추출.


Priority Queue:

구현 1: using list:
    enqueue = O(1)
    deque = O(n)

구현 2: using list but sort after enque according to priority 
    enqueue = O(nlogn)
    deque = O(1)

구현 3: using heap (완전 이진 트리)
    enqueue = O(log n)
    deque = O(log n)


"""