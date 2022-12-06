#################################
###Advent of Code Day 6
###Start Time: 11:00pm
###End Time: 11:45pm
###Author: Jonathan LeFeber
###Lines of Code: 54
#################################
"""
#Keeping this code here since this is how I technically solved star 1, like a cannibal.
import time
marker = 0
x = 0
f = open("Puzzle6Input.txt", "r")
dataStream = f.readline()
print("DataStream Length: ",len(dataStream))
for x in range(len(dataStream)):
    print(x)
    if dataStream[x] == dataStream[x+1] or dataStream[x] == dataStream[x+2] or dataStream[x] == dataStream[x+3] or dataStream[x+1] == dataStream[x+2] or dataStream[x+1] == dataStream[x+3] or dataStream[x+2] == dataStream[x+3]:
        print("Not: ",dataStream[x:x+4])
    else:
        marker = x+4
        break
print("Characters: ",marker)
f.close()
print(time.process_time())
"""

def checkFirstToRest(checkString):
    noMatch = True
    for z in range(1,len(checkString)):
        if checkString[0] == checkString[z]:
            noMatch = False
            break
    if noMatch:
        return checkString[1:]
    else:
        return ""

#This WOULD be the one to screw me over for hard-coding the comparisons.....
import time
marker = 0
x = 0
#Change Marker Length for 1st/2nd test:
markerLength = 4
f = open("Puzzle6Input.txt", "r")
dataStream = f.readline()
print("DataStream Length: ",len(dataStream))
for x in range(len(dataStream)):
    subStringToCheck = dataStream[x:x+markerLength]
    checking = True
    while subStringToCheck:
        #print("Checking Substring: ",subStringToCheck,x)
        subStringToCheck = checkFirstToRest(subStringToCheck)
        if len(subStringToCheck) == 1:
            marker = x+markerLength
            break
    if marker != 0:
        break
print("Characters: ",marker)
f.close()
print(time.process_time())