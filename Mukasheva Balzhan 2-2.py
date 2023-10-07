#код в котором может возникнуть исключение помещено в try
try:
    #вводим четырехзначное число
    num=input("Enter a four-digit number:")
    #выводим на экран позиции четырехзначного числа с помощью индексов
   first_position=num/10
   second_position=num%10
   print(f"Позиция первая {first})

except ValueError:
    print("Ввод данных неверный")
