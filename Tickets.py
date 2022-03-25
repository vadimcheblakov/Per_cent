tickets = int(input("Введите количество билетов: "))
cost = 0

for i in range(tickets):
    age = int(input("Введите ваш возраст: "))
    i += 1
    if age < 18:
        print("Бесплатно!")
    elif 18 <= age < 25:
        cost += 990
        print('Билет стоит 990 рублей')
    else:
        cost += 1390
        print("Билет стоит 1390 рублей")
if tickets > 3:
    cost = cost*0.9
    print("Стоимость билетов с 10% скидкой для 3+ человек: ", cost)
else:
    print("Общая сумма к оплате", cost)