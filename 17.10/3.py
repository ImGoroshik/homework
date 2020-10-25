dolar = int(float(input("1 кг конфет стоит 20 руб.\nВведите курс доллора в рублях.\n1$=  ")))

for i in range(1, 101):
	print(i, end='')
	print(' $' + ' = ' + str(dolar * i)+ ' rub' + ' = ' + str((dolar * i)/20 ) + 'kg')