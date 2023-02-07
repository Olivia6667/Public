tickets = int(input("Введите количество необходимых билетов: "))
person = 1
cash = 0
while person <= tickets:
    age_for_ticket = int(input(f'Для какого возраста приобретается билет N{person}:'))
    if age_for_ticket < 18:
        print('Билет бесплатный')
    elif 25 > age_for_ticket >= 18:
        ticket_price = 990
        cash += ticket_price
        print(f'Стоимость билета: {ticket_price} рублей')
    else:
        ticket_price = 1390
        cash += ticket_price
        print(f'Стоимость билета: {ticket_price} рублей')
    person += 1
if tickets > 3:
        sale = cash - ((cash/100) * 10)
        print(f'Сумма к оплате {sale} рублей, применена скидка 10% за покупку более трёх билетов одновременно')
else:
        print(f'Сумма к оплате {cash} рублей')
