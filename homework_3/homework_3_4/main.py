import test_data


def get_status_statistics(users):
    statistics = {"ACTIVE": 0, "BLOCKED": 0, "INACTIVE": 0}

    for user in users:
        status = user["status"]
        statistics[status] += 1

    return statistics


try:
    count = int(input("Количество пользователей: "))
except ValueError:
    print("Введите число")
else:
    if count < 1:
        print("Количество пользователей должно быть больше 0")
    else:
        users = []

        for i in range(count):
            users.append(test_data.generate_user())

        print("\nПользователи:")

        for user in users:
            print(user)

        statistics = get_status_statistics(users)

        print("\nСтатистика:")

        for status, count in statistics.items():
            print(status + ":", count)