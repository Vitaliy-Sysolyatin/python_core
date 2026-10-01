from functools import reduce

tests = [{"name": "auth_test", "status": "PASS", "duration": 1.0},
    {"name": "profile_test", "status": "PASS", "duration": 4.6},
    {"name": "payment_test", "status": "SKIP", "duration": 3.2},
    {"name": "settings_test", "status": "FAIL", "duration": 2.0},
    {"name": "cart_test", "status": "FAIL", "duration": 0.7},
    {"name": "registration_test", "status": "PASS", "duration": 10}, ]

statistics = {"PASS": 0, "FAIL": 0, "SKIP": 0, }

for test in tests:
    statistics[test["status"]] += 1

failed_tests = list(filter(lambda x: x["status"] == "FAIL", tests))
failed_names = list(map(lambda x: x["name"], failed_tests))

passed_names = [test["name"] for test in tests if test["status"] == "PASS"]

total_duration = round(reduce(lambda total, test: total + test["duration"], tests, 0), 2)

print("Количество тестов:")
print("PASS: ", statistics["PASS"])
print("FAIL: ", statistics["FAIL"])
print("SKIP: ", statistics["SKIP"])

print(f"Упавшие тесты: {failed_names}")
print(f"Успешные тесты: {passed_names}")
print(f"Общее время выполнения: {total_duration}")
