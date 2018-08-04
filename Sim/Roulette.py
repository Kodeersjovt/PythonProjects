import random
import matplotlib
import matplotlib.pyplot as plt

def spinWheel():
    resultList = ['A'] * 1 + ['B'] * 3 + ['C'] * 3 + ['D'] * 3 + ['E'] * 3 + ['F']\
        * 3 + ['G'] * 3 + ['H'] * 3 + ['I'] * 3 + ['J'] * 3 + ['K'] * 3 + ['L'] * 3 + ['M'] * 3
    spin = random.choice(resultList)
    return spin


def game(cutLossSpin):
    resultList = []
    spinCount = 0
    while spinCount <= cutLossSpin:
        result = spinWheel()
        if result not in resultList and len(resultList) < 3:
            resultList.append(result)
            spinCount += 1
        elif result in resultList:
            spinCount += 1
            return True, spinCount, resultList, result
        elif spinCount == cutLossSpin:
            return False, spinCount
        else:
            spinCount += 1


def cashOutcome(cutLossSpin):
    runningCostList = [1, 3, 6, 12, 21, 33, 48, 69, 96, 132, 180, 246, 333, 450, 606, 813, 1089, 1458, 1950, 2604]
    profitList = [11, 9, 6, 12, 15, 15, 12, 15, 12, 12, 12, 18, 15, 18, 18, 15, 15, 18, 18, 12]
    outcome = 0
    result = game(cutLossSpin)
    if result[0] == True:
        outcome = profitList[result[1]-1]
        return outcome
    else:
        outcome = -1 * runningCostList[result[1]-1]
        return outcome


def bettor(funds, cutLossSpin, gameLength):
    bankroll = funds
    gameNumber = 1
    gNx = [0]
    bY = [funds]
    while bankroll > 0 and gameLength > gameNumber:
        bankroll = bankroll + cashOutcome(cutLossSpin)
        gameNumber += 1
        gNx.append(gameNumber)
        bY.append(bankroll)

    plt.plot(gNx, bY)


x = 0

while x < 100:
    bettor(2000, 19, 2000)
    x += 1

plt.ylabel('bankroll')
plt.xlabel('Tries')
plt.show()
