def isAFND(AF):
    for d in AF.deltaStates:
        if (len(d) >= 2):
            return True
    return False

