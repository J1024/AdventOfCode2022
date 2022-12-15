#################################
###Advent of Code Day 12
###Start Time: 11:00pm
###End Time: 12:53am
###Author: Jonathan LeFeber
###Lines of Code: 94
#################################

import time
lines = open("Puzzle12Input.txt", "r").read().split("\n")
for y in range(len(lines)):
    lines[y] = list(lines[y])
    if "S" in lines[y]:
        start = [lines[y].index("S"),y]
print(lines)
print(start)
print(start[0])
print(start[1])
print(lines[start[0]][start[1]])
distance = 0
shortestDistance = 10000
haveBeen = []
#solved = False

def pathFromHere(coords,distance,haveBeen):
    #Always going to add 1 to distance, so might as well do that first
    distance += 1
    #Append where we are to haveBeen
    haveBeen.append(coords)
    #Define directions
    left = [coords[0]-1,coords[1]]
    right = [coords[0]+1,coords[1]]
    up = [coords[0],coords[1]-1]
    down = [coords[0],coords[1]+1]
    #check for edges of map, or if result == Z, or if haveBeen
    if left[0] < 0 or left in haveBeen:
        print("LEFT Outside of the edges, or have been here before:",left)
    else:
        print("Recursing LEFT:",left)
        distance += pathFromHere(left,distance,haveBeen)
    if right[0] >= len(lines[0]) or right in haveBeen:
        print("RIGHT Outside of the edges, or have been here before:",right)
    else:
        print("Recursing RIGHT:",right)
        distance += pathFromHere(right,distance,haveBeen)
    if up[1] < 0 or up in haveBeen:
        print("UP Outside of the edges, or have been here before:",up)
    else:
        print("Recursing UP:",up)
        distance += pathFromHere(up,distance,haveBeen)
    if down[1] >= len(lines) or down in haveBeen:
        print("DOWN Outside of the edges, or have been here before:",down)
    else:
        print("Recursing DOWN:",down)
        distance += pathFromHere(down,distance,haveBeen)
    
    
    
    #If Z is in any direction that is legal, just need to increment distance and return, don't need to know which direction.
    #TODO: Need to check these before recursing, but need to know if they exist first...
    if lines[left[0]][left[1]] == "E" or lines[right[0]][right[1]] == "E" or lines[up[0]][up[1]] == "E" or lines[down[0]][down[1]] == "E":
        print("Found Z next to ",coords)
        distance += 1
        return distance
    return -1
    
result = pathFromHere(start,distance,haveBeen)
print("Shortest path is distance ",result)



"""
monkeys = []
roundNum = 1
for line in f:
    if line[:6] == "Monkey":
        nextLine = f.readline()
        items = nextLine[18:].strip().split(", ")
        #print(items)
        
        #Star 2: Adding a 'trillions' counter
        for item in items:
            item = [item,0]
            
            
        nextLine = f.readline()
        operation = nextLine[19:].strip().split(" ")
        #print(operation)
        nextLine = f.readline()
        test = int(nextLine[21:].strip())
        #print(test)
        nextLine = f.readline()
        ifTrue = int(nextLine[29:].strip())
        #print(ifTrue)
        nextLine = f.readline()
        ifFalse = int(nextLine[30:].strip())
        #print(ifFalse)
        monkeys.append([items,operation,test,ifTrue,ifFalse,0])
#for x in range(len(monkeys)):
#    print(monkeys[x])

itemsNum = 0
operations = 1
tests = 2
ifTrues = 3
ifFalses = 4
worryCounter = 5

#Credit to 'hyper-neutrino' for this code. I did not understand this math, or how to reduce the 'item numbers'. Based on reading his code I now understand it.
#https://github.com/hyper-neutrino/advent-of-code/blob/main/2022/day11p2.py
modNum = 1
for monkey in monkeys:
    modNum *= int(monkey[tests])
print("ModNum = :",modNum)

while roundNum <= 10000:
    #print("Round Num: ",roundNum)
    for monkey in monkeys:
        while len(monkey[itemsNum]) > 0:
            item = monkey[itemsNum][0]
            #Remove Item from Inventory... it's going somewhere
            monkey[itemsNum].remove(item)
            #Perform Worry Operation and increment inspection counter
            monkey[worryCounter] += 1
            if monkey[operations][2] == "old":
                if monkey[operations][1] == "+":
                    item = int(item)*2
                else: # == *
                    item = int(item)*int(item)
            else: #== int
                if monkey[operations][1] == "+":
                    item = int(item)+int(monkey[operations][2])
                else: # == *
                    item = int(item)*int(monkey[operations][2])
            #Perform Worry Reduction
            
            #STAR 1 Method:
            #item = int(item/3)
            #STAR 2 Method
            item = item%modNum
            
            #Perform Test
            if item%int(monkey[tests]) == 0:
                toMonkey = int(monkey[ifTrues])
                #Star 2 attempts:
                #item = int(monkey[tests])*10
                monkeys[toMonkey][0].append(item)
            else: #Test failed
                #Star 2 attempts:
                #while item > int(monkey[tests])*10:
                #    item = item-(int(monkey[tests])*10)
                toMonkey = int(monkey[ifFalses])
                monkeys[toMonkey][0].append(item)
    roundNum += 1
    
#Calculate
totalWorry = []
for x in range(len(monkeys)):
    print(monkeys[x])
for x in range(len(monkeys)):
    totalWorry.append(monkeys[x][worryCounter])
totalWorry.sort()
print(totalWorry)
"""
print("\n",time.process_time())