import random
from Cromosoma import Cromosoma

class Individuo():
	def __init__(self, intervalo):
		self.generarIndividuo(intervalo)
	def generarIndividuo(self, intervalo):
		objCromosoma=Cromosoma(intervalo)
		#Cromosoma del individuo, en esta parte se guarda el arreglo de bits
		self.cromosoma=objCromosoma.getCadenaCromosoma()
		self.valorIndividuo=int(self.cromosoma,2)
	
	def getCromosoma(self):
			return self.cromosoma	
			
	def setCromosoma(self, stringCromosoma):
		self.cromosoma=stringCromosoma #Se puede modificar el valor del string cromosoma
		self.valorIndividuo=int(self.cromosoma,2) #Reestablece el valor real del individuo

	#Regresa el valor real de un Individuo		
	def getValorRealIndividuo(self):
			return self.valorIndividuo		


		

			
			


