#код в котором может возникнуть исключение помещено в try
try:
    #вводим четырехзначное число
    num=input("Enter a four-digit number:")
    #выводим на экран позиции четырехзначного числа с помощью индексов
    thousands = number // 1000
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    ones = number % 10

    print("Цифры числа:")
    print("Тысячи:", thousands)
    print("Сотни:", hundreds)
    print("Десятки:", tens)
    print("Единицы:", ones)

except ValueError:
    print("Ввод данных неверный")
