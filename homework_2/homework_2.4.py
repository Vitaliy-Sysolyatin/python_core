secret_number = 37
count_of_attempts = 0

while 1:
    number = int(input("Введите число: "))
    count_of_attempts += 1

    if number == secret_number:
        print("Успех! Число отгадано")
        print(f'Количество попыток: {count_of_attempts}')
        break
    elif number > secret_number:
        print("Введённое число больше секретного")
    else:
        print("Введённое число меньше секретного")