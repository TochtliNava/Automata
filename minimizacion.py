def minimizarAFD(Q, sQ, fQ):
    partition = []
    tempArr = []
    partition.append(fQ)
    print(Q)
    try:
        for q in Q:
            if (q not in partition[0]):
                try:
                    tempArr.append(q)
                except:
                    input("ERROR PARTITION/APPEND")
        partition.append(tempArr)
    except:
        input("ERROR EN AÑADIR PARTES DE PARTITION")
    tempArr = []
    print(f"π{0} = {partition}")