from ReadFileConfiguration import ReadFileConfiguration
from Puzzle import Puzzle
from BranchBound import BranchBound

print("Welcome to the 15-Puzzle Solver Program by: Tri Sulton Adila (13520033)")
print("Please enter the method to generate puzzle:")
print("1. Random")
print("2. Manual")
#generate_puzzle = int(input("Your choice: "))
generate_puzzle = 2

if generate_puzzle == 1:
    print("not done")
elif generate_puzzle == 2:
    puzzles = ReadFileConfiguration().puzzles

for puzzle in puzzles:
    branch_bound = BranchBound()
    puzzle = Puzzle(None, puzzle, branch_bound.cost(puzzle), 0)
    if not puzzle.is_solveable():
        print("Puzzle cannot be solved")
    else:
        print("Puzzle can be solved")
        branch_bound.solve(puzzle)