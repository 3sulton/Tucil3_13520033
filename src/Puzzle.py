class Puzzle:
    def __init__(self, puzzle):
        self.puzzle = puzzle # list of list of char

    def is_solveable(self):
        """
        This method checks whether the puzzle is solvable or not
        :return: boolean
        """
        x_row = self.get_x_row()
        if (self.parity() + x_row + 1) % 2 == 0:
            return True
        return False
        # if x_row % 2 == 0:
        #     return self.kurang() % 2 != 0
        # else:
        #     return self.kurang() % 2 == 0
        # if(self.kurang() + X) % 2 == 0:
        #     return True
        # return False
    
    def parity(self):
        """
        this method to return the sum of number of pieces with that the position of
        """
        linear_puzzle = [int(number) for row in self.puzzle for number in row if number != 'x']
        count = 0
        for i in range(15):
            # ctr = 0
            for j in range(i + 1, 15):
                if linear_puzzle[i] > linear_puzzle[j]:
                    # ctr += 1
                    count += 1
            # if(i == 14):
            #     for j in range(14):
            #         if linear_puzzle[i] > linear_puzzle[j]:
            #             count += 1
                        # ctr+= 1
            #print([i, ctr])
        return count

    def get_x_row(self):
        """
        This method returns the x position of the empty space
        :return: list of int
        """
        for(row, col) in enumerate(self.puzzle):
            if 'x' in col:
                return row

    def solve(self):
        """
        This method solves the puzzle
        :return: list of list of char
        """
        print("hiya hiya hiya")

