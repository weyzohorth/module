#=[site officiel]=====================
#<<<<<mod_oct by W3YZOH0RTH>>>>>
#=====[http://progject.free.fr/]=======

# fonctions
#	conv_octm(valeur,debit=128,unite="m")
#		-> if unite != "ms": str else int
#	conv_msoct
#		-> int
#	conv_ms(string)
#		-> int
#	conv_oct(valeur,unite = "")
#		-> str

def conv_octm(valeur,debit=128,unite="m"):
	from mod_time import conv_time
	"""valeur en octet, debi en kb/s , unite = "m" ou "ms" ---> temps en mm:ss ou ms"""

	if unite != "ms":
		return conv_time(int(tronquer(valeur / (debit/8),3,"f")))
	else:
		return valeur / (debit/8)

#:::::::::::::::::::::::::::::::::::::::::::::::::
def conv_msoct(valeur,debit=128):
	"""valeur en ms, debit en kb/s ---> valeur en octet"""
	return valeur * (debit/8)

#:::::::::::::::::::::::::::::::::::::::::::::::::
def conv_ms(string):
	"""string de la forme hh:mm:ss ---> int ms"""
	liste = string.split(":")
	liste.reverse()
	ms = 0
	for i in range(len(liste)):
		ms += int(liste[i])*pow(60,i)
	return ms * 1000

#:::::::::::::::::::::::::::::::::::::::::::::::::
def conv_oct(valeur,unite = ""):
	"""valeur en octet[,unite = 'o','k','m','g' ou 't'] ---> valeur en o, ko ou mo"""
	if float(valeur)/1024 < 1 and unite == "" or unite == "o":
		return str(valeur)+" o"
	elif float(valeur)/1024 < 1024 and unite == "" or unite == "k":
		return str(float(valeur)/1024)+" ko"
	elif float(valeur)/(1024**2) < 1024 and unite == "" or unite == "m":
		return str(float(valeur)/(1024**2))+" Mo"
	elif float(valeur)/(1024**3) < 1024 and unite == "" or unite == "g":
		return str(float(valeur)/(1024**3))+" Go"
	else:
		return str(float(valeur)/(1024**4))+" To"
