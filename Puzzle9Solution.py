#################################
###Advent of Code Day 9
###Start Time: 3:00pm
###End Time: 11:15pm
###Author: Jonathan LeFeber
###Lines of Code: 71
#################################
import time
numKnots = 10
ropeLocation = []
for x in range(numKnots):
    ropeLocation.append([0,0])
hasBeen = ["0/0"]
f = open("Puzzle9Input.txt", "r")
for line in f:
    line = line.strip()
    moves = int(line[2:])
    direction = line[:1]
    for move in range(moves):
        #MoveHead
        if direction == "L":
            ropeLocation[0][0] -= 1
        elif direction == "R":
            ropeLocation[0][0] += 1
        elif direction == "U":
            ropeLocation[0][1] += 1
        elif direction == "D":
            ropeLocation[0][1] -= 1
        #Loop through all following knots
        for knotNum in range(1,numKnots):
            #MoveTail(s)
            #If I'm 2 away or greater, I need to move
            if abs(ropeLocation[knotNum-1][0] - ropeLocation[knotNum][0]) > 1 or abs(ropeLocation[knotNum-1][1] - ropeLocation[knotNum][1]) > 1:
                #If I'm >= 1 away in two directions, I need to move diagonally
                if abs(ropeLocation[knotNum-1][0] - ropeLocation[knotNum][0]) >= 1 and abs(ropeLocation[knotNum-1][1] - ropeLocation[knotNum][1]) >= 1:
                    if ropeLocation[knotNum-1][0] > ropeLocation[knotNum][0] and ropeLocation[knotNum-1][1] > ropeLocation[knotNum][1]:
                        #x and y + 1
                        ropeLocation[knotNum][0] = ropeLocation[knotNum][0]+1
                        ropeLocation[knotNum][1] = ropeLocation[knotNum][1]+1
                    elif ropeLocation[knotNum-1][0] < ropeLocation[knotNum][0] and ropeLocation[knotNum-1][1] < ropeLocation[knotNum][1]:
                        #x and y - 1
                        ropeLocation[knotNum][0] = ropeLocation[knotNum][0]-1
                        ropeLocation[knotNum][1] = ropeLocation[knotNum][1]-1
                    elif ropeLocation[knotNum-1][0] > ropeLocation[knotNum][0] and ropeLocation[knotNum-1][1] < ropeLocation[knotNum][1]:
                        #x + 1 and y - 1
                        ropeLocation[knotNum][0] = ropeLocation[knotNum][0]+1
                        ropeLocation[knotNum][1] = ropeLocation[knotNum][1]-1
                    elif ropeLocation[knotNum-1][0] < ropeLocation[knotNum][0] and ropeLocation[knotNum-1][1] > ropeLocation[knotNum][1]:
                        #x - 1 and y + 1
                        ropeLocation[knotNum][0] = ropeLocation[knotNum][0]-1
                        ropeLocation[knotNum][1] = ropeLocation[knotNum][1]+1
                    else:
                        print("How did I get here: 1")
                #Otherwise I'm still 2 away, so just move towards numKnot-1    
                else:
                    if ropeLocation[knotNum-1][0] > ropeLocation[knotNum][0]:
                        ropeLocation[knotNum][0] = ropeLocation[knotNum][0]+1
                    elif ropeLocation[knotNum-1][0] < ropeLocation[knotNum][0]:
                        ropeLocation[knotNum][0] = ropeLocation[knotNum][0]-1
                    elif ropeLocation[knotNum-1][1] > ropeLocation[knotNum][1]:
                        ropeLocation[knotNum][1] = ropeLocation[knotNum][1]+1
                    elif ropeLocation[knotNum-1][1] < ropeLocation[knotNum][1]:
                        ropeLocation[knotNum][1] = ropeLocation[knotNum][1]-1
                    else:
                        print("How did I get here: 2")
                        print("Preceding Rope Location: ",ropeLocation[knotNum-1][0],ropeLocation[knotNum-1][1])
                        print("My Rope Location:        ",ropeLocation[knotNum][0],ropeLocation[knotNum][1])
            #Otherwise I'm not 2 away, didn't move, and can break 
            else:
                break
            
            #If I'm the tail, update tail tracker
            if knotNum == numKnots-1:
                tailString = str(ropeLocation[numKnots-1][0])+"/"+str(ropeLocation[numKnots-1][1])
                if tailString not in hasBeen:
                    hasBeen.append(tailString)
print("For ",numKnots,"knots, the tail has been in ",len(hasBeen)," locations.")
print(time.process_time())