import json

file_name = "users.json"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        users = json.load(file)

    for user in users:
        print("-------------------------")
        print("Пользователь:", user["login"])
        print("Пароль:", user["password"])
        print("Статус авторизации:", user["expected_result"])

except FileNotFoundError as e:
    print(f"Ошибка: файл не найден {e}")

except KeyError as e:
    print(f"Ошибка: отсутствует обязательное поле {e}")

except json.JSONDecodeError as e:
    print(f"Ошибка: файл содержит некорректный JSON {e}")
