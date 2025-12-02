# Part two - Sum invalid IDs determined by AT LEAST 2 repeated sequences
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

def has_repeated_sequence(num: str) -> bool:
    chunk_size = 1
    while True:
        # Skip chunk sizes that don't divide cleanly
        if len(num) % chunk_size == 0:
            # The original number is not a sequence
            if chunk_size == len(num):
                return False
            
            chunks = get_chunk_list(num, chunk_size)

            # If not a list of identical chunks, increase chunk size
            if len(set(chunks)) != 1:
                chunk_size += 1
            else:
                return True # Found repeating sequence!
        else:
            chunk_size += 1
   
def get_chunk_list(num: str, chunk_size: int) -> list:
    chunk_list = [num[i:i+chunk_size] for i in range(0, len(num), chunk_size)]
    return chunk_list

if __name__ == "__main__":
    main()
