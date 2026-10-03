import json
from functools import reduce


def load_tests(filename: str) -> list[dict]:
    with open(filename, "r", encoding="utf-8") as file:
        tests = json.load(file)

    if not isinstance(tests, list):
        raise ValueError("Ожидался список тестов")

    if not tests:
        raise ValueError("Файл не содержит тестов")

    required_fields = ["name", "status", "duration"]

    allowed_statuses = ["PASS", "FAIL", "SKIP"]

    for test in tests:
        if not isinstance(test, dict):
            raise ValueError("Каждый тест должен быть объектом")

        for field in required_fields:
            if field not in test:
                raise ValueError(f"Отсутствует обязательное поле: {field}")

        if test["status"] not in allowed_statuses:
            raise ValueError(f"Некорректный статус: {test['status']}")

        if not isinstance(test["duration"], (int, float)):
            raise ValueError(f"Некорректное время выполнения: {test['duration']}")

        if test["duration"] < 0:
            raise ValueError("Время выполнения не может быть отрицательным")

    return tests


def create_report(tests: list[dict]) -> dict:
    statistics = {
        "PASS": len([test for test in tests if test["status"] == "PASS"]),
        "FAIL": len([test for test in tests if test["status"] == "FAIL"]),
        "SKIP": len([test for test in tests if test["status"] == "SKIP"])
    }

    failed_tests = list(map(lambda test: test["name"], filter(lambda test: test["status"] == "FAIL", tests)))

    longest_test = max(tests, key=lambda test: test["duration"])

    total_time = round(reduce(lambda total, test: total + test["duration"], tests, 0), 2)

    return {
        "total_tests": len(tests),
        "statistics": statistics,
        "failed_tests": failed_tests,
        "longest_test":
            {
                "name": longest_test["name"],
                "duration": longest_test["duration"]
            },
        "total_time": total_time}


try:
    tests = load_tests("test_results.json")
    report = create_report(tests)

    with open("result/test_report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=4)

    print("Отчёт сохранён в result/test_report.json")

except FileNotFoundError as e:
    print(f"Ошибка: файл не найден — {e}")

except json.JSONDecodeError as e:
    print(f"Ошибка: файл содержит некорректный JSON — {e}")

except ValueError as e:
    print(f"Ошибка в структуре тестовых данных: {e}")
