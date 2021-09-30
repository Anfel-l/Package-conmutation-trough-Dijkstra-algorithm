#Implementación de algoritmo Dijkstra

"""
	Nodos = Enrutadores = Vertices
	Aristas = Medio

"""
"""Clase cuyo fin es describir el contenido pertinente de cada vertice"""
class Vertex:

	#Método constructor
	def __init__(self, i):
		
		#identificador del vertice (en este caso, la IP del host)
		self.id = i

		#lista que almacena los nodos vecinos
		self.neighbors = []

		#Atributo que indica si el enrutador ya fue visitado
		self.visited = False

		#Atributo que me indica el predecesor del enrutador
		self.predecessor = None

		#Atributo que me indica el peso de las aristas
		self.weight = float('inf')

	#Esta función recibe como parámetros el id del vertice y el peso
	#de la arista del enrutador vecino
	def add_neighbor(self, v, p):

		#Si el nodo no está en la lista de vecinos
		if v not in self.neighbors:

			#Agrego una lista a vecinos con el indice de vecino en [0]
			#y el peso de la arista con el vecino en [1] 
			self.append([v, p])

"""Clase cuyo fin es implementar el grafo que será utilizado para 
   representar la topología de red planteada"""
class Graph:

	#Método constructor
	def __init__(self):

		"""
			Defino un diccionario en el cual su estructura será la siguiente
			{clave:valor}
			{IDdelVertice:ObjetoTipoVertice}

		"""
		self.vertices = {}

	#Esta función recibe como parámetro el id del vertice que quiero agregar
	def add_vertex(self, v):

		#Si el nodo con id 'v' no se encuentra en mi diccionario, lo agrego
		if v not in self.vertices(v):

			#Agrego el id del vertice a mi diccionario
			#Agrego el vertice indicando el objeto de tipo Vertice
			self.vertices[v] = Vertex(v)

	#Esta funcion recibe como parametros dos vertices y el peso que habrá
	#entre ellos
	def add_edge(self, a, b, p):

		#Primero confirmo si ambos vertices se encuentran en mi diccionario
		if a in self.vertices and b in self.vertices:

			#primero accedo al vertice con el id 'a' y
			#le indico que el nodo destino es b y el peso de su arista será p
			self.vertices[a].add_neighbor(b, p)

			#primero accedo al vertice con el id 'b' y
			#le indico que el nodo destino es a y el peso de su arista será p
			self.vertices[b].add_neighbor(a, p)

			"""
			Con esto establezco la ruta de los vertices, es decir
			de (a -> b) y (b -> a)

			"""

		#Si no se encuentran me voy a la pija
		else:
			return False

	#Esta función me permitirá conocer la distancia mínima de los enrutadores
	#que no han sido visitados para realizar la siguiente operación del algoritmo
	def minimum(self, lista):

		#Compruebo que no esté vacía	
		if len(lista)>0:

			#Defino una var 'm' con la que capturo el peso del vertice
			m = self.vertices[lista[0]].weight
			v = lista[0]

			#Ahora realizo una búsqueda a través de la lista
			for e in lista:

				#Si el peso m es mayor a el peso del vertice recorrido
				if m > self.vertices[e].weight:

					#Reemplazo el valor del peso del vertice recorrido por
					#el valor del peso m
					m = self.vertices[e].weight

					#capturo el valor mínimo en la varibale 'v'
					v = e
			return v
		
	#Esta función será la implementación del algoritmo Dijkstra, recibe como
	#parámetro el nodo inicial
	def dijkstra(self, a):

		"""
		Algoritmo Dijkstra (En palabras de Andrés :D )

		1. En primar lugar, debo asignar el peso del nodo inicial como 0 y su predecessor nulo
		asimismo, a los demas nodos les asigno peso 'infinito' y predecessor nulo
		
		2. Establezco el nodo inicial como 'nodo actual' y creo una lista de los nodos que no han 
		sido visitados.

		(Paso de iteración hasta completar el algoritmo)
		3. Mientras la lista de nodos no visitados sea diferente de cero, hago lo siguiente:
			
			>> Para el nodo actual (a), teniendo en cuenta sus vecinos no visitados (b) y 
			   considerando además su peso w:

			   - Si la suma del peso del nodo actual (a) y el peso de la arista (w) es menor
			   que el peso del nodo (b), entonces debo actualizar el peso de (b) con el resultado
			   de la suma entre (a) y (w). Además, debo guardar al nodo (a) como predecesor de (b)
			
			>> Una vez se hayan visitado todos los nodos vecinos, y después de realizado el paso
			   anterior, marco el nodo como visitado y lo elimino de mi lista de nodos no visitados.

			>> Ahora selecciono el nodo que no ha sido visitado con menor peso parcial y lo marco 
			   como nuevo nodo actual. Regreso al paso número 3.
		"""

		#Me aseguro de que esté en mi diccionario
		if a in self.vertices:
			
			#Primer paso, establezo el peso del nodo inicial como 0 
			#y lo establezco como actual
			self.vertices[a].weight = 0
			actual = a

			#Creo lista de nodos no visitados
			not_visited = []

			#recorro mi diccionario
			for v in self.vertices:
				
				#Me aseguro de no cambiar al nodo inicial 'a'
				if v != a:

					#Segundo paso, establezco el peso 'infinito' de los demás vertices
					#recorriendo el diccionario y le añado su predecesor como nulo
					self.vertices[v].weight = float('inf')
					self.vertices[v].predecessor = None

					#Añado los nodos a mi lista de no visitados
					not_visited.append(v)

			#Paso 3, condición mientras, me aseguro de que la lista no esté vacía
			while(len(not_visited)>0):

				#Establezo 'neigbor' para recorrer a los nodos vecinos
				for neighbor in self.vertices[actual].neighbors:

					#Si el nodo vecino aún no ha sido visitado
					if self.vertices[neighbor[0]].visited == False:

						#Si el peso del nodo actual más el valor de la arista hacia el vecino
						#es menor que el peso del nodo vecino (recordad que existe una lista en
						#la cual 0 indica el id y 1 al peso de la arista del nodo vecino)
						if self.vertices[actual].weight + neighbor[1] < self.vertices[neighbor[0]].weight:
							
							#Asigno el peso del vecino con el nuevo valor que corresponderá a la suma entre
							#el peso del nodo origen y el peso del nodo vecino
							self.vertices[neighbor[0]].weight = self.vertices[actual].distancia + vecino[1]
							
							#Asigno al predecesor del nodo vecino como el nodo actual
							self.vertices[neighbor[0]].predecessor = actual

				#Indico que el nodo actual ya fue visitado
				self.vertices[actual].visited = True			

				#Invoco a la función 'minimum' para saber qué nodo será el próximo nodo actual
				actual = self.minimo(not_visited)
		
		#Si no está en el diccionario me piro
		else:
			return False

	""" Funciones extra """

	#Esta función recorrerá el diccionario y permitirá imprimir su contenido
	def print_graph(self):
		
		#recorro el diccionario con 'v'
		for v in self.vertices:
			print ("The weight of the vertex is " +
				str(v) + " is " + str(self.vertices[v].weight) + 
				" coming from " + str(self.vertices[v].predecessor))

	#Esta función recorrerá el diccionario y establecerá el camino que se ha recorrido
	#recibe como parámetro el nodo origen y el nodo destino
	def path(self, a, b):

		#Lista para guardar los nodos recorridos
		path = []
		actual = b

		#Mientras el nodo no esté vacío
		while actual != None:

			#Agrego el nodo actual al principio del camino
			path.insert(0, actual)

			#Actualizo el nodo actual con su predecesor
			actual = self.vertices[actual].predecessor

		#retorno una lista con el nodo actual y el peso final del nodo destino 
		return [path, self.vertices[b].weight]





