import os

def minimizarAFD(Automata):
    os.system("cls")
    partition = []
    tempArr = []
    tmp = []
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
    print("----PARTICIONES----")
    print()
    print(f"π{0} = {partition}")

    #   [[Q1], [Q2, Q3, Q4]]
    #   -->
    #   [[Q1],[Q2, Q3],[Q4]]
    
    partition = []
    estados = Automata.states

    for i in estados:
        tmp = []
        #A -> [] from [[], [], []]
        for u in estados:
            if (diQ[i] == diQ[u] and i != u):
                tmp.append(u)
                estados.remove(u)
        tmp.append(i)
        estados.remove(i)
        partition.append(tmp)
    print(partition)