#Tiempo - Python


class Tiempo:
	def __init__(self, tiempo, tiempo2):
		self.tiempo = ""
		self.hora = "00"
		self.minutos = tiempo[:2]
		self.segundos = tiempo[3:]
		self.milisegundos = "000"

		self.tiempo_final = ""
		self.minutos_final = tiempo2[:2]
		self.segundos_final = tiempo2[3:]


	def pasar_tiempo(self):
		self.tiempo = f"{self.hora}:{self.minutos}:{self.segundos},{self.milisegundos}"


	def pasar_tiempo_final(self):
		self.tiempo_final = f"{self.hora}:{self.minutos_final}:{self.segundos_final},{self.milisegundos}"


	def getTiempo_ahora(self):
		return self.tiempo


	def getTiempo_final(self):
		return self.tiempo_final


	#00:00:00,267 --> 00:00:00,567
	def getTiempo(self):
		self.pasar_tiempo()
		self.pasar_tiempo_final()
		return f"{self.getTiempo_ahora()} --> {self.getTiempo_final()}"


if __name__ == "__main__":
	obt_time = Tiempo("00:00", "00:09")
	print(obt_time.getTiempo())