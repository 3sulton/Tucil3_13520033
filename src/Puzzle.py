class Puzzle:
    def __init__(self, parent, matriks, cost, depth):
        self.parent = parent
        self.matriks = matriks
        self.cost = cost
        self.depth = depth
        self.parity()

    def is_solveable(self):
        """
        This method checks whether the puzzle is solvable or not
        :return: boolean
        """
        if (self.sum_of_kurang + self.X) % 2 == 0:
            return True
        return False
        
    
    def parity(self):
        """
        This method calculates the parity of the puzzle
        """
        self.linear_puzzle = [number for row in self.matriks for number in row]
        idx_empty = self.linear_puzzle.index('x')
        self.linear_puzzle[idx_empty] = '16'
        self.kurang = []
        for i in range(16):
            count = 0
            for j in range(i + 1, 16):
                if int(self.linear_puzzle[i]) > int(self.linear_puzzle[j]):
                    count += 1
            self.kurang.append(count)
        
        x_row = self.get_x_row()
        x_col = self.get_x_col()
        x_spot = x_row + x_col
        self.sum_of_kurang = 0
        for i in range(16):
            self.sum_of_kurang += int(self.kurang[i])
        if x_spot % 2 == 0:
            self.X = 0
        else:
            self.X = 1

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

    def printSolveable(self):
        for i in range(16):
            if len(str(i + 1)) == 1:
                print("0" + str(i + 1), ":", self.kurang[self.linear_puzzle.index(str(i + 1))])
            else:
                print(i + 1, ":", self.kurang[self.linear_puzzle.index(str(i + 1))])
        print("------------------------------------")
        print("sum of kurang:", self.sum_of_kurang)
        print("X:", self.X)
        print("sum of kurang + X:", self.sum_of_kurang + self.X)

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