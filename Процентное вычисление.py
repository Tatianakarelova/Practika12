money = int (input('Внесите сумму вклада:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
for key in per_cent:
    per_cent [key] = per_cent [key] * money/100
deposit = (list(per_cent.values ()))
print (deposit)
print (max(deposit))
