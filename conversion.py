def isAFND(AF):
    for d in AF.deltaStates:
        if (len(d) >= 2):
            return True
    return False

def toAFD(AF):
    if (isAFND(AF)):
        Q = ["0"]
        dQ = [AF.deltaStates[0]]    #Tiene a los de q0 por defecto
        tempDq = []
        indice = 0
        flag = False
        fin = 0
        try:
            for estado in AF.deltaStates[0]:
                if (estado not in Q):
                    Q.append(estado)
            while not flag:
                for estado in range(1, len(Q)):
                    for Segma in range(len(AF.sigma)):
                        tempDq.append("")
                        for letra in Q[estado]:
                            tempDq[indice] += AF.deltaStates[int(letra)][int(Segma)]
                        tempDq[indice] = quitarRepetidos(tempDq[indice])
                        indice += 1
                    for nuevoEstado in tempDq:
                        if (nuevoEstado not in Q):
                            Q.append(nuevoEstado)
                            flag = False
                        else:
                            fin += 1
                    dQ.append(tempDq)
                    tempDq = []
                    indice = 0
                print(fin, len(Q))
                if (fin >= (len(Q) - 1)):
                    break
                fin = 0
        except:
            print("ERROR EN Eq -> Q")
        print(Q)
        print(dQ)
        #print(f"transiciones q0 las mismas por defect: {dQ}")

        input()
        return True
    return False

def quitarRepetidos(str): 
    return "".join(set(str)) 