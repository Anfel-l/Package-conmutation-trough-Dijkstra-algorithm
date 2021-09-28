
class paquete():
    
    def __init__(self, tamano_ventana):
        self.tamano_ventana = tamano_ventana

    def mensaje_a_paquetes(self, message):
        lista_paquetes = []
        palabra_cortada = ""
        for i in range(len(message)):
            palabra_cortada += message[i]
            if ( i % self.tamano_ventana) == 1 or i == len(message)-1:
                lista_paquetes.append(palabra_cortada)
                palabra_cortada = ""
        return lista_paquetes
    
    def paquetes_a_mensaje(self, lista_paquetes):
        mensaje = ""
        for paquete in lista_paquetes:
            mensaje += paquete
        return mensaje


    