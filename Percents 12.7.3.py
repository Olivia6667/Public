per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
money = int(input("Введите сумму вклада:"))
tkb = per_cent['TKB']*money/100
skb = per_cent['SKB']*money/100
vtb = per_cent['VTB']*money/100
sber = per_cent['SBER']*money/100
print ("Вы заработаете с вклада в ТКБ:", tkb)
print ("Вы заработаете с вклада в СКБ:", skb)
print ("Вы заработаете с вклада в ВТБ:", vtb)
print ("Вы заработаете с вклада в СБЕР:", sber)
deposit = [tkb, skb, vtb, sber]
max_number = max(deposit)
print("Максимальная сумма, которую вы можете заработать — ", max_number)