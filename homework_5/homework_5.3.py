def validate_test_retries(retries: int, timeout: float) -> None:
    if retries < 0 or retries > 5:
        raise ValueError(
            "Количество запусков должно быть от 0 до 5"
        )
    if timeout <= 0:
        raise ValueError(
            "Таймаут должен быть больше нуля"
        )

test_cases = [
    ("Тест: Корректные значения", 3, 40),
    ("Тест: Отрицательный таймаут", 2, -5),
    ("Тест: Слишком много повторных запусков", 6, 10)
]

for name, retries, timeout in test_cases:
    print(name)
    try:
        validate_test_retries(retries, timeout)
        print("Настройки корректы")

    except ValueError as e:
        print(f"Ошибка: {e}")

    print("-------------------------")