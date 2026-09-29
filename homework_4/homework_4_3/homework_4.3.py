def square_numbers(input_file: str, output_file: str) -> None:
    numbers = []

    with open(input_file, "r") as file:
        for line in file:
            number = float(line)

            numbers.append(number ** 2)

    with open(output_file, "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")


square_numbers("test_files/float_numbers.txt", "result/float_numbers.txt")
