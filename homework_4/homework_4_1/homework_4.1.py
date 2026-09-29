def read_numbers(filename: str) -> list[int]:
    numbers = []

    with open(filename, "r") as file:
        for line in file:
            numbers.append(int(line))

    return numbers


numbers = read_numbers("test_files/numbers.txt")

if len(numbers) < 3:
    print("Ошибка: в файле меньше 3 чисел")
else:
    print("Первый элемент:", numbers[0])
    print("Второй элемент:", numbers[1])
    print("Предпоследний элемент:", numbers[-2])
    print("Последний элемент:", numbers[-1])
