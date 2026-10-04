from functools import wraps


def retry(count: int):
    if count < 1:
        raise ValueError("Количество попыток должно быть больше 0")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, count + 1):
                print(f"Попытка {attempt}")

                result = func(*args, **kwargs)

                if result is True:
                    return result

            return result

        return wrapper

    return decorator


test_results = [False, False, True]


@retry(3)
def check_status(service, expected_status="OK"):
    print(f"Проверка сервиса: {service}, "
          f"ожидаемый статус: {expected_status}")

    return test_results.pop(0)


result = check_status("auth", expected_status="OK")

print("Результат:", result)
