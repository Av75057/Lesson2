i = 1
k = 0
while i <= 10:
    p = input('Введите ' + str(i)  + ' цифру:')
    if p.isdigit() and len(p) == 1:
       if int(p) == 5:
          k +=1
       i +=1
    else:
        print('Некорректный ввод, попробуйте снова')
print('Количество введенных цифр 5 равно:',k)