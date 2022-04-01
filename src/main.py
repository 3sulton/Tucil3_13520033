import ReadFileConfiguration as rfc
import Puzzle as p

print("Welcome to the 15-Puzzle Solver Program by: Tri Sulton Adila (13520033)")
print("Please enter the method to generate puzzle:")
print("1. Random")
print("2. Manual")
#generate_puzzle = int(input("Your choice: "))
generate_puzzle = 2

if generate_puzzle == 1:
    print("not done")
elif generate_puzzle == 2:
    puzzles = rfc.ReadFileConfiguration().puzzles

for puzzle in puzzles:
    puzzle = p.Puzzle(puzzle)
    if not puzzle.is_solveable():
        print("Puzzle cannot be solved")
    else:
        print("Puzzle can be solved")
        # print(puzzle.kurang())
        # puzzle.solve()