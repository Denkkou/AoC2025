# Part two - How many rolls can be removed until none have <4 adjacent rolls
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
    
    # Convert into list of lists
    grid = []
    for line in puzzle_input:
        grid.append(list(line))

    while True:
        removed_this_pass = 0

        # Row then Column
        for x in range(0, len(grid[0])):
            for y in range(0, len(grid)):
                
                surrounding_rolls = 0

                # First, check if a roll at all
                if grid[x][y] == '@':

                    # Adjacency checks
                    for i in range(-1, 2):
                        for j in range(-1, 2):

                            # Skip self
                            if i == 0 and j == 0:
                                continue

                            # Skip out of bounds
                            if (x + i < 0 or 
                                x + i > len(grid[0])-1 or
                                y + j < 0 or 
                                y + j > len(grid)-1
                                ):
                                continue

                            # Otherwise, as you were
                            if (grid[x + i][y + j] == '@' or
                                grid[x + i][y + j] == 'x'
                                ):
                                surrounding_rolls += 1

                    # Accessible?
                    if surrounding_rolls < 4:
                        # Set self to x to mark as removed
                        grid[x][y] = 'x'
                        removed_this_pass += 1 
                        total_rolls += 1
        
        # Remove all x's and repeat
        for x in range(0, len(grid[0])):
            for y in range(0, len(grid)):
                if grid[x][y] == 'x':
                    grid[x][y] = '.'             
        
        # Escape loop if we removed none this pass
        print(f"Removed this pass: {removed_this_pass}")
        if removed_this_pass == 0:
            break

    print(f"Accessible rolls of paper: {total_rolls}")



if __name__ == "__main__":
    main()