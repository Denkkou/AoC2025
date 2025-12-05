# Part two - Find how many unique IDs are between all ranges
def main():
    puzzle_input = []
    total_fresh_ids = 0

    with open("puzzle_input.txt") as file:
        puzzle_input = file.read().split('\n')

    # Ignoring IDs-to-check for P2
    #id_ranges = ['3-5', '10-14', '16-20', '12-18']
    id_ranges = []
    for line in puzzle_input:
        if '-' in line: # Ranges only
            id_ranges.append(line)
    
    # Make ranges useable
    for id_range in id_ranges:
        split_range = id_range.split('-')
        lower = int(split_range[0])
        upper = int(split_range[1])

        # TODO condense ranges into as few, wide ranges as possible
        # This should eliminate cases of overlapping
        # Find the difference between upper and lower for each
        # Add to total_fresh_ids 

        # Create a list of super ranges, init with first id_range
        # for every range in id_ranges,
        #   for every range in super_ranges
        # check if id_range overlaps
        #   - does it start before the range and end after or within it?
        #   - does it start within the range and end after it?
        #   extend the super_ranger's upper and lower bounds accordingly
        # if the range does not overlap at all, add it to the super_ranges list
        # once all ranges are condensed into a series of fewer wider rangers,
        # find the difference between the upper and lower bounds of each
        # sum to total_fresh_ids
        
    
    # Output
    print(total_fresh_ids)



if __name__ == "__main__":
    main()
