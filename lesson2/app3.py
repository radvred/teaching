buy = int(input())
if buy > 5000:
    print('Итоговая сумма со скидкой:', (buy * 0.9))
if buy <= 5000:
    print('Скидка не применяется. Итог:', buy)