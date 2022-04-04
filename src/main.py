from ReadFileConfiguration import ReadFileConfiguration
from Puzzle import Puzzle
from BranchBound import BranchBound
from RandomPuzzle import RandomPuzzle
import time

print("Welcome to the 15-Puzzle Solver Program by: Tri Sulton Adila (13520033)")
print("Please enter the method to generate puzzle:")
print("1. Random")
print("2. Manual from file")
generate_puzzle = int(input("Your choice: "))

if generate_puzzle == 1:
    puzzles = RandomPuzzle().puzzles
elif generate_puzzle == 2:
    print("1. Run all the file in the tests folder")
    print("2. Run a specific file")
    choose_file = int(input("Your choice: "))
    if choose_file == 1:
        puzzles = ReadFileConfiguration().puzzles
    elif choose_file == 2:
        file_name = input("Please enter the file name: ")
        puzzles = ReadFileConfiguration(file_name).puzzles

for puzzle in puzzles:
    branch_bound = BranchBound()
    print("====================================")
    print("Your puzzle:")
    puzzle = Puzzle(None, puzzle, branch_bound.cost(puzzle), 0)
    puzzle.printPuzzle()
    print("====================================")

    print("Puzzle Parity:")
    puzzle.printSolveable()
    print("====================================\n")

    if not puzzle.is_solveable():
        print("Puzzle cannot be solved\n")
    else:
        print("Puzzle can be solved")
        print("Start solving...")
        start_time = time.time()
        branch_bound.solve(puzzle)
        print("--- %s seconds ---" % (time.time() - start_time))
        print("Arised Node:", branch_bound.count_node, "\n")