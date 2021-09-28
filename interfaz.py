global message 
global nodo_destiny
global nodo_origin

def readInput():
    return str(input(">"))

def printStringInput():
    print("Digite el mensaje a transferir por la red.")

def printNodo(tipo_nodo):
    print(f"Digite el nodo {tipo_nodo}")


def showNodos(lista_nodos):
    for posicion_nodo in range(len(lista_nodos)):
        print(f"{posicion_nodo}. Nodo ",lista_nodos[posicion_nodo])

"""
Lee un nodo que solamente este en el rango establecido por la cantidad de elementos en una lista.
Excepcion: si se digita una string, retorna un error de tipo ValueError
"""
def read_nodo(lista_nodos, tipo_nodo):
    while(True):
        printNodo(tipo_nodo)
        showNodos(lista_nodos)
        try:
            nodo = int(readInput())
            if(nodo < len(lista_nodos) and nodo >= 0):
                break
        except ValueError:
            print("Digite numeros enteros! Error:", ValueError)

    return nodo

def getData(lista_nodos):
    printStringInput()
    message = readInput()
    nodo_origin = read_nodo(lista_nodos, "origen")
    nodo_destiny = read_nodo(lista_nodos, "destino")

    context = (message,nodo_origin,nodo_destiny)
    return context

def start(lista_nodos):
    return getData(lista_nodos)
