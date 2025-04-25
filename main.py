smallFile = "small.txt"
largeFile = "large.txt"

# extracting the topographical data into a list
topo = []
with open(smallFile) as fin:
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

# functions to check the height of an adjacent square
def checkRight(pos, topo, height):
    if pos[1] < 7:  # checking boundary conditions
        if topo[pos[0]][(pos[1] + 1)] == height + 1:  # checking if the height right of the position is +1 
            return True


def checkLeft(pos, topo, height):
    if pos[1] > 0:  # checking boundary conditions
        if topo[pos[0]][(pos[1] - 1)] == height + 1:  # checking if the height left of the position is +1 
            return True

def checkDown(pos, topo, height):
    if pos[0] < 7:  # checking boundary conditions
        if topo[(pos[0] + 1)][pos[1]] == height + 1:  # checking if the height below the position is +1 
            return True

def checkUp(pos, topo, height):
    if pos[0] > 0:  # checking boundary conditions
        if topo[(pos[0] - 1)][pos[1]] == height + 1:  # checking if the height above the position is +1 
            return True

# popularity = []

run = True
pos = trailheads[0]
height = 0
summits = 0

while run:
    print(pos)
    if checkRight(pos, topo, height):  # right
        height = topo[pos[0]][(pos[1] + 1)]
        pos = (pos[0], (pos[1] + 1))
    elif checkLeft(pos, topo, height):  # left
        height = topo[pos[0]][(pos[1] - 1)]
        pos = (pos[0], (pos[1] - 1))
    elif checkDown(pos, topo, height):  # down
        height = topo[(pos[0] + 1)][pos[1]]
        pos = ((pos[0] + 1), pos[1])
    elif checkUp(pos, topo, height):  # up
        height = topo[(pos[0] - 1)][pos[1]]
        pos = ((pos[0] - 1), pos[1])
    elif height == 9:  # if we reach a summit
        summits = summits + 1
        run = False
    else:
        run = False

print(summits)

# finding how many summits can be reached by each trailhead 
# for head in trailheads:
#     pos = head  # when we start with a new trailhead, we set that as our initial position
#     height = 0  # since it's a trailhead its height will always be 0
#     summits = 0
#     run = True

#     print(pos)

#     while run:
#         if checkRight(pos, topo, height):  # right
#             height = topo[pos[0]][(pos[1] + 1)]
#             pos = (pos[0], (pos[1] + 1))
        
#         else:
#             run = False
        
    #     pos, height = checkLeft(pos, topo, height)  # left
    #     pos, height = checkDown(pos, topo, height)  # down
    #     pos, height = checkUp(pos, topo, height)  # up
        
    #     if height == 9:
    #         summits = summits + 1
    #         run = False
    
    # popularity.append(summits)

# print(popularity)