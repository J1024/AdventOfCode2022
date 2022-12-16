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
#print(lines)
#print(start)
lines[start[1]][start[0]]+="0"
#print(lines[start[1]][start[0]])
distance = 0
shortestDistance = 10000
haveBeenTo = []
#solved = False
#print("Hung here: ",lines[0][5])
maxDistance = 450

height = ['S','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','E']
#print("Height: ",height)

#References TO LINES SPECIFICALLY need to be in Y/X. Coords are generally stored as X/Y though.
def pathFromHere(coords,distance,haveBeen):
    #Always going to add 1 to distance, so might as well do that first
    #distance += 1
    #Append where we are to haveBeen
    #haveBeen.append(coords)
    #Define directions
    left = [coords[0]-1,coords[1]]
    right = [coords[0]+1,coords[1]]
    up = [coords[0],coords[1]-1]
    down = [coords[0],coords[1]+1]
    #check for edges of map, or if result == Z, or if haveBeen
    #TODO Add logic for 'if more then +1 height change, can't go that direction.
    #print("Checking Coords: ",coords," Letter: ",lines[coords[1]][coords[0]][:1]," Distance: ",distance)
    
    #Star 2
    #if lines[coords[1]][coords[0]][:1] == "a":
    #    lines[coords[1]][coords[0]] = "a0"
    #    
    #End Star 2
    if int(lines[coords[1]][coords[0]][1:]) > maxDistance:
        return distance
    
    
    
    
    #RIGHT
    #print("Checking RIGHT: ",right," from ",coords)
    
    if right[0] < len(lines[0]) and height.index(lines[right[1]][right[0]][:1])-1 <= height.index(lines[coords[1]][coords[0]][:1]):
        #print(" Letter Index:",height.index(lines[right[1]][right[0]][:1])," Value:",lines[right[1]][right[0]])
        if lines[right[1]][right[0]] == "E":
            distance += 1
            print("Found Z next to ",coords,int(lines[coords[1]][coords[0]][1:])+1)
            return distance
        elif len(lines[right[1]][right[0]]) == 1:
            lines[right[1]][right[0]]=lines[right[1]][right[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing RIGHT, new distance:",right)
            pathFromHere(right,distance+1,haveBeen)
        elif int(lines[right[1]][right[0]][1:]) > int(lines[coords[1]][coords[0]][1:])+1:
            lines[right[1]][right[0]]=lines[right[1]][right[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing RIGHT, better distance:",right,lines[right[1]][right[0]])
            pathFromHere(right,distance+1,haveBeen)
            
    #UP
    #print("Checking UP: ",up," from ",coords)
    if up[1] >= 0 and height.index(lines[up[1]][up[0]][:1])-1 <= height.index(lines[coords[1]][coords[0]][:1]):
        #print(" Letter Index:",height.index(lines[up[1]][up[0]][:1])," Value:",lines[up[1]][up[0]])
        if lines[up[1]][up[0]] == "E":
            distance += 1
            print("Found Z next to ",coords,int(lines[coords[1]][coords[0]][1:])+1)
            return distance
        elif len(lines[up[1]][up[0]]) == 1:
            lines[up[1]][up[0]]=lines[up[1]][up[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing UP, new distance:",up)
            pathFromHere(up,distance+1,haveBeen)
        elif int(lines[up[1]][up[0]][1:]) > int(lines[coords[1]][coords[0]][1:])+1:
            lines[up[1]][up[0]]=lines[up[1]][up[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing UP, better distance:",up,lines[up[1]][up[0]])
            pathFromHere(up,distance+1,haveBeen)
            
    #DOWN
    #print("Checking DOWN: ",down," from ",coords)
    if down[1] < len(lines) and height.index(lines[down[1]][down[0]][:1])-1 <= height.index(lines[coords[1]][coords[0]][:1]):
        #print(" Letter Index:",height.index(lines[down[1]][down[0]][:1])," Value:",lines[down[1]][down[0]])
        if lines[down[1]][down[0]] == "E":
            distance += 1
            print("Found Z next to ",coords,int(lines[coords[1]][coords[0]][1:])+1)
            return distance
        elif len(lines[down[1]][down[0]]) == 1:
            lines[down[1]][down[0]]=lines[down[1]][down[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing DOWN, new distance:",down)
            pathFromHere(down,distance+1,haveBeen)
        elif int(lines[down[1]][down[0]][1:]) > int(lines[coords[1]][coords[0]][1:])+1:
            lines[down[1]][down[0]]=lines[down[1]][down[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing DOWN, better distance:",down,lines[down[1]][down[0]])
            pathFromHere(down,distance+1,haveBeen)
    
    #LEFT
    #print("Checking LEFT: ",left," from ",coords,"Other Checks: ",left[0],height.index(lines[left[1]][left[0]][:1])-1,height.index(lines[coords[1]][coords[0]][:1]))
    if left[0] >= 0 and height.index(lines[left[1]][left[0]][:1])-1 <= height.index(lines[coords[1]][coords[0]][:1]):
        #print(" Letter Index:",height.index(lines[left[1]][left[0]][:1])," Value:",lines[left[1]][left[0]])
        if lines[left[1]][left[0]] == "E":
            distance += 1
            print("Found Z next to ",coords,int(lines[coords[1]][coords[0]][1:])+1)
            return distance
        elif len(lines[left[1]][left[0]]) == 1:
            lines[left[1]][left[0]]=lines[left[1]][left[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing LEFT, new distance:",left)
            pathFromHere(left,distance+1,haveBeen)
        elif int(lines[left[1]][left[0]][1:]) > int(lines[coords[1]][coords[0]][1:])+1:
            lines[left[1]][left[0]]=lines[left[1]][left[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing LEFT, better distance:",left,lines[left[1]][left[0]])
            pathFromHere(left,distance+1,haveBeen)
    

    return distance
    
result = pathFromHere(start,distance,haveBeenTo)
print("Shortest path is distance ",result)
#print(lines[2][4])
#print(lines[1][4])



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