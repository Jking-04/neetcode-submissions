class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word

        self.next_dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        starting_points = []
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if self.board[y][x] == word[0]:
                    starting_points.append((x,y))

        for point in starting_points: 
            if self.backtrack(visited = set([point]),point = point,string = self.word[1:]):
                return True

        return False

    def backtrack(self,visited,point,string):
        
        if not string:
            return True

        
        for next_dir in self.next_dirs:
            x,y = point
            x_shift,y_shift = next_dir
            new_x,new_y = x + x_shift,y + y_shift
            new_pos = (new_x,new_y)

            within_x = new_x >= 0 and new_x<len(self.board[0])
            within_y = new_y >= 0 and new_y<len(self.board)
            
            if new_pos in visited or not within_x or not within_y:
                continue
            

            if self.board[new_y][new_x] == string[0]:
                visited.add(new_pos)
                if self.backtrack(visited= visited,point = new_pos,string = string[1:]):
                    return True
                visited.remove(new_pos)
        return False





        



        