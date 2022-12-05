#################################
###Advent of Code Day 5
###Start Time: 11:08pm
###End Time: 2:03am
###Author: Jonathan LeFeber
###Lines of Code: 34
#################################
import time
fullyOverlapPair = 0
f = open("Puzzle5Input.txt", "r")
stackLines = []
while True:
    checkLine = f.readline()
    if checkLine == '\n':
        break
    else:
        stackLines.append(checkLine)
#print(stackLines)
stackHeight = len(stackLines)-1
print("Stack Height: ",stackHeight)
#Do not look upon my shame.
numStacks = int((len(stackLines[len(stackLines)-1].strip())+3)/4)
print("Number of Stacks: ",numStacks)

stacks = ['']*numStacks
#print(stacks)
for x in range(stackHeight-1,-1,-1):
    #print(stackLines[x])
    for y in range(numStacks):
        #print("Y:",y)
        if stackLines[x][y+1+(3*y)] != ' ':
            stacks[y]+=(stackLines[x][y+1+(3*y)])
print("Starting Stacks: ",stacks)

def CM9000():
    #We finally have the stacks in the 'stacks' array... now let's work on them.
    for action in f:
        #print("Starting Stacks: ",stacks)
        action = action[5:]
        #print(action)
        if action[1:2] == ' ':
            moves = int(action[:1])
            action = action[7:]
        else:
            moves = int(action[:2])
            action = action[8:]
        fromStack = int(action[:1])
        toStack = int(action[5:6])
        #print("Moves: ",moves)
        #print("From: ",fromStack)
        #print("To: ", toStack)
        for z in range(moves):
            #print("What is being moved: ",stacks[fromStack-1][len(stacks[fromStack-1])-1:])
            stacks[toStack-1] += stacks[fromStack-1][len(stacks[fromStack-1])-1:]
            stacks[fromStack-1] = stacks[fromStack-1][:len(stacks[fromStack-1])-1]
            #print("Removed stack after move: ",stacks[fromStack-1][:len(stacks[fromStack-1])])
        #print("Ending Stacks: ",stacks)
    print("Ending CM9000 Stacks: ",stacks)

def CM9001():
    #We finally have the stacks in the 'stacks' array... now let's work on them.
    for action in f:
        #print("Starting Stacks: ",stacks)
        action = action[5:]
        #print(action)
        if action[1:2] == ' ':
            moves = int(action[:1])
            action = action[7:]
        else:
            moves = int(action[:2])
            action = action[8:]
        fromStack = int(action[:1])
        toStack = int(action[5:6])
        #print("Moves: ",moves)
        #print("From: ",fromStack)
        #print("To: ", toStack)
        #print("What is being moved: ",stacks[fromStack-1][len(stacks[fromStack-1])-moves:])
        stacks[toStack-1] += stacks[fromStack-1][len(stacks[fromStack-1])-moves:]
        stacks[fromStack-1] = stacks[fromStack-1][:len(stacks[fromStack-1])-moves]
        #print("Removed stack after move: ",stacks[fromStack-1][:len(stacks[fromStack-1])])
        #print("Ending Stacks: ",stacks)
    print("Ending CM9001 Stacks: ",stacks)
    
    
CM9001()

    
    
    
"""
for pair in f:
    left = pair[:pair.index(',')].strip()
    right = pair[pair.index(',')+1:].strip()
    leftLow = int(left[:left.index('-')])
    leftHigh = int(left[left.index('-')+1:])
    rightLow = int(right[:right.index('-')])
    rightHigh = int(right[right.index('-')+1:])
    if leftLow <= rightLow and leftHigh >= rightHigh:
        fullyOverlapPair += 1
    elif rightLow <= leftLow and rightHigh >= leftHigh:
        fullyOverlapPair += 1
print("Full Overlaps: ", fullyOverlapPair)
"""
f.close()
print(time.process_time())