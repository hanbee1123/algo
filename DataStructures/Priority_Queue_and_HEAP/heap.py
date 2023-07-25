"""
heap 자체가 완전이진 트리기 때문에
우선순위 큐가 필요하면 heap을 구현하면 됨.

완전 이진 트리의 특성:
+++- 완전 이진 트리는 list로도 표현이 가능하다.

                        트리의 형태:

                                        1                 ------- level 0
                                3               2         ------- level 1
                            4       5       9       6     ------- level 2
                        8   7                           ------- level 3

                        리스트로 표현할 경우:
                        [1,3,2,4,5,9,6,8,7]


parent = i
left child = 2i+1
right child = 2i+2

child = 1
parent = (i-1)//2


min_heap = 부모 노드의 값이 자신 노드의 값보다 작은 트리 형태의 자료구조
max_heap = 부모 노드의 값이 자신 노드의 값보다 큰   트리 형태의 자료구조


"""
import heapq
#heapify = change list to min_heap
# heapify = O(n)
min_heap = [5,3,9,4,1,2,6]
heapq.heapify(min_heap)
print(min_heap)

#pop lowest value and reorder.
#heappop = O(log n)
#reorder process: move tail to head of tree and shift down until necessary.
heapq.heappop(min_heap)
print(min_heap)

#insert value and reorder.
#heappush = O(log n)
#reorder process: add new val to tail and shift up until necessary.
heapq.heappush(min_heap,7)
print(min_heap)


#### heapify max를 정해주는 방법은 의외로 재밌다.
# list의 모든값에 -를 추가해준다음에 heapify해주면된다.
max_heap = [i * -1 for i in min_heap]
print(max_heap)
heapq.heapify(max_heap)
print(max_heap)

#heappop max
a = heapq.heappop(max_heap)
a = a*-1
print(a)
print(max_heap)

#heappush max
val = 10
heapq.heappush(max_heap,val * -1)
print(max_heap)
