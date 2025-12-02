def main():
    # Read data in from file, deliniated by commas ,

    # For each item, split around the dash -
    # Use each item as a range, eg, 11-22 is a range from 11 to 22 inclusive
    # For each number in that range, check if it contains two repeated sequences
    # Eg, between 998-1012, only 1010 is a repeated sequence (10 and 10)

    # To find a repeated sequence, for each number, split it in half
    # Compare each half, and if they are the same, add to a total sum

    # (Anticipating part 2, may be asked to find if there is a sequence
    # hidden within a wider number, in which case recursively split until
    # each half is 1 digit long?)

    puzzle_input = ['11-22','95-115','998-1012','1188511880-1188511890','222220-222224','1698522-1698528','446443-446449','38593856-38593862','565653-565659','824824821-824824827','2121212118-2121212124']
    invalid_id_sum = 0

    # Read from txt here
    # ...

    for id_range in puzzle_input:
        pieces = id_range.split('-')

        # Range inclusive
        for num in range(int(pieces[0]), int(pieces[1]) + 1):
           if has_repeated_sequence(num):
               invalid_id_sum += num
               print(f"Invalid ID found between {pieces[0]} and {pieces[1]}: {num}")
        


def has_repeated_sequence(num) -> bool:
    if len(num) % 2 != 0: # Can't halve odd lengths
        return False
    
    # Slice in half spacially, compare halves when cast to ints
    # If the same, return True


if __name__ == "__main__":
    main()
