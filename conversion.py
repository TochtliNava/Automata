from collections import OrderedDict
import os

Q = ["0"]
dQ = []    #Tiene a los de q0 por defecto
fQ = []

def setZero():
    Q = ["0"]
    dQ = []    #Tiene a los de q0 por defecto
    fQ = []

def isAFND(AF):
    for d in AF.deltaStates:
        for c in d:
            if (len(c) >= 2 and c != "NULL"):
                return True
    return False

def toAFD(AF, data):
    setZero()
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
                            tempDq[indice] = sorted(tempDq[indice])
                    tempDq[indice] = quitarRepetidos(tempDq[indice])
                    indice += 1

                for nuevoEstado in tempDq:
                    if (nuevoEstado not in Q and nuevoEstado != ""):
                        Q.append(nuevoEstado)
                    else:
                        fin += 1
                tempDq = []
                indice = 0
            if (fin == (len(Q) * len(AF.sigma))):
                break
            fin = 0
            
        for estado in range(len(Q)):
            #[Q1, Q2, ..., Qn]
            for Segma in range(len(AF.sigma)):
                #[a,b,c,...,X]
                tempDq.append("")
                #["" + ""] -> ["", ""]
                for letra in Q[estado]:
                    #Q1 = abc --> a, b, c
                    #if (len(tempDq[indice]) == 0):
                    #    tempDq[indice] += AF.deltaStates[int(letra)][int(Segma)]
                    #else:
                    if (len(tempDq[indice]) == 0 and AF.deltaStates[int(letra)][int(Segma)] == "NULL"):
                        tempDq[indice] += AF.deltaStates[int(letra)][int(Segma)]
                    if (AF.deltaStates[int(letra)][int(Segma)] != "NULL"):
                        if ("NULL" == tempDq[indice]):
                            tempDq[indice] = ""
                        tempDq[indice] += AF.deltaStates[int(letra)][int(Segma)]
                        tempDq[indice] = quitarRepetidos(tempDq[indice])
                        tempDq[indice] = "".join(sorted(tempDq[indice]))
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

        for estado in range(len(Q)):
            for digito in Q[estado]:
                if (digito in AF.fStates and Q[estado] not in fQ):
                    fQ.append(Q[estado])
    
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
        print(fQ)
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

def obtenerDatos():
    return Q, dQ, fQ