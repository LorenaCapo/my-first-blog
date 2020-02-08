#def hi(name):
#	print('Hola ' + name + '!')

#girls = ['Lorena', 'Cloe', 'Daniela', 'Capi']
#for name in girls:
#	hi(name)
#	print(name)
#	print('Next')


#Prueba clases

class Persona():
	nombre = None
	edad = None

	def __init__(self, n):
		self.nombre=n

	def informacion(self):
		print(self.nombre)	
		print(self.edad)

pruebaPersona = Persona('Lorena')
pruebaPersona.informacion()
