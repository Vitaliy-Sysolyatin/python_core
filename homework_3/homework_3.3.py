import random

tests = ["test_login", "test_logout", "test_registration", "test_profile", "test_payment", "test_search"]
statuses = ["PASS", "FAIL", "SKIP"]

try:
    count = int(input("Сколько тестов запустить: "))
except ValueError:
    print("Введите число")


else:
    if count < 1 or count > len(tests):
        print(f"Ошибка: такого количества тестов нет. "
              f"Всего доступно: {len(tests)} тестов")
    else:
        selected_tests = random.sample(tests, count)
        statistics = {"PASS": 0, "FAIL": 0, "SKIP": 0}

        for test in selected_tests:
            status = random.choice(statuses)
            statistics[status] += 1

            print(test, "—", status)

        print()
        print("Статистика:")

        for status, count in statistics.items():
            print(status + ":", count)