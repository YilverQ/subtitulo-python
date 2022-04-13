#Main - Python

from traducir import *
from subtitulo import *
import os

directorio = "C:\\Users\\Yilver\\Downloads\\Engine-Room Resource"
contenido = []
archivos_textos = []


def listar():
	global contenido
	contenido.clear()
	contenido = os.listdir(directorio)


def archivo_txt():
	listar()
	global archivos_textos
	archivos_textos.clear()
	for i in contenido:
		if i[-3:] == "txt":
			archivos_textos.append(i)
		else:
			pass

def principal_traducir():
	archivo_txt()
	for i in archivos_textos:
		numero = i[3]
		print(f"Traduciendo {i}")
		main_traducir(numero)
		print(f"{i} Ha Sido Traducido")



def principal_subtitulo():
	archivo_txt()
	for i in archivos_textos:
		numero = i[3]
		texto = i[:-4]
		main_subtitulo(numero, texto)


if __name__ == "__main__":
	#principal_traducir()
	principal_subtitulo()