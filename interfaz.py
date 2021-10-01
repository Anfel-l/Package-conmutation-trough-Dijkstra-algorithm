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
    dir_ip  = str()
    while(True):
        printNodo(tipo_nodo)
        showNodos(lista_nodos)
        try:
            input_text = int(readInput())
            
            if (input_text < len(lista_nodos) and input_text >= 0): 
                dir_p = lista_nodos[input_text]
                return dir_p
        except ValueError:
            print("Digite numeros enteros! Error:", ValueError)
    print("DIRRRRRRRR",dir_ip)
    return dir_ip

def getData(lista_nodos):
    printStringInput()
    message = readInput()
    nodo_origin = read_nodo(lista_nodos, "origen")
    nodo_destiny = read_nodo(lista_nodos, "destino")

    context = (message,nodo_origin,nodo_destiny)
    return context



def start(lista_nodos):

    return getData(lista_nodos)
