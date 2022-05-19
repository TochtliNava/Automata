from collections import OrderedDict
import os

def isAFND(AF):
    for d in AF.deltaStates:
        for c in d:
            if (len(d) >= 2):
                return True
    return False

def toAFD(AF, data):
    Q = ["0"]
    dQ = []    #Tiene a los de q0 por defecto
    tempDq = []
    indice = 0
    fin = 0
    i = 0
    size = 0
    try:
        while True:
            for estado in range(len(Q)):
                for Segma in range(len(AF.sigma)):
                    tempDq.append("")
                    for letra in Q[estado]:
                        if (AF.deltaStates[int(letra)][int(Segma)] != "NULL"):
                            tempDq[indice] += AF.deltaStates[int(letra)][int(Segma)]
                    tempDq[indice] = quitarRepetidos(tempDq[indice])
                    indice += 1
                    
                for nuevoEstado in tempDq:
                    if (nuevoEstado not in Q):
                        Q.append(nuevoEstado)
                    else:
                        fin += 1
                tempDq = []
                indice = 0
            if (fin == (len(Q) * len(AF.sigma))):
                break
            fin = 0
            
        for estado in range(len(Q)):
            for Segma in range(len(AF.sigma)):
                tempDq.append("")
                for letra in Q[estado]:
                    if (AF.deltaStates[int(letra)][int(Segma)] != "NULL"):
                        tempDq[indice] += AF.deltaStates[int(letra)][int(Segma)]
                tempDq[indice] = quitarRepetidos(tempDq[indice])
                indice += 1


            dQ.append(tempDq)

            tempDq = []
            indice = 0
    except:
        print("ERROR EN Eq -> Q")
        
    fs = 0

    try:
        for estado in range(len(Q)):
            for digito in Q[estado]:
                if (digito in AF.fStates):
                    fs += 1
    
    except:
        print("ERROR EN ESOT")
    try:
        os.system("cls")
        print("######- AUTOMATA FINITO NO DETERMINISTA -######")
        print(data)
        print("########- AUTOMATA FINITO DETERMINISTA -########")
        print("")
        print(len(Q))
        print(len(AF.sigma))
        print(fs)
        print("Sig{", AF.sigma, "}")
        print("F{")
        for estado in range(len(Q)):
            for digito in Q[estado]:
                if (digito in AF.fStates):
                    print(Q[estado])
        print("}")
        print("{")
        for estado in range(len(Q)):
            print(f"{Q[estado]} > {dQ[estado]}")
        print("}")
        input()
    except:
        input("ERROR EN IMPRESION DE")


def quitarRepetidos(str): 
    return "".join(OrderedDict.fromkeys(str))