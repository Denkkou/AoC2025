# Part one - Find how many times the dial finishes a rotation on zero
def part_one():
    dial_position = 50
    puzzle_input = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82'] # Test input
    solution = 0

    with open("puzzle_input.txt") as file:
        puzzle_input = file.read().splitlines('\n')

    for rotation in puzzle_input:
        direction = rotation[0] # L or R
        distance = int(rotation[1:]) # Number

        match direction:
            case 'L':
                dial_position = rotate_dial(-distance, dial_position)
            case 'R':
                dial_position = rotate_dial(distance, dial_position)
                
        print(f"Rotating {direction}{distance}, New dial position = {dial_position}")

        if dial_position == 0:
            solution += 1
    
    print(f"Times Zero pointed at: {solution}")

def rotate_dial(distance, dial_position) -> int:
    new_position = dial_position + (distance % 100)

    if new_position < 0:
        new_position = 100 + new_position
    if new_position > 99:
        new_position = 0 + new_position - 100

    return new_position


# Part two - Find how many times the dial passes zero as well as finishes on it
def part_two():
    dial_position = 50
    puzzle_input = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82'] # Test input
    solution = 0

    with open("puzzle_input.txt") as file:
        puzzle_input = file.read().splitlines('\n')

    for rotation in puzzle_input:
        direction = rotation[0] # L or R
        distance = int(rotation[1:]) # Number

        # Inefficient, but couldn't figure out a better way :[
        match direction:
            case 'L':
                for i in range(0, distance):
                    if dial_position == 0:
                        solution += 1

                    dial_position -= 1
                    if dial_position < 0:
                        dial_position = 99

            case 'R':
                for i in range(0, distance):
                    if dial_position == 0:
                        solution += 1

                    dial_position += 1
                    if dial_position > 99:
                        dial_position = 0

        print(f"Rotating {direction}{distance}, New dial position = {dial_position}")

    print(f"Times Zero pointed at or passed: {solution}")


def main():
    #part_one()
    part_two()


if __name__ == "__main__":
    main()
