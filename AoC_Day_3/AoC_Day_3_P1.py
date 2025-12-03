# Part one - Find the spacially biggest number in each row, then sum them all
def main():
    puzzle_input = ['987654321111111', 
                    '811111111111119', 
                    '234234234234278', 
                    '818181911112111']
    total_output = 0
    
    with open("puzzle_input.txt") as file:
        puzzle_input = file.read().split('\n')

    # Always does 1 full pass for the first digit, <1 for second digit
    for bank in puzzle_input:
        curr_highest_first = 0
        curr_highest_index = 0
        for battery in bank[:-1]:
            battery_value = int(battery)
            if battery_value > curr_highest_first:
                curr_highest_first = battery_value
                curr_highest_index = bank.index(battery)
        
        # Once we have the first, resume from after it
        curr_highest_second = 0
        for battery in bank[curr_highest_index+1:]:
            battery_value = int(battery)
            if battery_value > curr_highest_second:
                curr_highest_second = battery_value

        # Combine and sum
        total_output += int(str(curr_highest_first) + str(curr_highest_second))   
    print(f"Total output joltage = {total_output}")


if __name__ == "__main__":
    main()