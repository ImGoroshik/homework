import random #код такой большой потому, что я решил сделать его красивее


print("    ●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●")
print("░░░░░░░░░░░░░░ДОБРО ПОЖАЛОВАТЬ ░░░░░░░░░░░░░")
print("    ●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●")
games = int(input("         Введите кол-во игр: "))
print(":::::::::::::::::::::::::::::::::::")
print("Ходы: 1-камень, 2-ножницы, 3-бумага")
print(":::::::::::::::::::::::::::::::::::")
winsChel = 0
winsBot = 0

for i in range (games):
	chelovek = int(input("                Ходите: "))
	bot = int(random.randint(1,3))

	print("------------------")
	if chelovek == 1 and bot == 1 or chelovek == 2 and bot == 2 or chelovek == 3 and bot == 3:
		print("Ничья!")
		winsBot += 0
		winsChel +=0
		print('Вы ' + str(winsChel) + ' : ' + 'Противник ' + str(winsBot))
		print("------------------")
	if chelovek == 1 and bot == 2:
		print("Вы победили!")
		winsChel += 1
		print('Вы ' + str(winsChel) + ' : ' + 'Противник ' + str(winsBot))
		print("------------------")
	if chelovek == 2 and bot == 3:
		print("Вы победили!")
		winsChel += 1
		print('Вы ' + str(winsChel) + ' : ' + 'Противник ' + str(winsBot))
		print("------------------")
	if chelovek == 3 and bot == 1:
		print("Вы выиграли!")
		winsChel += 1
		print('Вы ' + str(winsChel) + ' : ' + 'Противник ' + str(winsBot))
		print("------------------")	


	if chelovek == 1 and bot == 3:
		print("Вы проиграли!")
		winsBot += 1
		print('Вы ' + str(winsChel) + ' : ' + 'Противник ' + str(winsBot))
		print("------------------")
	if chelovek == 2 and bot == 1:
		print("Вы проиграли!")
		winsBot += 1
		print('Вы ' + str(winsChel) + ' : ' + 'Противник ' + str(winsBot))
		print("------------------")
	if chelovek == 3 and bot == 2:
		print("Вы проиграли!")
		winsBot += 1
		print('Вы ' + str(winsChel) + ' : ' + 'Противник ' + str(winsBot))
		print("------------------")
		
print("        !!Счет!!")
print("###########################")
print("#                         #")

print('# Вы: ' + str(winsChel) + ' : ' + 'Противник ' + str(winsBot) + '     #')
print("#                         #")
print("###########################")

if winsChel > winsBot:
	print("Вы выиграли противника!!")
elif winsChel == winsBot:
	print("Ничья!")
elif winsChel < winsBot:
	print("Вы проиграли!!")
