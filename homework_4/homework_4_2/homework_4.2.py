def read_numbers(filename: str) -> list[int]:
    numbers = []

    with open(filename, "r") as file:
        for line in file:
            numbers.append(int(line))

    return numbers


def write_numbers(filename: str, numbers: list[int]) -> None:
    with open(filename, "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")


def split_numbers(filename: str) -> None:
    numbers = read_numbers(filename)

    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)

        else:
            odd_numbers.append(number)

    write_numbers("result/even.txt", even_numbers)
    write_numbers("result/odd.txt", odd_numbers)


split_numbers("test_files/numbers.txt")
