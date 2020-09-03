def solution(m, apple, rotation):
    # Draw a map
    _map = [['0']*m for _ in range(m)]
    _map[0][0] = 'S'
    row = len(_map)
    col = len(_map[0])

    time_count = 0
    direction = 'D'
    for i in range(row):
        for j in range(col):
            if [i, j] in apple:
                _map[i][j] = 'A'
    
    while time_count != rotation[0][0]:
    
def direction(_map, direction):
    if direction = 'D':

def eat_apple(_map, direction):




    
    
    
    # TESTER
    for i in _map:
        print(i)


if __name__ == "__main__":
    m = 6
    apple = [[3,4],[2,5],[5,3]]
    rotation = [[3,'D'],[15,'L'],[17,'D']]
    solution(m, apple, rotation)