import os, conversion

class Automata():
    def __init__(self):
        self.nStates = 0;
        self.states = []        #Contenedor de los estados

        self.pos = 0

        self.s = 0              #Cuantos x | x∈σ
        self.sigma = []         #Contenedor de el alfabeto

        self.finalStates = 0    #Cuantos estados finales hay
        self.fStates = []       #Cuales estados son finales

        self.actualState = ["0"]   #Estado actual
        self.tempStates = []

        self.deltaStates = []

        #[] longitud = self.nStates, [[q1, q2, q3, ..., qn],[Cada q esta dentro [] segun self.s]]
        #[q0[q1, q2],q1[q1, q2]]
    def createStates(self, q):
        self.nStates = q
        for x in range(q):
            self.states.append(str(x))

    def agregateSigma(self, s):
        self.sigma.append(s)

    def agregatefinal(self, f):
        self.fStates.append(f)

    def delta(self, c):
        try:
            for n in range(len(self.sigma)):        #Obtiene la posicion en sigma[]
                if (c == self.sigma[n]):
                    self.pos = n
        except:
            print("ERROR INDEX SIGMA")

        self.tempStates = self.actualState      #Clonar el estado actual
        self.actualState = [""]                   #vaciar el estado actual

        for n in self.tempStates[0]:               #cada estado actual
            try:
                if (self.deltaStates[int(n)][self.pos] != "NULL"):
                    self.actualState[0] += self.deltaStates[int(n)][self.pos]
                if (self.deltaStates[int(n)][self.pos] == "NULL"):
                    self.actualState[0] += n
            except:
                print("ERROR DELTA")

    def isValid(self):
        try:
            for n in self.actualState[0]:
                if (n in self.fStates):
                    return True
                return False
        except:
            print("ERROR EN METODO ISVALID")

