# Part one - Perform arithmetic on columns of values
def main():
    puzzle_input = []
    grand_total = 0
    
    # A list of strings
    with open("puzzle_input.txt") as file:
        puzzle_input = file.read().split('\n')
    
    # Split strings into list of strings
    for line in puzzle_input:
        puzzle_input[puzzle_input.index(line)] = line.split(" ")
    
    # Remove all instances of " " from entire input
    for row in puzzle_input:
        puzzle_input[puzzle_input.index(row)] = [n for n in row if n != '']

    # New list where each sublist is a column 
    formatted_input = [[] for x in range(len(puzzle_input[0]))]

    # Sort row elements into correct columna
    for x in range(0, len(puzzle_input)): # For each row
        for y in range(0, len(puzzle_input[0])): # Each item in row
            formatted_input[y].append(puzzle_input[x][y])
    
    
    # Get operator, perform operation on each value
    for column in formatted_input:
        total = 0
        operator = column[-1]
        for value in column:
            if value != "+" and value != "*":
                if operator == "+":
                    total += int(value)
                if operator == "*":
                    if total == 0: # Guard against n*0=0
                        total += int(value)
                    else:
                        total *= int(value)
        grand_total += total

    print(grand_total)


if __name__ == "__main__":
    main()
