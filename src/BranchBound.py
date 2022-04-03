from PriorityQueue import PriorityQueue
from Puzzle import Puzzle
import copy
class BranchBound:
    def __init__(self):
        self.queue = PriorityQueue()
        self.goalPuzzle = [['1', '2', '3', '4'],
                           ['5', '6', '7', '8'],
                           ['9', '10', '11', '12'],
                           ['13', '14', '15', 'x']]
    
    def cost(self, matriks) -> int:
        """
        calculate cost of matriks
        """
        cost =0
        for i in range(4):
            for j in range(4):
                tile = matriks[i][j]
                if tile != 'x' and tile != self.goalPuzzle[i][j]:
                    cost += 1
        return cost
    
    def create_children(self, puzzle) -> list:
        """
        This method creates children of the puzzle
        """
        children = []
        # bottom, left, top, right
        row = [ 1, 0, -1, 0 ]
        col = [ 0, -1, 0, 1 ]
        for i in range(4):
            x_row = puzzle.get_x_row()
            x_col = puzzle.get_x_col()
            new_row = x_row + row[i]
            new_col = x_col + col[i]
            if 0 <= new_row <= 3 and 0 <= new_col <= 3:
                child_matriks = copy.deepcopy(puzzle.matriks)
                child_matriks[x_row][x_col], child_matriks[new_row][new_col] = child_matriks[new_row][new_col], child_matriks[x_row][x_col]
                child = Puzzle(puzzle, child_matriks, self.cost(child_matriks) + puzzle.depth, puzzle.depth + 1)
                children.append(child)
        return children

    def solve(self, puzzleParent):
        """
        This method solves the puzzle
        """
        self.puzzleParent = puzzleParent
        self.queue.push(puzzleParent)
        while (not self.queue.is_empty()):
            puzzle = self.queue.pop()
            if puzzle.matriks == self.goalPuzzle:
                puzzle.printPath()
                return
            else:
                children = self.create_children(puzzle)
                for child in children:
                        self.queue.push(child)