import binascii


def converthex(fileinput):
    with open(fileinput, "rb") as f:
        a = f.read()
        ab = binascii.hexlify(a)
        abc = str(ab, 'utf-8')
        return abc


def returnsplit(instring):
    aList = []
    for i in range(0, len(instring), 2):
        aList.append(instring[i:i + 2])

    return aList


def returnint(hexstring):
    aListInt = []

    for element in hexstring:
        aListInt.append(int(element, 16))

    return aListInt


def returnhex(fileinput):
    hexvar = converthex(fileinput)
    hexvar = returnsplit(hexvar)
    hexvar = returnint(hexvar)
    return hexvar


def returnlistlength(listvar,length):
    if length == 0:
        length = 1

    inputList = listvar
    for i in range(0, length - len(inputList) % length):
        inputList.append(0)

    return inputList