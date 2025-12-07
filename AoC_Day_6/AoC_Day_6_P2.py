# Part two - Right-to-left, column arithmetic on a wide input
def main():
    puzzle_input = []
    grand_total = 0
    
    # A list of strings
    with open("puzzle_input.txt") as file:
        puzzle_input = file.read().split('\n')

    # Start organising vertical slices into lists
    columns = []
    
    for i in range(len(puzzle_input[0])):
        column = []
        for row in puzzle_input:
            column.append(row[i])
        columns.append(column)

    # Traverse columns, toggling operator when encountered
    total = 0
    op = ''

    for col in columns:
        if is_column_empty(col):
            grand_total += total # Doesn't catch final total
            total = 0
            continue

        if col[-1] == '+' or col[-1] == '*':
            op = col[-1]

        number = column_to_number(col)
        if op == '+':
            total += number
        if op == '*':
            if total == 0:
                total += number
            else:
                total *= number
    grand_total += total # Catch final total
    print(grand_total)

# Check if column contains anything at all
def is_column_empty(column) -> bool:
    return all(c == ' ' for c in column)

# Take list of chars and return integer value
def column_to_number(column) -> int:
    num_string = []
    for char in column:
        if char:
            num_string.append(char)
    return int(''.join(num_string[:-1]))


if __name__ == "__main__":
    main()
