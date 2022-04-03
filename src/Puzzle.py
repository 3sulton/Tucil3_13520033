class Puzzle:
    def __init__(self, parent, matriks, cost, depth):
        self.parent = parent
        self.matriks = matriks
        self.cost = cost
        self.depth = depth

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
        linear_puzzle = [int(number) for row in self.matriks for number in row if number != 'x']
        count = 0
        for i in range(15):
            for j in range(i + 1, 15):
                if linear_puzzle[i] > linear_puzzle[j]:
                    count += 1
        return count

    def get_x_row(self) -> int:
        """
        This method returns the x position of the empty space
        :return: list of int
        """
        for(row, col) in enumerate(self.matriks):
            if 'x' in col:
                return row

    def get_x_col(self) -> int:
        """
        This method returns the x position of the empty space
        :return: list of int
        """
        row = self.get_x_row()
        for(col, number) in enumerate(self.matriks[row]):
            if number == 'x':
                return col


    def printPuzzle(self):
        """
        This method prints the puzzle
        :return: None
        """
        for i in range(4):
            print("+----" * 4 + "+")
            for j in range(4):
                number = self.matriks[i][j]
                if number == 'x':
                    print("|    ", end="")
                else:
                    if len(number) == 1:
                        print("| 0{} ".format(self.matriks[i][j]), end="")
                    else:
                        print("| {} ".format(self.matriks[i][j]), end="")
                if(j == 3):
                    print("|")
        print("+----" * 4 + "+")

    def get_tile(self, row, col):
        """
        This method returns the tile at the specified position
        :param row: int
        :param col: int
        :return: int
        """
        return self.matriks[row][col]

    def printPath(self):
        """
        This method prints the path of the puzzle
        :return: None
        """
        if self.parent is None:
            self.printPuzzle()
            return
        self.parent.printPath()
        self.printPuzzle()