#Python - Leer el archivo STR

from hora_aventura import *
import os 

texto_nuevo = []
segundos = 25
texto = []


directorio = "C:\\Users\\Yilver\\Videos\\Series\\Adventure Time\\Adventure Time - Temporada 3\\Subtitulos"
contenido = os.listdir(directorio)


def nuevo_tiempo(texto_comun):
	inicio_num = texto_comun[:8] 
	final_num = texto_comun[17:25]
	texto_final = f"{funcion_convertir(inicio_num, segundos)}{texto_comun[8:17]}{funcion_convertir(final_num, segundos)}{texto_comun[25:]}"
	return texto_final


def funcion_leer(numero):
	global texto
	with open(f"Subtitulo Adventure - 3x{numero}.srt", "r") as file:
		texto = [line for line in file]


def funcion_escribir(numero):
	with open(f"Subtitulo Adventure - 3x{numero}.srt", "w") as file:
		for i in texto_nuevo:
			file.write(i)

def funcion_nueva_linea():
	for i in texto:
		linea = i
		if i[:2] == "00":
			linea = nuevo_tiempo(i)
		texto_nuevo.append(linea)


for i in contenido:
	texto.clear()
	texto_nuevo.clear()
	if i[-3:] == "srt":
		numero = i[24:26]
		funcion_leer(numero)
		funcion_nueva_linea()
		funcion_escribir(numero)