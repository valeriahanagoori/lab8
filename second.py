#9
ye = int(input('Введите год: '))
if ye%4 == 0 and ye%400 == 0:
    print(ye, '- високосный год')
elif ye%4 == 0 and ye%100!=0:
    print(ye, '- високосный год')
else:
    print(ye, '- не високосный год')