def main():

    while True:

        ######################################
        ##                                  ##
        ##      Diccionarios para texto     ##
        ##                                  ##
        ######################################

        numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Æ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '*', '~', '+', '@']
        positions = [1]
        reservadas = ['s', 'i', 'g', 'F', 'S', 'I', 'G']

        ######################################
        ##                                  ##
        ##      Lector de archivos .txt     ##
        ##                                  ##
        ######################################

        path = input("Nombre del archivo: ")
        try:
            archivo = open(path)    #El archivo .txt como objeto
            data = archivo.read()   #data contiene el texto tipo string

        ######################################
        ##                                  ##
        ##     Procesador de automata       ##
        ##                                  ##
        ######################################

            i = 1               #Contador de ciclos multiproposito
            tempI = 0           #Contador temporal
            Auto = Automata()   #Crea el objeto Automata
            os.system("cls")
            print(data)         #DEBUG
            tempString = ""     #Linea del archivo de texto temporal
            tempNumber = ""     #Numero temporal
            sigFlag = False     #Bandera sigma
            fflag = False       #Bandera estados finales
            tempFlag = False    #Bandera temporal

        ######################################
        ##                                  ##
        ##     Procesador de automata       ##
        ##                                  ##
        ######################################

            for c in data:
                if (c != "\n"):
                    tempString = tempString + c     #Cualquier letra que no sea enter entra a tempString

                if (c == "\n"):
                    if (i == 1):
                        for n in tempString:        #si hay un enter procesa esa cadena antes de limpiarla
                            if (n in numeros):
                                tempNumber += n

                        Auto.createStates(int(tempNumber))

                    if ((i not in positions) and (Auto.s == 0)):
                        for n in tempString:
                            if (n in numeros):
                                tempNumber += n

                        Auto.s = int(tempNumber)
                        positions.append(i)

                    if ((i not in positions) and (Auto.finalStates == 0)):
                        for n in tempString:
                            if (n in numeros):
                                tempNumber += n

                        Auto.finalStates = int(tempNumber)
                        positions.append(i)

                    i += 1
                    tempString = ""
                    tempNumber = ""

            reservadas = []
            tempString = ""

        ####################################################
        ##                                                ##
        ##    Asignador de sigma y estados finales        ##
        ##                                                ##
        ####################################################

            for c in data:
                if (c == "S"):
                    sigFlag = True

                if (c == "F"):
                    fflag = True

                if (c == "{" and (sigFlag or fflag)):
                    tempFlag = True

                if (tempFlag and (sigFlag or fflag)):
                    tempString += c

                if ((c == "}") and tempFlag):
                    for s in tempString:
                        if ((s in alphabet) and (len(Auto.sigma) < Auto.s) and sigFlag):
                            Auto.agregateSigma(s)   #x deberia ser texto o int?
                            tempString = ""

                    if (sigFlag):
                        sigFlag = False

                    for s in tempString:
                        if ((s in numeros) and (len(Auto.fStates) < Auto.finalStates) and fflag):
                            Auto.agregatefinal(s)   #x deberia ser texto o int?
                            tempString = ""

                    if (fflag):
                        fflag = False

                    tempFlag = False

                i += 1

        ####################################################
        ##                                                ##
        ##    Banderas para evitar repeticion sigma       ##
        ##                                                ##
        ####################################################

            if (len(Auto.sigma) >= Auto.s):
                sigFlag = False

            if (len(Auto.fStates) >= Auto.finalStates):
                fflag = False

        ###########################################
        ##                                       ##
        ##    Crear cadena para transicion       ##
        ##                                       ##
        ###########################################

            tempI = 0

            for c in data:
                if (c == "S"):
                    sigFlag = True

                if (c == "F"):
                    fflag = True

                if (c == "}"):
                    tempI += 1

                if (tempFlag and sigFlag and fflag):
                    tempString += c

                if (tempI == 2 and sigFlag and fflag):
                    tempFlag = True

            tempFlag = False    #Reset bandera temporal
            mflag = False
            tempA = [""]      #Reset las posiciones
            i = 0               #Reset contador
            tempTempString = ""

            #[[],[],[]]
            for c in tempString:
                if (c == "," or c == "}"):
                    mflag = False

                if (c == ">"):
                    mflag = True
                    tempFlag = True

                if (mflag and tempFlag):
                    tempTempString += c

                if (not mflag and tempFlag and (len(tempTempString) != 0)):

                    #
                    #   Agregar [] con deltaStates.append sin usar auto.initDelta
                    #   > 0 | 12
                    for s in tempTempString:
                        if (s == "|"):
                            tempA.append("")
                            i += 1

                        if (s in Auto.states or s in "NULL"):
                            tempA[i] += s

                    Auto.deltaStates.append(tempA)
                    tempTempString = ""
                    i = 0
                    tempA = [""]

        ######################################
        ##                                  ##
        ##       Evaluar cadena delta       ##
        ##                                  ##
        ######################################

            print("OPCIONES")
            print("E) Evaluar Cadena")
            print("C) Convertir AFND -> AFD")
            print("M) Minimizar Automata")
            print("S) Salir")
            print("")
            cursor = input(">>")

            if (cursor.upper() == "E"):
                os.system("cls")
                print(data)
                cadena = input("Inserte cadena: ")
                for c in cadena:
                    if (c in Auto.sigma):
                        Auto.delta(c)
                    else:
                        print("Error, {} no esta en sigma".format(c))
                try:
                    if (Auto.isValid()):
                        input("Cadena Aceptada...")
                        archivo.close()
                        os.system('cls')
                    else:
                        input("Cadena Rechazada...")
                        archivo.close()
                        os.system('cls')
                except:
                    input("ERROR INVOCANDO ISVALID()...")
                    os.system('cls')

            if (cursor.upper() == "C"):
                try:
                    if (conversion.toAFD(Auto)):
                        os.system("cls")
                        print("YES")
                        input()
                    if (not conversion.toAFD(Auto)):
                        os.system("cls")
                        print(data)
                        input("--El Automata ya es determinista--")
                except:
                    print("Error en conversion")

            if (cursor.upper() == "D"):
                os.system("cls")
                print(Auto.deltaStates)
                input()

            if (cursor.upper() == "S"):
                ######################################
                ##                                  ##
                ##       Cerrar archivo .txt        ##
                ##                                  ##
                ######################################
                os.system('cls')
                print(data)
                setting = input("TERMINAR PROGRAMA (Y/N): ")
                if (setting.upper() == "Y"):
                    os.system('cls')
                    archivo.close()
                    break
            os.system("cls")

        except:
            print("No existe", path)    #En caso de que el titulo del archivo esté mal
            input("...")
            os.system('cls')



if __name__ == '__main__':
    main()
