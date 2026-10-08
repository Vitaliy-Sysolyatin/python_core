def create_time_checker(max_time: float):
    def check_time(actual_time: float):
        if actual_time > max_time:
            print(f"Время {actual_time} сек. превышает "
                  f"лимит {max_time} сек.")
        else:
            print(f"Время {actual_time} сек. не превышает "
                  f"лимит {max_time} сек.")

    return check_time


first_test_checker = create_time_checker(2)
second_test_checker = create_time_checker(5)

first_test_checker(1.5)
first_test_checker(3)

second_test_checker(0.3)
second_test_checker(6)
