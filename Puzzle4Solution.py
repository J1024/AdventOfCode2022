#################################
###Advent of Code Day 4
###Start Time: 1:24am
###End Time: 2:03am
###Author: Jonathan LeFeber
###Lines of Code: 34
#################################
import time
fullyOverlapPair = 0
f = open("Puzzle4Input.txt", "r")
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
f.close()

partialOverlapPair = 0
f = open("Puzzle4Input.txt", "r")
for pair in f:
    left = pair[:pair.index(',')].strip()
    right = pair[pair.index(',')+1:].strip()
    #print(left,right)
    leftLow = int(left[:left.index('-')])
    leftHigh = int(left[left.index('-')+1:])
    rightLow = int(right[:right.index('-')])
    rightHigh = int(right[right.index('-')+1:])
    if leftHigh >= rightLow and leftLow <= rightHigh:
        partialOverlapPair += 1       
    elif rightHigh >= leftLow and rightLow <= leftHigh:
        partialOverlapPair += 1        
print("Partial Overlaps: ", partialOverlapPair)
f.close()
print(time.process_time())