# loading the map as a list of lists with each sublist as a row and each number as an integer
def load_map(filename):
    with open(filename, 'r') as f:
        return [[int(ch) for ch in line.strip()] for line in f]  # uses list comprehension 
# outer: for line in f --> loop through each line in the file f
# inner: [int(ch) for ch in line.strip()] --> strip the line, loop over each ch in stripped line, convert to int and output list

# find what coordinates are adjacent to our current position, taking into account the map limits
def get_adjacent_coords(coord, max_rows, max_cols):
    r, c = coord  # current position in row and column 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right directions
    for dr, dc in directions:  # for each tuple in the directions we take the (r, c) values where dr = r, dc = c
        nr, nc = r + dr, c + dc  # new row, new column = old row + direction etc
        if 0 <= nr < max_rows and 0 <= nc < max_cols:  # check if the new coordinates are in the bounds of the map
            yield (nr, nc)  # calculates the first (nr, nc), remembers that it stopped there, then only calculates the next (nr, nc) if asked

# find the coordinates of where on the map the value is 0
def find_trailheads(map_data):
    trailheads = []
    for i in range(len(map_data)):  # index value i for which row we're in
        for j in range(len(map_data[0])):  # index value j for which column we're in
            if map_data[i][j] == 0:  # if (i,j) in our map we load in is 0, it's a trailhead
                trailheads.append((i, j))
    return trailheads  # returns list of trailheads

# counting how many summits can be reached from a certain start point, popularity score
def reachable_summits(map_data, start):  # finds all reachable summits given a starting coordinate
    height = len(map_data)  # initialising the height and width of our map
    width = len(map_data[0])
    current_coords = [start]  # the current coords starts at start, but then updates
    visited = set()  # stores any coordinates already visited without duplicates
    for target in range(1, 10):  # heights ranging from 1 to 9 inclusive
        next_coords = []  
        for r, c in current_coords:  # separates the (row, column)
            for nr, nc in get_adjacent_coords((r, c), height, width):  # gets the adjacent (nr, nc) of current with the adj function
                if map_data[nr][nc] == target and (nr, nc) not in visited:  # check if the value of (nr, nc) is the height we want
                    next_coords.append((nr, nc))  # we add the new possible coordinates at the target height
                    visited.add((nr, nc))  # we also add that we've already been to this position
        current_coords = next_coords[:]  # now we start from the adjacent coordinates at the new height
        if target == 9:  # stop when we get to height 9
            return set(current_coords)  # returns the unique coordinates that have a height 9
    return set()  # if a summit isn't reachable, it'll return an empty set

# counts how many distinct paths can be found to all summits accessible from a trailhead
def count_distinct_paths(map_data, start):
    height = len(map_data)  # initialising our map size
    width = len(map_data[0])
    count = 0

    # recursive function that tries to go as far as it can down one path, then backs up and tries the next one
    def dfs(r, c, current_value):  # (r,c) is the row and column of the current position, and current_value is the height at that position
        nonlocal count  # using the count variable from the enclosing function above
        if current_value == 9:  # if we reach 9, we reached a summit via a distinct path
            count += 1  # we increment our count, which counts how many distinct paths we can take to reach a summit 
            return  # end this path of exploration
        # finding all adj positions that are the current height + 1
        for nr, nc in get_adjacent_coords((r, c), height, width):  # find all adj coordinate to our current position
            if map_data[nr][nc] == current_value + 1:  # if the adj coordinate is the next elevation step 
                dfs(nr, nc, current_value + 1)

    dfs(start[0], start[1], 0)  # starts at the trailhead with its coordinates and height 0
    return count  # returns total number of distinct increasing-elevation paths from height 0 to height 9 starting at start
# how dfs works (recursion)
# trailhead -> adj coordinates that are +1 -> if multiple values start with first one -> adj coords that are +1 ->  if multiple values start 
# with first one -> repeat until either cannot go +1 with adj coordinates or we reach a summit, if a summit is reached we add +1 to the count 
# -> go back to where we last branched (found multiple adj coordinates that had +1 height) -> try to get to a summit again -> return to branch 
# before that


def main(filename):  # only inputs which text file we want to use
    map_data = load_map(filename)  # gets the topographic map as a list of lists with the rows as sublists and each number in it as an integer
    trailheads = find_trailheads(map_data)  # finds all trailheads in our map
    total_popularity = 0  # initialising
    total_completionist = 0

    for trailhead in trailheads:  # for each trailhead
        summits = reachable_summits(map_data, trailhead)  # find how many summits we can reach
        popularity = len(summits)  # popularity is just the how many coordinates of summits we reached
        completionist = count_distinct_paths(map_data, trailhead)  # completion is count of how many distinct paths we can reach from the trailhead
        total_popularity += popularity  # we sum the popularity found for each trailhead to find for the entire map
        total_completionist += completionist

    print("Total Popularity Score:", total_popularity)
    print("Total Completionist Score:", total_completionist)

# usage
main("large.txt")
