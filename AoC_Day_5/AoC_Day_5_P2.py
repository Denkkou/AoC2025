# Part two - Find how many unique IDs are between all ranges
def main():
    puzzle_input = ['3-5', '10-14', '16-20', '12-18']
    total_fresh_ids = 0

    #with open("puzzle_input.txt") as file:
        #puzzle_input = file.read().split('\n')

    # Ignoring IDs-to-check for P2
    id_ranges = []
    for line in puzzle_input:
        if '-' in line: # Ranges only
            split_range = line.split('-')
            id_ranges.append(split_range)

    # Initialise super ranges and drop from original list
    super_ranges = [id_ranges[0]]
    id_ranges.remove(id_ranges[0])
    
    for id_range in id_ranges:
        for super_range in super_ranges:
            r1, r2 = int(id_range[0]), int(id_range[1])
            s1, s2 = int(super_range[0]), int(super_range[1])

            # Check for exact overlap or range within super
            if (r1 >= s1 and r2 <= s2): 
                #print(f"{id_range} within {super_range}")
                continue

            # Now check if range overencompasses super
            if (r1 < s1 and r2 > s2):
                print(f"{id_range} encompasses {super_range}")
                # Update upper and lower bounds
                super_range[0] = r1
                super_range[1] = r2
                continue
            
            # We have two overlapping cases left
            # Starts before and ends on or after super start
            if (r1 < s1 and r2 >= s1 and r2 < s2):
                print(f"{id_range} overlaps start of {super_range}")
                # Update lower bound
                super_range[0] = r1
                continue

            # Starts within or on super start and ends after super end
            if (r1 >= s1 and r1 < s2 and r2 > s2):
                print(f"{id_range} overlaps end of {super_range}")
                # Update upper bound
                super_range[1] = r2
                continue
            
            # Finally, if it didnt overlap at all, add it to the super ranges
            print(f"No overlap, appending {id_range}")
            if id_range not in super_ranges:
                super_ranges.append(id_range)
                

    # Debug print
    print(*super_ranges)

    for super_range in super_ranges:
        total_fresh_ids += int(super_range[1]) - int(super_range[0])    
    print(total_fresh_ids)

####
# None of this works!!!
# I'm stumped and tired of it. 
# I know I will also have to do a merge check for the super_ranges
# but it's getting complicated. I think I've gone about it the wrong way.
####

if __name__ == "__main__":
    main()
