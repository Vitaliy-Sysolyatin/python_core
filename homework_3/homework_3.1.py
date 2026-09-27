def get_test_statistics(results):
    statistics = {"PASS": 0, "FAIL": 0, "SKIP": 0, "UNKNOWN_STATUS": 0}

    for result in results:
        if result in statistics:
            statistics[result] += 1
        else:
            statistics["UNKNOWN_STATUS"] += 1

    return statistics


tests = input("Введите результаты тестов через пробел: ")
results = tests.upper().split()
statistics = get_test_statistics(results)
total_tests = len(results)

if total_tests > 0:
    passed_percent = round(statistics["PASS"] / total_tests * 100, 1)
else:
    passed_percent = 0

print("Всего тестов:", total_tests)
print("PASS:", statistics["PASS"])
print("FAIL:", statistics["FAIL"])
print("SKIP:", statistics["SKIP"])
print("UNKNOWN_STATUS:", statistics["UNKNOWN_STATUS"])
print(f"Успешно: {passed_percent}%")