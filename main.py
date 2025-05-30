smallFile = "small.txt"
largeFile = "large.txt"

# extracting the topographical data into a list
topo = []
with open(largeFile) as fin:
    for line in fin:  # for each line in the file we choose
        topo.append([int(ch) for ch in line.strip()])  # strip each line in file, iterate through each ch, and add the int of that to a list, append that list to topo

# finding trailheads
trailheads = []
for i in range(len(topo)):  # index value i for which row we're in
    for j in range(len(topo[0])):  # index value j for which column we're in
        if topo[i][j] == 0:  # if (i,j) in our map we load in is 0, it's a trailhead
            trailheads.append((i, j))

# functions to check if the height of an adjacent square is suitable
def checkRight(pos, topo, height):
    if pos[1] < (len(topo[0]) - 1):  # checking boundary conditions by comparing to length of first row (aka how many columns)
        if topo[pos[0]][(pos[1] + 1)] == height + 1:  # checking if the height right of the position is +1 
            return True
    return False

def checkLeft(pos, topo, height):
    if pos[1] > 0:  # checking boundary conditions
        if topo[pos[0]][(pos[1] - 1)] == height + 1:  # checking if the height left of the position is +1 
            return True
    return False

def checkDown(pos, topo, height):
    if pos[0] < (len(topo) - 1):  # checking boundary conditions by comparing to number of rows in topo 
        if topo[(pos[0] + 1)][pos[1]] == height + 1:  # checking if the height below the position is +1 
            return True
    return False

def checkUp(pos, topo, height):
    if pos[0] > 0:  # checking boundary conditions
        if topo[(pos[0] - 1)][pos[1]] == height + 1:  # checking if the height above the position is +1 
            return True
    return False


# get the coordinates of all possible next steps
def makeCoords(pos, topo, height):
    coords = []
    if checkRight(pos, topo, height):
        nextPos = (pos[0], (pos[1] + 1))
        coords.append(nextPos)
    if checkLeft(pos, topo, height):
        nextPos = (pos[0], (pos[1] - 1))
        coords.append(nextPos)
    if checkDown(pos, topo, height):
        nextPos = ((pos[0] + 1), pos[1])
        coords.append(nextPos)
    if checkUp(pos, topo, height):
        nextPos = ((pos[0] - 1), pos[1])
        coords.append(nextPos)
    return coords

# getting the popularity and completionist scores
popularityScore = []
completionistScore = []

for head in trailheads:  # repeating this loop for each trailhead
    runPopularity = True
    runCompletionist = True

    # reset for popularity
    height = 0  # whenever we have a new trailhead the height is 0
    coords = [head]  # our starting coordinate is our trailhead
    while runPopularity:
        nextCoords = []  # resetting all possible next moves

        for coordinate in coords:
            options = makeCoords(coordinate, topo, height)  # adding all possible options

            for option in options:  # making sure we don't double up 
                if option not in nextCoords:
                    nextCoords.append(option)  # adds the elements in option one by one instad of the list of options (as in append)

        coords = nextCoords  # setting our new set of coordinates to our next possible moves 
        height = height + 1  # adjusting our height 

        if height == 9:  # check whether we reached a summit
            popularityScore.append(len(nextCoords))  # coords will be a list with all possible summits
            runPopularity = False
    
    # reset for completionist
    height = 0  # whenever we have a new trailhead the height is 0
    coords = [head]  # our starting coordinate is our trailhead
    while runCompletionist:
        nextCoords = []  # resetting all possible next moves

        for coordinate in coords:
            nextCoords.extend(makeCoords(coordinate, topo, height))  # adding all possible options instad of the list of options (as in append)

        coords = nextCoords  # setting our new set of coordinates to our next possible moves 
        height = height + 1  # adjusting our height 

        if height == 9:  # check whether we reached a summit
            completionistScore.append(len(nextCoords))
            runCompletionist = False

print("Popularity score:", sum(popularityScore))
print("Completionist score:", sum(completionistScore))