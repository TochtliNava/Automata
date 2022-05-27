import os

def minimizarAFD(Automata):
    os.system("cls")
    partition = []
    tempArr = []
    tmp = []
    estados = []
    partition.append(Automata.fStates)
    diQ = dict(zip(Automata.states, Automata.deltaStates))
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
    estados = Automata.states.copy()
    #backup = Automata.states

    while (len(estados) > 0):
        for i in estados:
            tmp = []
            #A -> [] from [[], [], []]
            for u in estados:
                if (diQ[i] == diQ[u] and i != u):
                    if (u not in tmp):
                        tmp.append(u)
                if(i not in tmp):
                    tmp.append(i)
            partition.append(tmp)
            for E in tmp:
                if (E in estados):
                    estados.remove(E)
    
    print(f"πF = {partition}")
    print()
    input("...PRESIONE ENTER PARA CONTINUAR...")
    os.system("cls")

    #remplazo
    quitar = []
    YES = False
    for grupo in partition:
        #Quitar desde states
        if (len(grupo) > 1):
            for estado in Automata.states:
                if ((estado in grupo) and (estado != grupo[0])):
                    quitar.append(estado)
            for estado in quitar:
                Automata.states.remove(estado)
            quitar = []
            for estado in Automata.fStates:
                if ((estado in grupo) and (estado != grupo[0])):
                    quitar.append(estado)
            for estado in quitar:
                Automata.fStates.remove(estado)
            quitar = []
            try:
                Automata.deltaStates = []
                for estado in Automata.states:
                    Automata.deltaStates.append(diQ[estado])
            except:
                input("ERROR EN QUITAR DELTA")
            for miniPart in Automata.deltaStates:
                for estado in range(len(miniPart)):
                    if ((miniPart[estado] in grupo) and (miniPart[estado] != grupo[0])):
                        miniPart[estado] = grupo[0]
    
    diQ = dict(zip(Automata.states, Automata.deltaStates))
    print("########- AUTOMATA FINITO DETERMINISTA SIMPLIFICADO -########")
    print(len(Automata.states))
    print(len(Automata.sigma))
    print(len(Automata.fStates))
    print("Sig{", Automata.sigma, "}")
    print("F{")
    print(Automata.fStates)
    print("}")
    print("{")
    for estado in range(len(Automata.states)):
        print(f"{Automata.states[estado]} > {Automata.deltaStates[estado]}")
    print("}")