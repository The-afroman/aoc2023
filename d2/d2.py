nRed = 12
nGreen = 13
nBlue = 14
sum = 0
part = 2

def getNum(s: str):
    s = s.split(" ")
    return int(s[0])

if __name__ == "__main__":
    with open("./input.txt") as iFile:
        for idx, line in enumerate(iFile):
            maxR, maxG, maxB = 0, 0, 0
            splitL = line.split(':')[1]
            splitL = [s.split(',') for s in splitL.split(';')]
            for subgame in splitL:
                for s in subgame:
                    s = s.lstrip(' ')
                    s = s.rstrip('\n')
                    if s.find("red") > 0:
                        maxR = max(maxR,getNum(s))
                    elif s.find("green") > 0:
                        maxG = max(maxG,getNum(s))
                    else:
                        maxB = max(maxB,getNum(s))
            if((maxR <= nRed and maxG <= nGreen and maxB <= nBlue) and part == 1):
                sum+=idx+1
                print(idx, splitL,"(", maxR, maxG, maxB, ")")
            else:
                sum+=(maxR*maxG*maxB)

    print(sum)