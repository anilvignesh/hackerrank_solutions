def noOfDigits(x):
    count = 0
    while x>0:
        count = count+1
        x=x/10
    return count

def requiredNumber(number):
    sqrdNumber = number ** 2
    size = noOfDigits(number)
    leftPart = sqrdNumber/10 ** size
    rightPart = sqrdNumber - leftPart*10**size
    if leftPart + rightPart == number:
        return True
    else:
        return False

def main():
    p,q = raw_input().split()
    result = []
    for i in range(int(p),int(q)+1):
        if requiredNumber(i):
            result.append(i)
    print result

if __name__ == '__main__':
    main()    






