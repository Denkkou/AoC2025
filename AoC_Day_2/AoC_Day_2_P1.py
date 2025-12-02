# Part one - Sum invalid IDs determined by repeated sequences
def main():
    puzzle_input = ['11-22','95-115','998-1012',
                    '1188511880-1188511890','222220-222224','1698522-1698528',
                    '446443-446449','38593856-38593862','565653-565659',
                    '824824821-824824827','2121212118-2121212124']
    invalid_id_sum = 0

    with open("puzzle_input.txt") as file:
        puzzle_input = file.read().split(',')

    for id_range in puzzle_input:
        pieces = id_range.split('-')

        # Range inclusive
        for num in range(int(pieces[0]), int(pieces[1]) + 1):
           if has_repeated_sequence(str(num)):
               invalid_id_sum += num
               print(f"Invalid ID found {pieces[0]}-{pieces[1]}: {num}")
    
    print(f"Sum of invalid IDs {invalid_id_sum}")        

def has_repeated_sequence(num) -> bool:
    if len(num) % 2 != 0: # Can't halve odd lengths
        return False
    
    first, second = num[:len(num)//2], num[len(num)//2:]
    if int(first) == int(second):
        return True
    
    return False

if __name__ == "__main__":
    main()
