sotrudniki = int(input('Введите количество сотрудников цифрой: '))
money = []
distance = []
stoimost = []
sotr1= 0
sto1= 0
c = 0
d = 0
while sotr1 < sotrudniki: #Вводятся все расстроения
    Km = int(input("Введите расстояние до дома сотрудника (цифрой): "))
    distance.append(Km)
    sotr1 += 1
while sto1 < sotrudniki: #ввод всех тарифов
    cashe = int(input('Введите тариф цифрой : '))
    money.append(cashe)
    money[sto1] = (money[sto1], sto1+1)
    sto1 += 1
dist = sorted(distance) #Сортировка расстояний
tar = sorted(money, reverse=True) #Сортировка тарифов 
while c < sotrudniki: #Вывод работников и такси по очереди
    print (c+1, "Сотрудник поедет на такси номер" , tar[c][1] )
    c += 1
while d < sotrudniki: #Счет за такси
    stoimost.append(dist[d]*tar[d][0])
    d += 1
num = sum(stoimost) #Итоговая сумма
#Присвоение букв
W1a = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
W1b = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
W2 = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
W3 = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
W4 = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
W5 = ["тысяча", "тысячи", "тысяч"]
R = ["рубль", "рубля", "рублей"]
num1 = (num // 100000)
num2 = (num // 10000) % 10
num3 = (num // 1000) % 10
num4 = (num // 100) % 10
num5 = (num // 10) % 10
num6 = (num % 10)
Number = "" 
if num1 != 0:
    i1 = num1 - 1
    Number += W4[i1] + " "
if num2 == 1 and num3 == 0:
    Number += W3[0] + " "
if num2 != 1:
    if num2 != 0:
        i2 = num2 - 1
        Number += W3[i2] + " "
if num3 != 0:
    if num2 == 1:
        i3 = num3 - 1
        Number += W2[i3] + " " + W5[2] + " "
    else:
        i3 = num3 - 1
        Number += W1b[i3] + " "
        if num3 == 1:
            Number += W5[0] + " "
        elif 1 < num3 < 5:
            Number += W5[1] + " "
        else:
            Number += W5[2] + " "
if (num3 == 0) and (num2 or num1 != 0):
    Number += W5[2] + " "
if num4 != 0:
    i4 = num4 - 1
    Number += W4[i4] + " "
if num5 == 1 and num6 == 0:
    Number += W3[0] + " "
if num5 != 1:
    if num5 != 0:
        i5 = num5 - 1
        Number += W3[i5] + " "
if num6 != 0:
    if num5 == 1:
        i6 = num6 - 1
        Number += W2[i6] + " " + R[2]
    else:
        i6 = num6 - 1
        Number += W1a[i6] + " "
        if num6 == 1:
            Number += R[0] + " "
        elif 1 < num6 < 5:
            Number += R[1] + " "
        else:
            Number += R[2] + " "
if (num6 == 0) and (num5 or num4 or num3 or num2 or num1 !=0):
    Number += R[2]
Number = Number.capitalize() #Вывод числа буквами
print ('Итоговая сумма =', num,'(', Number, ')')