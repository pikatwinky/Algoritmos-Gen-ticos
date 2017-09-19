from Gen import Gen
import random

class Cromosoma():
	"""docstring for Cromosoma"""
	def __init__(self, longitudCromosoma):
		self.codificarCromosoma(longitudCromosoma)
    
    #Genera los bits del cromosoma de forma aleatoria
	def codificarCromosoma(self, intervalo):
		self.cromosoma=''
		#Recibe el intervalo y usa el extremo superior del mismo para calcular el numero de bits del cromosoma
		ultimoEnBin="{0:b}".format(intervalo[-1])
		longitudCromosoma=len(ultimoEnBin)
		for x in range(longitudCromosoma):
			gen=Gen()
			self.cromosoma=self.cromosoma+gen.getAlelo()	
	#Regresa la cadena de bits que se guardaran en el cromosoma del individuo
	def getCadenaCromosoma(self):
		return self.cromosoma				
	