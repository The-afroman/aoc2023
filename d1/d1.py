lines = []
numberStrings = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


class matchS:
    idx: int
    mStr: str
    rStr: str

    def __init__(self, idx: int, mStr: str, rStr: str):
        self.idx = idx
        self.mStr = mStr
        self.rStr = rStr


def getSum():
    sum = 0
    for line in lines:
        num = ""
        l = 0
        r = len(line) - 1
        foundL = False
        foundR = False
        while l <= r and not (foundL and foundR):
            if line[l].isnumeric() and (not foundL):
                num = line[l] + num
                foundL = True
            elif not foundL:
                l += 1
            if line[r].isnumeric() and (not foundR):
                num = num + line[r]
                foundR = True
            elif not foundR:
                r -= 1
        if num != "":
            sum += int(num)
        else:
            print(line, num)
    return sum


def fixListP2():
    with open("./input.txt") as iFile:
        for line in iFile:
            fOcc = matchS(len(line), "", "")
            lOcc = matchS(-1, "", "")
            lines.append(line.rstrip("\n"))
            print(lines[-1])
            for i, x in numberStrings.items():
                curr = lines[-1].find(i)
                if curr < fOcc.idx and curr >= 0:
                    fOcc.idx = curr
                    fOcc.mStr = i
                    fOcc.rStr = x

                curr = lines[-1].rfind(i)
                if curr > lOcc.idx and curr >= 0:
                    lOcc.idx = curr
                    lOcc.mStr = i
                    lOcc.rStr = x

            if fOcc.idx == lOcc.idx:
                lines[-1] = (
                    lines[-1][: lOcc.idx] + lOcc.rStr + lines[-1][lOcc.idx + 1 :]
                )
            elif fOcc.idx < lOcc.idx:
                lines[-1] = (
                    lines[-1][: lOcc.idx] + lOcc.rStr + lines[-1][lOcc.idx + 1 :]
                )
                lines[-1] = (
                    lines[-1][: fOcc.idx] + fOcc.rStr + lines[-1][fOcc.idx + 1 :]
                )

            print(lines[-1], "\n")


if __name__ == "__main__":
    fixListP2()
    print(getSum())
