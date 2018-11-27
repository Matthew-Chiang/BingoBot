import continuous
import foundAns

gameBoard = [
    [7,21,41,54,65],
    [1,30,33,53,74],
    [9,16,35,47,71],
    [8,29,38,58,61],
    [11,24,44,47,75]
]

def inGameBoard(a):
    for i,row in enumerate(gameBoard):
        for j,col in enumerate(row):
            if col == a:
                return (i,j)

    return -1

def setBoard(newBoard):
    gameBoard = newBoard

def main():
    val = 0
    ansArr = []
    valArr = []

    with open("bingobuffer.txt", "r") as bufferfile:
        for line in bufferfile:
            for c in line:
                if c != ' ':
                    val = val * 10 + int(c)
                else:
                    ans = inGameBoard(val)
                    if ans != -1:
                        ansArr.append(ans)
                        valArr.append(val)
                    val = 0

    foundAns.sendAns(valArr[-1],ansArr[-1])

if __name__ == "__main__":
    main()
