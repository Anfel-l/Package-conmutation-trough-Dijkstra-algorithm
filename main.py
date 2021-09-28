import interfaz
from paquete_c import paquete

def generar_lista_de_nodos(matriz_adyacencia):
    contador = 1
    lista_nodos = []
    for sub_matriz in matriz_adyacencia:
        for nodo in sub_matriz:
            lista_nodos.append(nodo)
            contador += contador
    return lista_nodos

if __name__ == "__main__":
    
    matriz_red_adyacencia = [[0,0,25],[0,0,25],[0,0,25],[0,0,25]]
    print(matriz_red_adyacencia[0][0])

    print(len(matriz_red_adyacencia))
    lista_nodos = generar_lista_de_nodos(matriz_red_adyacencia)
    
    #print(list_nodos)
    context = interfaz.start(lista_nodos)
    empaquetador = paquete(5)
    message_test = context[0]
    
    lista_paquetes = empaquetador.mensaje_a_paquetes(message_test)
    print(lista_paquetes)
    mensaje = empaquetador.paquetes_a_mensaje(lista_paquetes)
    print(mensaje)
    
    

    #print(context)