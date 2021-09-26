global message 
global nodo_destiny
global nodo_origin

def readInput():
    return str(input(">"))

def printStringInput():
    print("Digite el mensaje a transferir por la red.")

def printNodoOrigen():
    print("Digite el nodo origen")

def printNodoDestino():
    print("Digite el nodo destino")

def showNodos():
    print("Ex:")
    print("1. Nodo A")
    print("2. Nodo B")
    print("3. Nodo C")
    print("n. Nodo N...")

def getData():
    printStringInput()
    message = readInput()

    printNodoOrigen()
    nodo_origin = readInput()

    printNodoDestino()
    nodo_destiny = readInput()
    context = (message,nodo_origin,nodo_destiny)
    return context
def start():
    return getData()
        