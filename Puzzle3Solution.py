#################################
###Advent of Code Day 3
###Start Time: 12:27am
###End Time: 1:20am
###Author: Jonathan LeFeber
###Lines of Code: 49
#################################
import time
totalPriority = 0
priority = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
f = open("Puzzle3Input.txt", "r")
for rucksack in f:
    half = (len(rucksack.strip()))/2
    leftRuck = rucksack[:int(half)]
    rightRuck = rucksack[int(half):]
    duplicate = ''
    for left in leftRuck:
        for right in rightRuck:
            if left == right:
                duplicate = left
                break
        if duplicate != '':
            break
            
    totalPriority += priority.index(duplicate)
    #print(duplicate,priority.index(duplicate),totalPriority)
print("Total Individual Priority: ", totalPriority)
f.close()


totalPriority = 0
priority = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
f = open("Puzzle3Input.txt", "r")
while True:
    duplicate = ''
    firstSack = f.readline()
    secondSack = f.readline()
    thirdSack = f.readline()
    if not firstSack:
        break
    for first in firstSack:
        for second in secondSack:
            if first == second:
                for third in thirdSack:
                    if first == third:
                        duplicate = third
                        break
            if duplicate != '':
                break
        if duplicate != '':
            break
    totalPriority += priority.index(duplicate)
    print(duplicate,priority.index(duplicate),totalPriority)
print("Total Group Priority: ", totalPriority)
f.close()
print(time.process_time())