import random
from Individuo import Individuo
#
class Poblacion():
	# !Estas variables se comparte entre todos los objetos de la clase Poblacion

	poblacion=[] #Arreglo de Strings binarias de cada individuo
	individuos=[] #Arreglo de Objetos tipo Individuo    
	valorRealIndividuo=[]
	valorDeLaFuncion=[]
	probabilidadIndividuo=[]
	suma=0
	valor=0


	intervaloRuleta=[]
	valorRuleta=0


	"""docstring for Poblacion"""
	def __init__(self, intervalo, n): 
		 
		self.generarPoblacion(intervalo,n)
		self.calcularFuncion()
		self.calcularSuma()
		self.calcularProbabilidad()
	
	def generarPoblacion(self, intervalo, n):
		#Se itera n veces y en cada una se agrega un arreglo (individuo), al arreglo Poblacion
		for x in range(n):
			individuo=Individuo(intervalo)
			self.individuos.append(individuo) #Inserta los objetos individuos en el arreglo 'individuos'
			#Devuelve la cadena binaria y la guarda en el arreglo poblacion
			self.poblacion.append(individuo.getCromosoma())
			#Esta parte añade el valor real (de binario a entero) de cada individuo en el arreglo 'numeroReal'
			self.asignarValorReal()
			#valorRealIndividuo=individuo.getValorRealIndividuo()
			#self.valorRealIndividuo.append(valorRealIndividuo)
			#añade el valor de la funcion objetivo evaluada en el arreglo numeroReal
			#self.valorDeLaFuncion.append(self.funcion(valorRealIndividuo))
			
	#Aqui van las funciones get que devuelven valores en el main		
	#Metodo que regresa la variable poblacion		
	def getPoblacion(self):
				return self.poblacion

	#Regresa el arreglo de valores reales de la cadena codificada			
	def getValorRealIndividuoArray(self):
		return self.valorRealIndividuo

	def getValorDeLaFuncion(self):
			return self.valorDeLaFuncion
	def getSuma(self):
					return self.suma

	def getProbabilidades(self):
			return self.probabilidadIndividuo	

	def getIntervaloRuleta(self):
			return self.intervaloRuleta	

	def getValorRuleta(self):
			return  self.valorRealIndividuo[self.valorRuleta] #Devuelve el individuo correspondiente al valor de la		

	#Guarda en el arreglo valorRealIndividuo los valores correspondientes a su representacion decimal
	def asignarValorReal(self):
		self.valorRealIndividuo=[]
		for i in range(len(self.individuos)):
			self.valorRealIndividuo.append(self.individuos[i].getValorRealIndividuo())

#Esta es la funcion objetivo, en ella se evalua el arreglo de numeros reales 
	def funcion(self, valorIndividuo):
			return valorIndividuo**2	 #x**2

#Calcula el valor de la funcion, recibe el arreglo de valores reales y anade los valores a 'valorDeLaFuncion'
	def calcularFuncion(self):
			for valorRealIndividuo in self.valorRealIndividuo:
				self.valorDeLaFuncion.append(self.funcion(valorRealIndividuo))
	def calcularSuma(self):   
			for x in self.valorDeLaFuncion:
				self.suma=self.suma+x

#Calcula la probabilidad de cada individuo, divide el valor de su funcion entre el valor de la suma				
	def calcularProbabilidad(self):
			for x in self.valorDeLaFuncion:
				tempProbabilidad=x/self.suma
				self.probabilidadIndividuo.append(tempProbabilidad)

	def generarNuevaPoblacion(self):
		anterior=0
		siguiente=0
		poblacionRuleta=[]	
		self.intervaloRuleta.append(0)			
		for x in self.probabilidadIndividuo:
			indice=0
			siguiente=siguiente+x #valorDeLaFuncion es el diccionario creado localmente en ruleta()
			self.intervaloRuleta.append(siguiente)
			anterior=siguiente
			indice=indice+1

		print('Intervalo de Ruleta')
		print(self.intervaloRuleta)	
		for i in range(len(self.poblacion)):
			#Intercambia el valor de cada string binaria de la poblacion por otra del mismo arreglo dado por el valor devuelto por ruleta()
			poblacionRuleta.append(self.poblacion[self.ruleta()]) 
			self.individuos[i].setCromosoma(self.poblacion[i])
		self.asignarValorReal()
		self.poblacion=poblacionRuleta
		self.calcularFuncion()
		self.calcularSuma()
		self.calcularProbabilidad()
		print('La poblacion ahora es:')
		print(self.getPoblacion())	

	def ruleta(self):
			dardo = random.random()
			print('Valor del dardo')
			print(dardo)
			self.valorRuleta = 0
			for i in range(len(self.intervaloRuleta)):
				if dardo < self.intervaloRuleta[i+1]:
					elegido = self.valorRealIndividuo[i]
					print('El elegido es')
					print(elegido)
					return i #Regresa el indice del elegido
					break		
		
	def cruceYMutacion():
			pass	
	
	
#Poblacion deberia tener un arreglo de Objetos tipo Individuo, cada uno de los cuales debe usar los metodos que definimos			
