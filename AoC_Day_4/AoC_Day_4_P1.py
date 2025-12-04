def main():
    puzzle_input = ['..@@.@@@@.',
                    '@@@.@.@.@@',
                    '@@@@@.@.@@',
                    '@.@@@@..@.',
                    '@@.@@@@.@@',
                    '.@@@@@@@.@',
                    '.@.@.@.@@@',
                    '@.@@@.@@@@',
                    '.@@@@@@@@.',
                    '@.@.@@@.@.']
    total_rolls = 0
    
    with open("puzzle_input.txt") as file:
        puzzle_input = file.read().split('\n')
    
    # Row then Column
    for x in range(0, len(puzzle_input[0])):
        for y in range(0, len(puzzle_input)):
            
            surrounding_rolls = 0

            # First, check if a roll at all
            if puzzle_input[x][y] == '@':

                # Adjacency checks
                for i in range(-1, 2):
                    for j in range(-1, 2):

                        # Skip self
                        if i == 0 and j == 0:
                            continue

                        # Skip out of bounds
                        if (x + i < 0 or 
                            x + i > len(puzzle_input[0])-1 or
                            y + j < 0 or 
                            y + j > len(puzzle_input)-1
                            ):
                            continue

                        # Otherwise, as you were
                        if puzzle_input[x + i][y + j] == '@':
                            surrounding_rolls += 1

                # Accessible?
                if surrounding_rolls < 4:
                    total_rolls += 1

    print(f"Accessible rolls of paper: {total_rolls}")


if __name__ == "__main__":
    main()