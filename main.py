import random 
from Individuo import Individuo
from Poblacion import Poblacion
		
def ruleta(self, numeroIndividuos, individuos, valorDeLaFuncion, probabilidades):
	arreglo={}
	numero=0.5
	anterior=0
	poblacionRuleta=[]

	#for x in probabilidades:
	 # siguiente=x
	  #if (numero>anterior)&&(numero<siguiente):
		
		


		


#Intervalo en donde se buscara una solucion
intervalo=[0,4]
print('Intervalo [0,4]\n')
#numero de individuos del AG
numeroIndividuos=5
#Se declara un objeto poblacion, recibe el intervalo y el numero de individuos
poblacion=Poblacion(intervalo, numeroIndividuos)
#Se imprime la poblacion generada
print('Poblacion codificada en Binario:\n')
print(poblacion.getPoblacion())
#ind=Individuo(intervalo)
print('Valor decodificado de cada individuo\n')
print(poblacion.getValorRealIndividuoArray())
print('Funcion evaluada en cada individuo:\n')
print(poblacion.getValorDeLaFuncion())
print()
print('Suma de f(x):\n')
print(poblacion.getSuma())
print('Probabilidad de cada Individuo:\n')
print(poblacion.getProbabilidades())
print()

individuos=poblacion.getValorRealIndividuoArray()
valorDeLaFuncion=poblacion.getValorDeLaFuncion()
probabilidades=poblacion.getProbabilidades()

print('Valor de la recta de la Ruleta')
poblacion.generarNuevaPoblacion()
print()
#print('Intervalo Ruleta')
#print(poblacion.getIntervaloRuleta())
#print('El valor del individuo es: ')
#print(poblacion.getValorRuleta())



#Seleccion de las soluciones mejor adaptadas...