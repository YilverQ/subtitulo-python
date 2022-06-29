#Hacer Subtitulos de Youtube
#Convertir Archivo txt en srt
from tiempo import *

directorio = "C:\\Users\\Yilver\\Downloads\\Marine Online\\Steering Gear"



def funcion_leer(numero):
	global texto, final_numero
	with open(f"{directorio}\\sub{numero}_espa\xf1ol.txt", "r") as file:
		texto = [line for line in file]
	final_numero = texto[-2]


def funcion_escribir(numero):
	linea_total = 0
	itertador = 0
	linea_iterada = 1
	with open(f"{directorio}\\sub{numero}_espa\xf1ol.srt", "w") as file:
		for i in texto:
			if linea_iterada % 2 != 0:
				linea_iterada += 1
				itertador +=1
				file.write(str(itertador)+"\n")
				try:
					obj_time = Tiempo(i.rstrip('\n'),texto[linea_iterada].rstrip('\n'))
				except:
					obj_time = Tiempo(i.rstrip('\n'),final_numero.rstrip('\n'))
				
				file.write(obj_time.getTiempo()+"\n")
				pass
			else:
				linea_iterada += 1
				file.write(i+"\n")
				pass


if __name__ == "__main__":
	for i in range(8):
		funcion_leer(i+1)
		funcion_escribir(i+1)
