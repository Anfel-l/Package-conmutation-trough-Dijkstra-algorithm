class Package():
    
    #Constructor que recibe el tamaño de men
    def __init__(self, window_size):
        self.window_size = window_size

    #Genera una lista de N paquetes
    #En base a el tamaño de un paquete dado por el tamaño de ventana
    def message_to_package(self, message):
        tempo_package_list = []
        
        cut_word = ""
        #Recorre cada letra del mensaje incluyendo espacios
        for i in range(len(message)):
            #Selecciona el caracter en la posicion i
            #y lo agrega a palabra cortada
            cut_word += message[i]
            
            #Recorro comparando cada caracter con el múltiplo del rango generado
            #si no es multiplo, agrega la letra, cuando coincide el múltiplo
            #corta la cadena y la agrega a la lista de paquetes
            if ( i % self.window_size) == 1 or i == len(message)-1:
                tempo_package_list.append(cut_word)
                cut_word = ""
        package_list = []
        for j in range(len(tempo_package_list)):
            #Crea una estructura de la forma List [[numero_paquete,mensaje_cortado]]
            package_list.append([j, tempo_package_list[j]])

        return package_list
    

    #Suma cadenas de caracteres de una lista 
    #Recibe una estructura de la forma List [[numero_paquete,mensaje_cortado]]
    def package_to_message(self, package_list):
        message = ""
        for package in package_list:
            message += package[1]
        return message


    