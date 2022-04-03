from PriorityQueue import PriorityQueue

class BranchBound:
    def __init__(self, puzzleParent):
        pass
        self.queue = PriorityQueue()
        self.puzzleParent = puzzleParent
        self.goalPuzzle = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', 'x']]
    
    def cost(self, puzzle) -> int:
        """
        calculate cost of puzzle
        """
        cost = puzzle.depth
        for i in range(4):
            for j in range(4):
                tile = puzzle.get_tile(i, j)
                if tile != 'x' and tile != self.goalPuzzle[i][j]:
                    cost += 1
        return cost