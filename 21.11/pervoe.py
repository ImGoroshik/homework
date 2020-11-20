stroka = input("Введите все, что угодно с пробеломи:")
lin = stroka.split()#split разрезает строку по пробелам
NewStroka = ' '.join(lin)#join список строк
print(NewStroka)