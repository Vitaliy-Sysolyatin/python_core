test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]


def print_report(test_cases, statuses):
    statistics = {"PASS": 0, "FAIL": 0, "SKIP": 0}

    for test, status in zip(test_cases, statuses):
        print(test, "—", status)
        statistics[status] += 1

    print("-------------------------")

    print("Успешных тестов:", statistics["PASS"])
    print("Неуспешных тестов:", statistics["FAIL"])
    print("Пропущенных тестов:", statistics["SKIP"])

    print("-------------------------")

    if statistics["FAIL"] > 0:
        print("Тестовый запуск неуспешен")
    else:
        print("Тестовый запуск успешен")


print_report(test_cases, statuses)