#Prueba de algoritmo con direcciones IP
class main:
	
	g = Graph()

	#Añado todos los hosts
	g.add_vertex("192.168.0.1")
	g.add_vertex("192.168.0.2")
	g.add_vertex("192.168.0.3")
	g.add_vertex("192.168.0.4")
	g.add_vertex("192.168.0.5")
	g.add_vertex("192.168.0.6")

	#Establezco el peso de las aristas, recordando que el
	#primer parámetro es el actual, el segundo el vecino y el tercero el peso

	g.add_edge("192.168.0.1", "192.168.0.6", 14)
	g.add_edge("192.168.0.1", "192.168.0.2", 7)
	g.add_edge("192.168.0.1", "192.168.0.3", 9)
	g.add_edge("192.168.0.2", "192.168.0.3", 10)
	g.add_edge("192.168.0.2", "192.168.0.4", 15)
	g.add_edge("192.168.0.3", "192.168.0.4", 11)
	g.add_edge("192.168.0.3", "192.168.0.6", 2)
	g.add_edge("192.168.0.4", "192.168.0.5", 6)
	g.add_edge("192.168.0.5", "192.168.0.6", 9)

	print("The fastest route and its weight is: \n")

	#Indico el nodo inicial (Aquí se puede recibir de la interfaz)
	g.dijkstra("192.168.0.1")

	#Indico e imprimo que camino quiero calcular (Aquí se puede recibir de la interfaz)
	print(g.path("192.168.0.1", "192.168.0.2"))

	print("Final weights: \n\n")
	g,print_graph

	