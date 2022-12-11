#################################
###Advent of Code Day 11
###Start Time: 11:00pm
###End Time: 12:53am
###Author: Jonathan LeFeber
###Lines of Code: 94
#################################
import time
f = open("Puzzle11Input.txt", "r")
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
print("\n",time.process_time())