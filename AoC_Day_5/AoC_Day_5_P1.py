# Part one - Find how many IDs occur between any of the given ranges
def main():
    puzzle_input = []
    total_fresh_ids = 0

    with open("puzzle_input.txt") as file:
        puzzle_input = file.read().split('\n')

    # Decant input into appropriate lists
    id_ranges = []
    ids = []

    for line in puzzle_input:
        if '-' in line: # Ranges only
            id_ranges.append(line)
        elif line: # Omit blank line
            ids.append(line)

    # Iterate through ranges
    for id_range in id_ranges:
        range = id_range.split('-')
        lower = int(range[0])
        upper = int(range[1])

        ids_to_remove = []
        for id in ids:
            if int(id) >= lower and int(id) <= upper:
                total_fresh_ids += 1
                ids_to_remove.append(id)
        
        ids = list(set(ids) - set(ids_to_remove))

    print(total_fresh_ids)


if __name__ == "__main__":
    main()