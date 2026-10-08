from functools import wraps


def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Запуск теста: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Тест завершён: {func.__name__}")
        print(f"Результат: {result}")

        return result

    return wrapper


@log_test
def test_login(username, password):
    return username == "alex" and password == "Python123"


test_login("alex", password="Python123")
