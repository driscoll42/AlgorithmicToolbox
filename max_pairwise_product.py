# Uses python3
import time
import random


def max_pairwise_product_old(numValues, values):
    '''
    file = open('input.txt', 'r')
    n = int(file.readline())
    a = [int(x) for x in file.readline().split()]
    file.close()

    assert (len(a) == n)
    '''

    result = 0
    aMax = values[0]
    aMax2 = -1

    for i in range(0, numValues):
        for j in range(i + 1, numValues):
            if values[i] * values[j] > result:
                result = values[i] * values[j]
                aMax = values[i]
                aMax2 = values[j]

    return (result, aMax, aMax2)


def max_pairwise_product(numValues, values):
    aMax = values[0]
    aMax2 = -1

    for i in range(1, numValues):
        if values[i] > aMax2:
            if values[i] > aMax:
                aMax2 = aMax
                aMax = values[i]
            else:
                aMax2 = values[i]

    return (aMax * aMax2, aMax, aMax2)


def main():
    time2 = time.time()
    totalOldTime = 0
    totalNewTime = 0
    count = 0
    while count < 100:
        numValues = random.randint(2, 100000)
        values = [random.randint(1, 10 ** 4) for p in range(0, numValues)]

        newTime = time.time()
        newTest = max_pairwise_product(numValues, values)
        totalNewTime = totalNewTime + (time.time()-newTime)
        # print("NewTime: " + str(newTotalTime))

        oldTime = time.time()
        oldTest = max_pairwise_product_old(numValues, values)
        totalOldTime = totalOldTime + (time.time()-oldTime)
        # print("OldTime: " + str(oldTotalTime))

        if oldTest[0] != newTest[0]:
            print("FAIL - numValues: " + str(numValues) + " - oldMaxes: " + str(oldTest[1]) + " " + str(
                oldTest[2]) + " - newMaxes: " + str(newTest[1]) + " " + str(newTest[2]))
        '''if newTotalTime == 0:
            print("INFINITE")
        else:
            print("SpeedUp: " + str(oldTotalTime/newTotalTime))
        '''
        '''     if oldTest[0] == newTest[0]:
            print("PASS - numValues: " + str(numValues) + " - oldMaxes: " + str(oldTest[1]) + " " + str(oldTest[2])
                  + " - newMaxes: " + str(newTest[1]) + " " + str(newTest[2]))'''
        count = count + 1
    print("TOTAL TIME: " + str(time.time() - time2))
    print("SPEEDUP: " + str(totalOldTime/totalNewTime))


main()
