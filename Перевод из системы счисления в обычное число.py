def cod():
    x = input('Введите число: ')
    n = int(input('Введите систем счисления: '))
    if n > 9:
        x = x[::-1]
        a = []
        a.extend(x)
        c = 0
        z = [10, 11, 12, 13, 14, 15]
        for i in range(len(a)):
            if a[i] == 'A':
                a[i] = z[0]
            elif a[i] == 'B':
                a[i] = z[1]
            elif a[i] == 'C':
                a[i] = z[2]
            elif a[i] == 'D':
                a[i] = z[3]
            elif a[i] == 'E':
                a[i] = z[4]
            elif a[i] == 'F':
                a[i] = z[5]
            c += int(a[i]) * n**i
        print(c)
    elif n <= 9:
        x = x[::-1]
        c = 0
        for i in range(len(x)):
            c += int(x[i]) * n**i
        print(c)
    x = input('Продолжить работу с новыми числами? Если да, то нажмите "д". Если или нет, то нажмите "н": ')
    while x != 'д' and x != 'н':
        print('Введите правильный символ')
        x = input()
    if x == 'д':
        cod()
    elif x == 'н':
        print('Успехов в Ваших замыслах')
cod()
input()