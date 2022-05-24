import os

def minimizarAFD(Automata):
    os.system("cls")
    partition = []
    tempArr = []
    partition.append(Automata.fStates)
    diQ = dict(zip(Automata.states, Automata.deltaStates))
    print(diQ)
    try:
        for q in Automata.states:
            if (q not in partition[0]):
                try:
                    tempArr.append(q)
                except:
                    input("ERROR PARTITION/APPEND")
        partition.append(tempArr)
    except:
        input("ERROR EN AÑADIR PARTES DE PARTITION")
    tempArr = []
    temp = []
    print("----PARTICIONES----")
    print()
    print(f"π{0} = {partition}")

    #   [[Q1], [Q2, Q3, Q4]]
    #   -->
    #   [[Q1],[Q2, Q3],[Q4]]

    turno = 1
    for miniParticion in partition:
        if (len(miniParticion) > 1):
            i = 0
            temp = []
            for estado in miniParticion:
                if (i == 0):
                    tmQ = diQ[estado]
                    tQ = estado
                if (diQ[estado] != tmQ and i != 0):
                    tempArr.append(tQ)
                    tempArr.append(estado)
                tmQ = diQ[estado]
                tQ = estado
                i += 1
            for mmπ in range(len(partition)):
                for eQ in partition[mmπ]:
                    if (eQ in tempArr):
                        partition[mmπ].remove(eQ)
            if (len(tempArr) != 0 and (tempArr not in partition)):
                partition.append(tempArr)
                print(f"π{turno} = {partition}")
            turno += 1
            tempArr = []