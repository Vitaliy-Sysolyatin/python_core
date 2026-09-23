for user in range(1,21):
    if user == 18:
        break

    if user == 5 or user == 10 or user == 15:
        continue

    print(f'Запущено тестирование для пользователя {user}')