from ReadFileConfiguration import ReadFileConfiguration
from Puzzle import Puzzle
from PriorityQueue import PriorityQueue

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
    puzzle1 = Puzzle(puzzle, 999)
    puzzle2 = Puzzle(puzzle, 888)
    puzzle = Puzzle(puzzle, 999)
    if not puzzle.is_solveable():
        print("Puzzle cannot be solved")
    else:
        print("Puzzle can be solved")
        pq = PriorityQueue()
        pq.push(puzzle1)
        pq.push(puzzle2)
        pq.printQueue()
        ppop = pq.pop()
        print(ppop.cost)
        pq.printQueue()
        # print(puzzle.kurang())
        # puzzle.solve()