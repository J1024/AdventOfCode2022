#################################
###Advent of Code Day 10
###Start Time: 11:23pm
###End Time: 12:44am
###Author: Jonathan LeFeber
###Lines of Code: 62
#################################
import time

f = open("Puzzle10Input.txt", "r")
cycle = 1
x = 1
sumSignal = 0
carryOn = True
while cycle < 250:
    if cycle/20 in [1,3,5,7,9,11]:
        sumSignal += (cycle * x)
        #print("Sum of signals (so far): ",(cycle*x),sumSignal,cycle,x)
    if carryOn:
        instruction = f.readline()
        if instruction[:4] == "addx":
            carryOn = False
    else:
        change = int(instruction[5:])
        x += change
        carryOn = True
    cycle += 1
print("Sum of signals: ",sumSignal,"\n")
f.close()



f = open("Puzzle10Input.txt", "r")
cycle = 1
x = 1
resume = 0
screen = []
while cycle <= 240:
    #Begin Execution First (but ordered last)
    if resume < cycle:
        instruction = f.readline()
        if instruction[:4] == "addx":
            resume = cycle+1
    #print("Cycle, X          : ",cycle,x)
    #Draw Pixel Second (but ordered first)
    position = (cycle%40)-1
    if position == x or position == x+1 or position == x-1:
        #print(screen,cycle)
        screen.append("#")
    else:
        screen.append(".")
    
    #Finish Execution if necessary 
    if resume == cycle:
        change = int(instruction[5:])
        x += change
        #print("Change: ",change)
    #print("Cycle, X, Position: ",cycle,x,position,screen[cycle-1])
    cycle += 1

#Print a nice screen
screenPrint = []
for y in range(6):
    screenPrint.append("")
    for z in range(40):
        screenPrint[y] = screenPrint[y]+screen[(y*40)+z]
for y in range(6):
    print(screenPrint[y])
print("\n",time.process_time())