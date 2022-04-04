import random

class RandomPuzzle:
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', 'x']
    def __init__(self):
        self.puzzle = []
        self.puzzles = []
        random.shuffle(self.number)
        for i in range(4):
            row = []
            for j in range(4):
                row.append(self.number[i*4 + j])
            self.puzzle.append(row)
        self.puzzles.append(self.puzzle)