import re
#https://www.youtube.com/watch?v=u3WBRgpxQcc
#Curso Python. Expresiones regulares IV. Vídeo 72

nombre1="Sandra López"
nombre2 = "Antonio Gómez"
nombre3 = "sandra López"

if re.match("Sandra",nombre3, re.IGNORECASE):
	print("ok")
else:
	print("no G")