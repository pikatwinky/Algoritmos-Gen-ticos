import random

class Gen():
	"""docstring for Gen"""
	def __init__(self):
		self.alelo=random.randint(0,1)
	#Devuelve la representacion string del alelo, 0 1 en formato string	
	def __str__(self):
			return str(self.alelo) 	
	#Devuelve la variable alelo		
	def getAlelo(self):
				return str(self.alelo)		

	