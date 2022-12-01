#################################
###Advent of Code Day 1
###Start Time: 10:00am
###End Time: 10:25am
###Author: Jonathan LeFeber
###Lines of Code: 35
#################################
ElfList = []
ChonkiestElf = 0
ChonkiestElfTeam = 0

def d1s1Sum():
    f = open("Puzzle1Input.txt", "r")
    CurrentElfSum = 0
    for line in f:
        currentLine = line
        if currentLine.strip() == "":
            #Push to Array
            ElfList.append(CurrentElfSum)
            CurrentElfSum = 0
        else:
            CurrentElfSum += int(currentLine.strip())
    #ElfList.remove('')
    #print("ElfList: ",ElfList)
    return ElfList

def d1s1Max(ElfListMax):
    ChonkiestElf = 0
    for elf in ElfListMax:
        if int(elf) > ChonkiestElf:
            ChonkiestElf = elf
    print("Chonkiest Elf: ",ChonkiestElf)
    return ChonkiestElf

def d1s2MaxTeam(ElfListTeam):
    ChonkiestElfTeam = 0
    print("Now finding chonkiest elf team of 3:")
    for index in range(3):
        ChonkiestElf = d1s1Max(ElfListTeam)
        ChonkiestElfTeam += ChonkiestElf
        ElfListTeam.remove(ChonkiestElf)
    
    """
    ChonkiestElf = 0
    for elf in ElfList:
        if int(elf) > ChonkiestElf:
            ChonkiestElf = elf
    ChonkiestElfTeam += ChonkiestElf
    ElfList.remove(ChonkiestElf)
    ChonkiestElf = 0
    for elf in ElfList:
        if int(elf) > ChonkiestElf:
            ChonkiestElf = elf
    ChonkiestElfTeam += ChonkiestElf
    """
    print("Chonkers = ",ChonkiestElfTeam)
    
d1s1Max(d1s1Sum())
d1s2MaxTeam(d1s1Sum())