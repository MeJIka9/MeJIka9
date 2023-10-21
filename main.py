i = 0 #перемнная триггер
while i == 0: #создание цикла
    try: #проверка на текст
        first = float(input()) #три принимающие переменные
        second = float(input())
        third = float(input())
#проверка на условие задачи
        if first + second > third and first > 0 and second > 0 and third > 0:
#логика программы
            func1 = (first + second + third) / 2

            result = (func1 * (func1 - first) * (func1 - second) * (func1 - third)) ** 0.5
            print(result) #вывод результата
            i = i + 1 #закрытие тригера для приостановки цикла
        else:
            print('Введите правильные данные')

    except:
        print('Введите букву а не число')