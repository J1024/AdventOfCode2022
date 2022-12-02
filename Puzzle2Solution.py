#################################
###Advent of Code Day 2
###Start Time: 7:15am
###End Time: 7:40am
###Author: Jonathan LeFeber
###Lines of Code: 56
#################################
import time

def callTheShots():
    totalScore = 0
    f = open("Puzzle2Input.txt", "r")
    for bout in f:
        stripBout = bout.strip()
        #print(stripBout)
        if stripBout == "A Y":
            totalScore += 8
        elif stripBout == "A X":
            totalScore += 4
        elif stripBout == "A Z":
            totalScore += 3
        elif stripBout == "B Y":
            totalScore += 5
        elif stripBout == "B X":
            totalScore += 1
        elif stripBout == "B Z":
            totalScore += 9
        elif stripBout == "C Y":
            totalScore += 2
        elif stripBout == "C X":
            totalScore += 7
        elif stripBout == "C Z":
            totalScore += 6
    f.close()
    print("Total Score: ",totalScore)

def callTheResults():
    totalScore = 0
    f = open("Puzzle2Input.txt", "r")
    for bout in f:
        stripBout = bout.strip()
        #print(stripBout)
        if stripBout == "A Y":
            totalScore += 4
        elif stripBout == "A X":
            totalScore += 3
        elif stripBout == "A Z":
            totalScore += 8
        elif stripBout == "B Y":
            totalScore += 5
        elif stripBout == "B X":
            totalScore += 1
        elif stripBout == "B Z":
            totalScore += 9
        elif stripBout == "C Y":
            totalScore += 6
        elif stripBout == "C X":
            totalScore += 2
        elif stripBout == "C Z":
            totalScore += 7
    f.close()
    print("Total Score: ",totalScore)
    
callTheShots()
callTheResults()
print(time.process_time())