smallFile = "small.txt"
largeFile = "large.txt"

# extracting the topographical data into a list
topo = []
with open(largeFile) as fin:
    for line in fin:  # for each line in the file we choose
        line = line.strip()  # remove any non-number stuff
        topoRow = []  # make a mini list for each line 
        for ch in line:  # for each character in our line
            topoRow.append(int(ch))  # add this character as an integer to the list with our row
        topo.append(topoRow)  # add the completed row list to our topo data list

# finding trailheads
trailheads = []
for idxRow, row in enumerate(topo):  # storing the row number and iterating through each row
    for idxCol, num in enumerate(row):  # idx is the counter and num is the element in the list topo
        if num == 0:
            trailheads.append((idxRow, idxCol))  # adding the counter value (which is the index) for each time we find a zero

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
    run = True
    height = 0  # whenever we have a new trailhead the height is 0
    coords = [head]  # our starting coordinate is our trailhead
    
    while run:
        nextCoords = []  # resetting all possible next moves

        for coordinate in coords:
            options = makeCoords(coordinate, topo, height)  # adding all possible options

            # nextCoords.extend(options) # for the completitionist score

            # for the popularity score
            options = makeCoords(coordinate, topo, height)  # possible next coordinates from the coord
            for option in options:  # making sure we don't double up 
                if option not in nextCoords:
                    nextCoords.append(option)  # adds the elements in option one by one instad of the list of options (as in append)

        coords = nextCoords  # setting our new set of coordinates to our next possible moves 
        height = height + 1  # adjusting our height 

        if height == 9:  # check whether we reached a summit
            popularityScore.append(len(nextCoords))  # coords will be a list with all possible summits
            # completionistScore.append(len(nextCoordsCompletionist))
            run = False
    
    # while run:
    #     # resetting all possible next moves
    #     nextCoordsPopularity = []  # no duplicates allowed
    #     nextCoordsCompletionist = []  # duplicates allowed

    #     for coordinate in coords:
    #         options = makeCoords(coordinate, topo, height)  # adding all possible options

    #         # for the completitionist score
    #         nextCoordsCompletionist.extend(options)

    #         # for the popularity score
    #         options = makeCoords(coordinate, topo, height)  # possible next coordinates from the coord
    #         for option in options:  # making sure we don't double up 
    #             if option not in nextCoordsPopularity:
    #                 nextCoordsPopularity.append(option)  # adds the elements in option one by one instad of the list of options (as in append)

    #     coords = nextCoordsPopularity  # setting our new set of coordinates to our next possible moves 
    #     completionistScore.append(len(nextCoordsCompletionist))
    #     height = height + 1  # adjusting our height 

    #     if height == 9:  # check whether we reached a summit
    #         popularityScore.append(len(nextCoordsPopularity))  # coords will be a list with all possible summits
    #         # completionistScore.append(len(nextCoordsCompletionist))
    #         run = False

print("Popularity score:", sum(popularityScore))
print("Completionist score:", sum(completionistScore))
