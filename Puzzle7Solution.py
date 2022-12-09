#################################
###Advent of Code Day 7
###Start Time: 9:50am
###End Time: 7:40am
###Author: Jonathan LeFeber
###Lines of Code: 56
#################################
import time

parent = 0
name = 1
folderSize = 2
subFolders = 3
inputString = []
parentDir = ''
currentDir = '-'
folderStructure = [[parentDir,currentDir,0,[]]]
def calculateFileSizes():
    #Do stuff
    print("Function")

#Read entire file into an array so I can move around a bit more dynamically.
f = open("Puzzle7Input.txt", "r")
for line in f:
    inputString.append(line)

#Walk the file.
for x in range(1,len(inputString)):
    getLine = inputString[x].strip()
    if getLine[:5] == "$ cd ":
        if getLine[5:] == "..":
            currentDir = parentDir
            for y in range(len(folderStructure)):
                if folderStructure[y][name] == currentDir:
                    parentDir = folderStructure[y][parent]
                    break
        else:
            parentDir = currentDir
            currentDir = parentDir+"/"+getLine[5:]
            #Check to see if the directory exists first. If it doesn't, THEN create it. Since I don't think we will ever browse to something I haven't seen, we are going to comment this out for now.
            #folderStructure.append([parentDir,currentDir,0,[]])
    elif getLine[:4] == "$ ls":
        x += 1
        #Find position in folderStructure so we know what size to update.
        for z in range(len(folderStructure)):
            if folderStructure[z][name] == currentDir:
                break
        while inputString[x][:1] != "$":
            if inputString[x][:3] == "dir":
                #print("Deets: ",parentDir,currentDir)
                newFolderName = currentDir+"/"+inputString[x][4:].strip()
                folderStructure.append([currentDir,newFolderName,0,[]])
                folderStructure[z][subFolders].append(newFolderName)
                #print("Folder Structure Updated To: ",folderStructure)
                #print("")
            else:
                size = int(inputString[x].split(' ')[0])
                folderStructure[z][folderSize] += size
                
            #After I'm done with the logic I need to make sure the next line exists, otherwise I might need to break
            x += 1
            if x == len(inputString):
                break

print(folderStructure)
#We now have the sum of all individual directories... we now need to walk folderStructure and add up totals.
finalFolderSizes = []

def calcFolderSize(folderName):
    totalSize = 0
    x = 0
    for x in range(len(folderStructure)):
        if folderStructure[x][name] == folderName:    
            totalSize += folderStructure[x][folderSize]
            #print("Checking folder: ",folderName)
            #print("Subfolders: ",folderStructure[x][subFolders])
            #print("Num Subfolders: ",len(folderStructure[x][subFolders]))
            if len(folderStructure[x][subFolders]) > 0:
                #print("Num Subfolders > 0: ",len(folderStructure[x][subFolders]))
                for subFolder in folderStructure[x][subFolders]:
                    #print("Recursing on subfolder: ",subFolder)
                    #print("")
                    totalSize += calcFolderSize(subFolder)
            break
    finalFolderSizes.append([folderName,totalSize])
    return totalSize

calcFolderSize('-')
for asdf in range(len(finalFolderSizes)):
    print(finalFolderSizes[asdf])
finalFinalSize = 0
for items in finalFolderSizes:
    if items[1] <= 100000:
        finalFinalSize += items[1]
print("Sum of folders <100,000: ",finalFinalSize)
rootSize = items[len(items)-1]
amountToDelete = rootSize - 40000000
deleteSize = rootSize
for qwer in range(len(finalFolderSizes)):
    if finalFolderSizes[qwer][1] > amountToDelete and finalFolderSizes[qwer][1] < deleteSize:
        deleteSize = finalFolderSizes[qwer][1]
print("Amount to delete: ",deleteSize)

print(time.process_time())