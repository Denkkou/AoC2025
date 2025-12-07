# Part one - Character cascades down, splitting on carat characters
def main():
    puzzle_input = []
    total_splits = 0
    
    # A list of strings
    with open("puzzle_input.txt") as file:
        puzzle_input = file.read().split('\n')

    # Convert to list of lists
    for line in puzzle_input:
        puzzle_input[puzzle_input.index(line)] = list(line)
    
    # Start position
    start_index = puzzle_input[0].index('S')

    # Descend line-by-line
    beams_present_at = {start_index}
    for i in range(len(puzzle_input)):
        beams_to_remove = []
        beams_to_add = []
        for beam in beams_present_at:
            # Skip any beams that would be behind splitter
            if beam == -1:
                continue
            
            if puzzle_input[i][beam] == '.':
                puzzle_input[i][beam] = '|'

            if puzzle_input[i][beam] == '^': 
                # Splitter hit!
                total_splits += 1

                puzzle_input[i][beam-1] = '|'
                puzzle_input[i][beam+1] = '|'

                # Update locations
                beams_to_add.append(beam - 1)
                beams_to_add.append(beam + 1)
                beams_to_remove.append(beam)

        # Tidy up beams
        for btr in beams_to_remove:
            beams_present_at.remove(btr)
        for bta in beams_to_add:
            beams_present_at.add(bta)

    for line in puzzle_input:
        print(line)
    print(total_splits)           


if __name__ == "__main__":
    main()
