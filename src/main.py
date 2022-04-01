import ReadFileConfiguration as rfc

print("Welcome to the 15-Puzzle Solver Program by: Tri Sulton Adila (13520033)")
print("Please enter the method to generate puzzle:")
print("1. Random")
print("2. Manual")
generate_puzzle = int(input("Your choice: "))

if(generate_puzzle == 1):
    print("not done")
elif(generate_puzzle == 2):
    puzzles = rfc.ReadFileConfiguration().puzzles
    print(puzzles)


# for puzzle in puzzles:
    # if bisa diselesaikan
        # solve(puzzle)
    # else:
        # print("Puzzle cannot be solved")