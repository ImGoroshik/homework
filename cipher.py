string = one = str(input("Введите текст: "))

summ = ''
b = 0
dlina = int(len(one))
a = len(one)//2
one = string[a: len(string)]
two = string[0:a]

while b < a:
    StrOne = one[b]
    StrTwo = two[b]
    summ += StrOne + StrTwo
    b += 1

if b < len(one) + 1:
    summ += one[b]

print(summ)
print(string)

