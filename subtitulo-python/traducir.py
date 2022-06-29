#Traducir Texto - Python

from googletrans import Translator

translator = Translator()
directorio = "C:\\Users\\Yilver\\Downloads\\Marine Online\\Steering Gear"
texto = []
nuevo_texto = []


def leer(numero=1):
	global texto
	with open(f"{directorio}\\sub{numero}.txt", "r") as file:
		texto = [line for line in file]
	file.close()


def traducir():
	global nuevo_texto
	linea = 0
	for i in texto:
		linea += 1
		if linea % 2 == 0:
			resultado = translator.translate(i, src="en", dest="es")
			nuevo_texto.append(resultado.text.strip() + "\n")
		else:
			nuevo_texto.append(i)


def cambiar_texto(numero=1):
	with open(f"{directorio}\\sub{numero}_espa\xf1ol.txt", "w") as file:
		for i in nuevo_texto:
			try:
				file.write(i)
			except:
				print(i)
				file.write("Subtitulo no Encontrado\n")
				pass
	file.close()
'''
from googletrans import Translator

translator = Translator()
print(translator.translate('Hola Mundo', src="es", dest='en'))
result = translator.translate('Hellor World, Good Bye', src="en", dest="es")
print(result.text)
'''

def main_traducir(numero):
	leer(numero)
	traducir()
	cambiar_texto(numero)


if __name__ == "__main__":
	for i in range(8):
		print(f"Traduciendo Archivo {i+1}...")
		main_traducir(i+1)
		print("Archivo Traducido\n")