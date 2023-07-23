"""
0번방부터 n-1번방까지 총 n개의 방이 있다. 
0번을 제외한 모든 방은 잠겨있다. 우리의 목표는 모든 방에 visit하는것이다. 하지만 잠겨져 있는 방은 key가 없으면 visit할 수 없다.
각 방에 방문할 때, 별개의 열쇠뭉치 (a set of distinct keys)를 찾을 수도 있다. 각각의 열쇠에는 number가 쓰여있고, 해당 번호에 해당하는 방을
잠금 해제할 수 있다. 열쇠뭉치는 모두 가져갈 수 있고, 언제든 방문을 열기 위해서 사용할 수 있다.

문제에서 rooms 배열이 주어지고, rooms[i]는 해당 방에서 얻을 수 있는 열쇠뭉치 목록을 표현한다.
모든 방을 visit할 수 있다면 True, 그렇지 않다면 False를 반환해라.

input: rooms = [[1],[2],[3],[]]
output: true

input: rooms  = [[1,3],[3,0,1],[2],[0]]
output: False

코드구현:
loop through rooms:
collect values and append it to keys. using a dict would be best.
if v not in keys:
return False

else, if looping is done return True. 


"""
from collections import deque
def kar(rooms: list):
    visited = set([0])
    q = deque([0])
    while q:
        now_room = q.popleft()
        for room in rooms[now_room]:
            if room not in visited:
                visited.add(room)
                q.append(room)

    return len(rooms) == len(visited)



def kar_dfs(rooms: list):
    visited = set([0])

    def dfs(index):
        for j in rooms[index]:
            if j not in visited:
                visited.add(j)
                dfs(j)
    
    dfs(0)
    return len(visited) == len(rooms)
    



if __name__=="__main__":
    rooms = [[1],[2],[3],[]]
    rooms2  = [[1,3],[3,0,1],[2],[0]]
    rooms3 = [[2],[],[1]]
    print(kar_dfs(rooms2))

