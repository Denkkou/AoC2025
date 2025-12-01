def main():
    dial_position = 50
    puzzle_input = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
    solution = 0

    with open("puzzle_input.txt") as file:
        puzzle_input = file.read().splitlines('\n')

    for rotation in puzzle_input:
        direction = rotation[0] # L or R
        distance = int(rotation[1:]) # Number

        match direction:
            case 'L':
                dial_position = rotate_dial_left(distance, dial_position)
            case 'R':
                dial_position = rotate_dial_right(distance, dial_position)
        
        print(f"Rotating {direction}{distance}\nNew dial position = {dial_position}")

        if dial_position == 0:
            solution += 1
    
    print(f"Times Zero pointed at: {solution}")

def rotate_dial_left(distance, dial_position) -> int:
    new_position = dial_position - (distance % 100)

    if new_position < 0:
        new_position = 100 + new_position

    return new_position

def rotate_dial_right(distance, dial_position) -> int:
    new_position = dial_position + (distance % 100)

    if new_position > 99:
        new_position = 0 + new_position - 100

    return new_position
    
if __name__ == "__main__":
    main()
