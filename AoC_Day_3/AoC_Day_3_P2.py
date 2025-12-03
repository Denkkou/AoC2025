# Part two - Find the largest spacial number using only 12 digits
def main():
    puzzle_input = ['987654321111111', 
                    '811111111111119', 
                    '234234234234278', 
                    '818181911112111']
    total_output = 0

    with open("puzzle_input.txt") as file:
        puzzle_input = file.read().split('\n')

    for bank in puzzle_input:
        digits_left = 12
        joltage = []
        start = 0

        while digits_left > 0:
            end = len(bank) - digits_left
            
            # Special case: No excess digits to compare
            if start == end:
                joltage.append(bank[start:])
                break
            
            curr_highest = 0
            for i in range(start, end + 1):
                battery_value = int(bank[i])
                if battery_value > curr_highest:
                    curr_highest = battery_value
                    start = i + 1
            
            joltage.append(str(curr_highest))
            digits_left -= 1

        # Combine and sum
        total_output += int(''.join(joltage))
    print(f"Total joltage: {total_output}")


if __name__ == "__main__":
    main()