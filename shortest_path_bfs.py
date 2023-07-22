# shortest path using Breadth First Search
# Find the shortest path that goes from 'S' to 'E'

class solution:
    def find_exit(self, cube):
        for i in range(len(cube)):
            for j in range(len(cube[i])):
                if cube[i][j] == 'E':
                    return [i,j]
    
    def find_start(self, cube):
        for i in range(len(cube)):
            for j in range(len(cube[i])):
                if cube[i][j] == 'S':
                    return [i,j]
    
    def is_valid(self, cube, moves):
        start = self.find_start(cube)
        x = start[0]
        y = start[1]

        for move in moves:
            if move == 'L':
                y -= 1
            elif move == 'R':
                y += 1
            elif move == 'D':
                x += 1
            elif move == 'U':
                x -= 1

            if not (0<=y<len(cube[0]) and 0<=x<len(cube)):
                return False
            elif cube[x][y] == '0':
                return False
        return True 
    
    def is_done(self, cube, moves):
        start = self.find_start(cube)
        end = self.find_exit(cube)
        x = start[0]
        y = start[1]

        for move in moves:
            if move == 'L':
                y -= 1
            elif move == 'R':
                y += 1
            elif move == 'D':
                x += 1
            elif move == 'U':
                x -= 1

        if x == end[0] and y == end[1]:
            return True
        else:
            return False

    def shortest_path(self, cube):
        queue = [""]
        first_out = ""
        
        while self.is_done(cube,first_out) != True:
            first_out = queue.pop(0)
            for j in ["L",'R','U','D']:
                put = first_out + j
                if self.is_valid(cube, put)==True:
                    if len(put)<3:
                        queue.append(put)
                    else:
                        if put[-1] == "L" and put[-2] != "R" or put[-1] == "R" and put[-2] != "L" or put[-1] == "U" and put[-2] != "D" or put[-1] == "D" and put[-2] != "U":
                            queue.append(put)
                
        return first_out[:len(first_out)-1]

    
    def print_shortest_path(self, cube):
        moves = self.shortest_path(cube)
        start = self.find_start(cube)
        x = start[0]
        y = start[1]
        for move in moves:
            if move == 'D':
                cube[x+1][y] = '+'
                x += 1
            elif move == 'U':
                cube[x-1][y] = '+'
                x -= 1
            elif move == 'L':
                cube[x][y-1] = '+'
                y -= 1
            elif move == 'R':
                cube[x][y+1] = '+'
                y += 1
        
        for i in cube:
            print(i)        

if __name__ == "__main__":
    cube = [
        ['0','0','S','0','0','0','0','0','0'],
        ['0',' ',' ',' ','0',' ',' ',' ','0'],
        ['0',' ','0','0','0',' ',' ',' ','0'],
        ['0',' ','0',' ','0',' ',' ',' ','0'],
        ['0',' ','0','0','0',' ',' ',' ','0'],
        ['0',' ','0',' ',' ',' ',' ',' ','0'],
        ['0',' ','0',' ',' ','0',' ',' ','0'],
        ['0',' ','0',' ',' ','0',' ',' ','0'],
        ['0',' ',' ',' ','0',' ',' ',' ','0'],
        ['0',' ',' ',' ','0',' ','0',' ','E'],
        ['0','0','0','0','0','0','0','0','0']
    ]
S = solution()
print(S.print_shortest_path(cube))
