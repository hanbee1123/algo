class Snake:
    def solution(self, m, apple, rotation):
        rotation = dict(rotation)    
        apple = [[i[0]-1,i[1]-1] for i in apple]

        #Draw a map
        _map = [['0']*m for _ in range(m)]
        _map[0][0] = 'S'

        #set variables
        row = len(_map)
        col = len(_map[0])
        location_of_snake = [[0,0]]
        time_count = 0
        direction = 'RR'
        move_dir = ''

        # Snake keeps moving until the following conditions are met: HIT WALL, HIT TAIL
        while 0<=location_of_snake[-1][0]<=col-1 and 0<=location_of_snake[-1][1]<=col-1 and (location_of_snake[-1] not in location_of_snake[:-1]):
            time_count += 1
            #First move the snake
            location_of_snake = self.move(location_of_snake, direction, apple)
            move_dir = ''

            if time_count in rotation.keys():
                move_dir = rotation[time_count]
                if move_dir == 'L':
                    if direction == 'RR':
                        direction = 'UU'
                    elif direction == 'LL':
                        direction = 'DD'
                    elif direction == 'UU':
                        direction = 'LL'
                    else:
                        direction = 'RR'
                if move_dir == 'D':
                    if direction == 'RR':
                        direction = 'DD'
                    elif direction == 'LL':
                        direction = 'UU'
                    elif direction == 'UU':
                        direction = 'RR'
                    else:
                        direction = 'LL'

            # Print location of snake for debugging
            _map = self.print(_map, location_of_snake)
        return time_count

    def move(self, location_of_snake, direction, apple):
        if direction == 'RR':
            location_of_snake.append([location_of_snake[-1][0],location_of_snake[-1][1]+1])

    
        elif direction == 'LL':
            location_of_snake.append([location_of_snake[-1][0],location_of_snake[-1][1]-1])

        
        elif direction == 'DD':
            location_of_snake.append([location_of_snake[-1][0]+1,location_of_snake[-1][1]])

        
        else: #direction == 'UU'
            location_of_snake.append([location_of_snake[-1][0]-1,location_of_snake[-1][1]])

        if location_of_snake[-1] not in apple:
                location_of_snake.pop(0)
        else:
            apple.remove([location_of_snake[-1][0], location_of_snake[-1][1]])
        return location_of_snake

    def print(self, _map, location_of_snake):
        for i in range(len(_map)):
            for j in range(len(_map[0])):
                if [i,j] in location_of_snake:
                    _map[i][j] = 'S'
                else:
                    _map[i][j] = '0'
        for i in _map:
            print(i)
        print("")
        
        return _map



if __name__ == "__main__":
    B = Snake()
    m = 10
    apple = [[1,5],[1,3],[1,2],[1,6],[1,7]]
    rotation = [[8,'D'],[10,'D'],[11,'D'],[13,'L']]
    print(B.solution(m, apple, rotation))
    