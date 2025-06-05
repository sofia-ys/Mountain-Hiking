smallFile = "small.txt"
largeFile = "large.txt"

# extracting the topographical data into a list
topo = []
with open(largeFile) as fin:
    for line in fin:  # for each line in the file we choose
        topo.append([int(ch) for ch in line.strip()])  # strip each line in file, iterate through each ch, and add the int of that to a list, append that list to topo

rowNum = len(topo)
colNum = len(topo[0])

# making coordinate matrix
sortedCoords = []
for height in range(10):
    coordLine = []
    for i in range(len(topo)):  
        for j in range(len(topo[0])): 
            if topo[i][j] == height:  
                coordLine.append((i, j))
    sortedCoords.append(coordLine)

# adjacent check
def adjacent(coord1, coord2):
    r1, c1 = coord1  # getting the two components of the coordinate 
    r2, c2 = coord2
    if (abs(r1 - r2) == 1 and c1 == c2) or (abs(c1 - c2) == 1 and r1 == r2):  # if the rows are 1 apart and column same OR column 1 apart row same
        return True
    else:
        return False  # coordinates are not adjacent

# initialising
popularity = 0 
completionist = 0 

for trailhead in sortedCoords[0]:  # each coordinate in sortedCoords[0]
    current = [trailhead]  # restarting our current to just the trailhead 
    for height in range(9):  # climb from 1 to 9
        nextLvl = []
        for coord in current:  # for the coordinate (r, c) in our list current [(r,c) (r,c) (r,c)] etc
            for candidate in sortedCoords[height + 1]:  # our candidate coordinate in the next row of our sortedcoords list
                if adjacent(coord, candidate):  # if adj function returns true (aka our coordinate is adjacent to the one that's +1 height)
                    nextLvl.append(candidate)  # add it to the next level
        current = nextLvl[:]  # making sure in memory current is a completely new list with what we found is in the next level

    popularity += len(set(current))  # length of current is how many summits were reached from one trailhead, we add onto it with each trailhead (but set so no duplicate)
    completionist += len(current)  # with duplicates for completionist

print("Total Popularity Score:", popularity)
print("Total Completionist Score:", completionist)