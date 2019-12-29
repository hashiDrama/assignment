def checkTwoSidedPrime(n):
    n = int(n)
    isPrimeArr = [None] * (n + 1)
    isPrime(n, isPrimeArr)
    if isLeftSidedPrime(n, isPrimeArr) and isRightSidedPrime(n, isPrimeArr):
        return True
    return False

def isLeftSidedPrime(n, isPrimeArr):
    temp = n
    count = getDigitCount(n)
    mod = 0
    while count > 0:
        mod = pow(10,count)
        temp = n % mod
        if isPrimeArr[temp] == False :
            return False
        count = count-1
    return True

def getDigitCount(n):
    digitCount = 1
    rem = 0
    temp = n
    while temp > 0:
        rem = temp % 10
        temp = temp // 10
        digitCount = digitCount + 1
    return digitCount

def isRightSidedPrime(n, isPrimeArr):
    temp = n
    while temp > 1:
        if isPrimeArr[temp] == False:
            return False
        temp = temp // 10
    return True

def isPrime(n, isPrimeArr):
    isPrimeArr[0] = isPrimeArr[1] = False
    for i in range(2, n + 1):
        isPrimeArr[i] = True
    p = 2
    while(p * p <= n):
        if(isPrimeArr[p] == True):
            i = p * 2
            while i <= n:
                isPrimeArr[i] = False
                i = i + p
        p = p + 1
