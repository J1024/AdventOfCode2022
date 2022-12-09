#################################
###Advent of Code Day 8
###Start Time: 10:00am
###End Time: 11:30am
###Author: Jonathan LeFeber
###Lines of Code: 109
#################################
import time
headLocation = [0,0]
tailLocation = [0,0]
hasBeen = []
f = open("Puzzle9Input.txt", "r")
for line in f:
    line = line.strip()
    moves = int(line[2:])
    direction = line[:1]
    print("Head is at: ",headLocation)
    print("Tail is at: ",tailLocation)
    print("Moving ",moves," times in ",direction," direction")
    for move in range(moves):
        #MoveHead
        if direction == "L":
            headLocation[0] -= 1
        elif direction == "R":
            headLocation[0] += 1
        elif direction == "U":
            headLocation[1] += 1
        elif direction == "D":
            headLocation[1] -= 1
        #MoveTail
        #If I'm 2 away or greater, I need to catchup
        if tailLocation[0] 






"""

forrest = []
forrestLine = []
visibleTrees = 0
f = open("Puzzle8Input.txt", "r")
x = 0
y = 0
for line in f:
    forrestLine = []
    for c in line.strip():
        #print(c)
        forrestLine.append([int(c),' '])
    forrest.append(forrestLine)
    y += 1
    

#for z in range(len(forrest)):
#    print(forrest[z])


#Check Left-to-Right
for y in range(1,len(forrest)-1):
    tallest = forrest[y][0][0]
    for x in range(1, len(forrestLine)-1):
        if forrest[y][x][0] > forrest[y][x-1][0] and forrest[y][x][0] > tallest:
            #print("1st > 2nd: ",forrest[y][x][0],forrest[y][x-1][0])
            tallest =  forrest[y][x][0]
            forrest[y][x][1] = "x"

#Check Right-to-Left
for y in range(1,len(forrest)-1):
    tallest = forrest[y][len(forrestLine)-1][0]
    for x in range(len(forrestLine)-2,0,-1):
        if forrest[y][x][0] > forrest[y][x+1][0] and forrest[y][x][0] > tallest:
            #print("1st > 2nd: ",forrest[y][x][0],forrest[y][x+1][0])
            tallest =  forrest[y][x][0]
            forrest[y][x][1] = "x"

#Check Up-to-Down
for x in range(1,len(forrestLine)-1):
    tallest = forrest[0][x][0]
    for y in range(1,len(forrest)-1):
        if forrest[y][x][0] > forrest[y-1][x][0] and forrest[y][x][0] > tallest:
            #print("1st > 2nd: ",forrest[y][x][0],forrest[y-1][x][0])
            tallest =  forrest[y][x][0]
            forrest[y][x][1] = "x"

#Check Down-to-Up
for x in range(1,len(forrestLine)-1):
    tallest = forrest[len(forrest)-1][x][0]
    for y in range(len(forrest)-2,0,-1):
        if forrest[y][x][0] > forrest[y+1][x][0] and forrest[y][x][0] > tallest:
            #print("1st > 2nd: ",forrest[y][x][0],forrest[y+1][x][0])
            tallest =  forrest[y][x][0]
            forrest[y][x][1] = "x"


#Visible Count
edgeTrees = (2*len(forrest))+(2*len(forrestLine))-4
print("Edge Trees: ",edgeTrees)
#Count the Xs
for y in range(len(forrest)):
    for x in range(len(forrestLine)):
        if forrest[y][x][1] == "x":
            edgeTrees += 1
print("Total Visible Trees: ",edgeTrees)

#Best TreeHouse Location Go:
for y in range(len(forrest)):
    for x in range(len(forrestLine)):
        if y != 0 and x != 0 and y != len(forrest)-1 and x != len(forrestLine)-1:
            #Checking values for forrest[y][x]:
            treeHeight = forrest[y][x][0]
            North = 0
            South = 0
            East = 0
            West = 0
            #Check North
            for why in range(y,0,-1):
                North += 1
                if forrest[why-1][x][0] >= forrest[y][x][0]:
                    break
            #Check West
            for ex in range(x,0,-1):
                West += 1
                if forrest[y][ex-1][0] >= forrest[y][x][0]:
                    break
            #Check East
            for ex in range(x,len(forrestLine)-1):
                East += 1
                if forrest[y][ex+1][0] >= forrest[y][x][0]:
                    break
            #Check South
            for why in range(y,len(forrest)-1):
                South += 1
                if forrest[why+1][x][0] >= forrest[y][x][0]:
                    break
            socialScore = North*South*East*West
            forrest[y][x][1] = socialScore

#Find Largest Social Score TODO: I could build this into the above easily enough.... saves having to walk the array AGAIN.
best = 0
for y in range(len(forrest)):
    for x in range(len(forrestLine)):
        if forrest[y][x][1] != ' ' and int(forrest[y][x][1]) > best:
            best = int(forrest[y][x][1])
print("Best Social Score: ",best)
"""
print(time.process_time())