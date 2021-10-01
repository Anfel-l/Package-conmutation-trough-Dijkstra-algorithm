import random
import interfaz
from dijkstra import *
import time
import threading 

from package import Package

class Controller():

    
    def __init__(self):

        #Lista de hilos
        self.threads_list= []

        self.package_list = []

        self.receive_package = []

        #Datos a recuperar
        self.vertex_origin = str()
        self.vertex_destiny = str()
        self.message = str()

        
        self.vertex_list = []
        self.edge_list = []
        
        self.window_size = int(5)
        
        #Instancio objeto de la clase paquete
        self.package_manager = Package(self.window_size)
        pass

    #Genera números aleatorios para los pesos de los vertices
    def random_edge(self):
        aux_num = random.randint(1,15)
        return aux_num    
            
    #Rellena la lista de vertices (6 nodos) con un rango 
    #de ips de 192.168.0.1 hasta 192.168.0.6
    def fulfill_vertex_list(self):
        for i in range(1,7):
            self.vertex_list.append(f"192.168.0.{i}")
    
    
    #Genera y establece las relaciones entre cada vertice y sus vertices vecinos
    def establish_edges(self,graph):
        graph.add_edge(self.vertex_list[0],self.vertex_list[5],self.random_edge())
        graph.add_edge(self.vertex_list[0],self.vertex_list[1],self.random_edge())
        graph.add_edge(self.vertex_list[0],self.vertex_list[2],self.random_edge())
        graph.add_edge(self.vertex_list[1],self.vertex_list[2],self.random_edge())
        graph.add_edge(self.vertex_list[1],self.vertex_list[3],self.random_edge())
        graph.add_edge(self.vertex_list[2],self.vertex_list[3],self.random_edge())
        graph.add_edge(self.vertex_list[2],self.vertex_list[5],self.random_edge())
        graph.add_edge(self.vertex_list[3],self.vertex_list[4],self.random_edge())
        graph.add_edge(self.vertex_list[4],self.vertex_list[5],self.random_edge())
    
    #Añade los vertices previamente agregados a 'vertex_list' en un objeto de tipo 
    #grafo. Recibe como parámetro objeto de tipo grafo
    def add_vertex_graph(self,graph):
        for i in self.vertex_list:
            graph.add_vertex(i)
    
    #Encuentra la ruta mas corta de un origen a un destino
    #en un grafo con pesos aleatorios
    #retorna una lista con el camino y el peso total 
    def found_path(self):
        graph = Graph()
        self.add_vertex_graph(graph)
        self.establish_edges(graph)
        graph.dijkstra(self.vertex_origin)
        #graph.print_graph()
        return graph.path(self.vertex_origin, self.vertex_destiny)

    
    def send_packages(self):
       
        for package in self.package_list:
            path_package = self.found_path()
            #print("Paquete enviado", path_package)
            self.entramar_paquete(package,path_package)
        
        self.await_sincronized_matriz_status_on()

    #Crea un hilo al cual se le asigna como objetivo la funcion enviar unidad de paquete
    #posteriormente se alamacena el hilo en la lista de hilos
    def entramar_paquete(self, package, path_package):
        hilo = threading.Thread(target= self.send_package_unit, args=(package,path_package))
        hilo.start()
        self.threads_list.append(hilo)
    
    def await_sincronized_matriz_status_on(self):
        for hilo in self.threads_list:
            hilo.join()


    #@param path_package = [[nodos],peso]
    def send_package_unit(self,package,path_package):
        time.sleep(path_package[1])
        self.receive_package.append([package, path_package])
        print("Paquete recibido")

    #Llama al interfaz para obtener el nodo de origen
    #el nodo destino y el mensaje
    def set_data_main(self):
        self.message , self.vertex_origin , self.vertex_destiny = interfaz.start(self.vertex_list)
    #Genera un conjunto de paquetes en base a un mensaje
    def generate_package(self):
        self.package_list = self.package_manager.message_to_package(self.message)
        
    def printDATAMAIN(self):
        print("Origen:", self.vertex_origin)
        print("Destino:",self.vertex_destiny)
        print("Paquetes:",self.package_list)

    #      0                    1
    #  0,0 0,1             1,0     1,1
    # 0,0 0,1           1,0,0       1,1
    #[[1,"cont"],[[ruta#1,ruta#2],peso_total]]
    def show_received_package(self):
        for i in self.receive_package:
            path_sexy = str()
            for j in range(len(i[1][0])):
                if j == len(i[1][0]):
                    path_sexy += i[1][0][j]
                else:
                    path_sexy += i[1][0][j] + " ==> "

            print(f"Paquete {i[0][0]}. contenido = {i[0][1]}.  Peso total = {i[1][1]}. Ruta = {path_sexy}.")
    
    def run(self):

        print("Controlando la situacion")
        self.fulfill_vertex_list()
        self.set_data_main()
        self.generate_package()
        self.printDATAMAIN()
        self.send_packages()
        
        print(self.receive_package)
        print("")
        print("Paquetes recibidos")
        self.show_received_package()
        #print(self.package_list)
        
        
