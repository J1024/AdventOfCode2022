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
path = ""
#solved = False
#print("Hung here: ",lines[0][5])
maxDistance = 485

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
    #     lines[coords[1]][coords[0]] = "a0"
    #End Star 2
    #This didn't work at all.... but a pretty basic review of the data shows that there are only 'b's in the second column... so really we just needed to count up/down to get to whatever the shortest path is to go right across the majority of the map.... thus, previous answer -6 for my data....
    if int(lines[coords[1]][coords[0]][1:]) > maxDistance:
        return distance
    
    
    #for x in range(len(lines)):
    #    print(''.join(lines[x]))
    #print("\n\n\n\n\n")
    #sleep(100)
    
    #RIGHT
    #print("Checking RIGHT: ",right," from ",coords)
    
    if right[0] < len(lines[0]) and height.index(lines[right[1]][right[0]][:1])-1 <= height.index(lines[coords[1]][coords[0]][:1]):
        #print(" Letter Index:",height.index(lines[right[1]][right[0]][:1])," Value:",lines[right[1]][right[0]])
        if lines[right[1]][right[0]] == "E":
            print("Found Z next to ",coords,int(lines[coords[1]][coords[0]][1:])+1)
            return
        elif len(lines[right[1]][right[0]]) == 1:
            lines[right[1]][right[0]]=lines[right[1]][right[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing RIGHT, new distance:",right)
            pathFromHere(right,distance+1,haveBeen)
        elif int(lines[right[1]][right[0]][1:]) > int(lines[coords[1]][coords[0]][1:])+1:
            lines[right[1]][right[0]]=lines[right[1]][right[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing RIGHT, better distance:",right,lines[right[1]][right[0]])
            pathFromHere(right,distance+1,haveBeen)
            
    #DOWN
    #print("Checking DOWN: ",down," from ",coords)
    if down[1] < len(lines) and height.index(lines[down[1]][down[0]][:1])-1 <= height.index(lines[coords[1]][coords[0]][:1]):
        #print(" Letter Index:",height.index(lines[down[1]][down[0]][:1])," Value:",lines[down[1]][down[0]])
        if lines[down[1]][down[0]] == "E":
            print("Found Z next to ",coords,int(lines[coords[1]][coords[0]][1:])+1)
            return
        elif len(lines[down[1]][down[0]]) == 1:
            lines[down[1]][down[0]]=lines[down[1]][down[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing DOWN, new distance:",down)
            pathFromHere(down,distance+1,haveBeen)
        elif int(lines[down[1]][down[0]][1:]) > int(lines[coords[1]][coords[0]][1:])+1:
            lines[down[1]][down[0]]=lines[down[1]][down[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing DOWN, better distance:",down,lines[down[1]][down[0]])
            pathFromHere(down,distance+1,haveBeen)
            
    #UP
    #print("Checking UP: ",up," from ",coords)
    if up[1] >= 0 and height.index(lines[up[1]][up[0]][:1])-1 <= height.index(lines[coords[1]][coords[0]][:1]):
        #print(" Letter Index:",height.index(lines[up[1]][up[0]][:1])," Value:",lines[up[1]][up[0]])
        if lines[up[1]][up[0]] == "E":
            print("Found Z next to ",coords,int(lines[coords[1]][coords[0]][1:])+1)
            return
        elif len(lines[up[1]][up[0]]) == 1:
            lines[up[1]][up[0]]=lines[up[1]][up[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing UP, new distance:",up)
            pathFromHere(up,distance+1,haveBeen)
        elif int(lines[up[1]][up[0]][1:]) > int(lines[coords[1]][coords[0]][1:])+1:
            lines[up[1]][up[0]]=lines[up[1]][up[0]][:1]+str(int(lines[coords[1]][coords[0]][1:])+1)
            #print("Recursing UP, better distance:",up,lines[up[1]][up[0]])
            pathFromHere(up,distance+1,haveBeen)
    
    #LEFT
    #print("Checking LEFT: ",left," from ",coords,"Other Checks: ",left[0],height.index(lines[left[1]][left[0]][:1])-1,height.index(lines[coords[1]][coords[0]][:1]))
    if left[0] >= 0 and height.index(lines[left[1]][left[0]][:1])-1 <= height.index(lines[coords[1]][coords[0]][:1]):
        #print(" Letter Index:",height.index(lines[left[1]][left[0]][:1])," Value:",lines[left[1]][left[0]])
        if lines[left[1]][left[0]] == "E":
            print("Found Z next to ",coords,int(lines[coords[1]][coords[0]][1:])+1)
            return
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
for x in range(len(lines)):
    print(','.join(lines[x]))

print("\n",time.process_time())