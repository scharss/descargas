from math import sqrt



a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))
c = float(input('Ingrese el valor de c: '))

if a == 0:
	print('No es una función de segundo grado')
else:
	z = b**2 - 4*a*c
if z < 0:
	print('No hay soluciones en los reales')
else:
	x1 = (-b + sqrt(z)) / (2 * a)
	x2 = (-b - sqrt(z)) / (2 * a)
if x1 == x2:
	print('Raíz: x1 =', round(x1, 2))
else:
	print('Raíz: x1 =', round(x1, 2), 'y x2 =', round(x2, 2))
    