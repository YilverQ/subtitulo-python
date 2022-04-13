#Python - Convertidor de Segundos

class Convertido:
	def __init__(self, tiempo):
		self.tiempo = tiempo
		self.hora = self.tiempo[0:2]
		self.minutos = int(self.tiempo[3:5])
		self.segundos = int(self.tiempo[6:8])

	def __str__(self):
		return f"""
		Tiempo: {self.tiempo}
		Hora: {self.hora}
		Minutos: {self.minutos}
		Segundos: {self.segundos}
		"""

	def convertir_tiempo(self, restar):
		if self.segundos>=25:
			self.segundos = self.segundos - restar
		else:
			if self.minutos != 0:
				self.minutos -= 1
				self.segundos += 60
				self.segundos = self.segundos - restar
			else:
				self.segundos = 0


	def convertir_digito(self):
		if len(str(self.minutos)) == 1:
			self.minutos = f"0{self.minutos}"
		if len(str(self.segundos)) == 1:
			self.segundos = f"0{self.segundos}"


	def actualizar(self):
		self.nuevo_tiempo = f"{self.hora}:{self.minutos}:{self.segundos}"


	def getTiempo(self):
		return self.nuevo_tiempo



def funcion_convertir(texto_hora,segundos):
	hora = Convertido(texto_hora)
	hora.convertir_tiempo(segundos)
	hora.convertir_digito()
	hora.actualizar()
	return hora.getTiempo()