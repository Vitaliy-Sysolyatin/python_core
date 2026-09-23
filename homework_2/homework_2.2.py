password = "Python123"

for number in range(3):
    user_password = input("Введите пароль: ")

    if password == user_password:
        print("Авторизация успешна!")
        break
else:
    print("Доступ заблокирован")