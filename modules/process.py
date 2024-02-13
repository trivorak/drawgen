def scalevalues(inputlist, scale):
    listVar = []
    for element in inputlist:
        listVar.append(round(element * scale, 0))

    return listVar


def loomvaluesprep(inputlist, scale):
    scaledVar = scalevalues(inputlist, scale)
    listVar = []

    for i in range(len(scaledVar)):
        if i % 4 == 0:
            listVar.append((0, scaledVar[i]))
        elif i % 4 == 1:
            listVar.append((scaledVar[i], 0))
        elif i % 4 == 2:
            listVar.append((255 * scale, scaledVar[i]))
        elif i % 4 == 3:
            listVar.append((scaledVar[i], 255 * scale))

    return listVar
