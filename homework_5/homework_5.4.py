class InvalidTestStatusError(Exception):
    pass

def check_test_status(status: str):
    allowed_statuses = {"PASS", "FAIL", "SKIP"}
    if status not in allowed_statuses:
        raise InvalidTestStatusError(
            f"Некорректный статус теста: {status}"
        )

statuses = ["PASS", "FAIL", "SKIP", "ERROR"]

for status in statuses:
    try:
        check_test_status(status)
        print(f"Статус {status} корректен")

    except InvalidTestStatusError as e:
        print(f"Ошибка: {e}")