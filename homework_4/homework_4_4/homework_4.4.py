def swap_files(file_1: str, file_2: str, result_file_1: str, result_file_2: str) -> None:
    with open(file_1, "rb") as first_file:
        first_content = first_file.read()

    with open(file_2, "rb") as second_file:
        second_content = second_file.read()

    with open(result_file_1, "wb") as first_file:
        first_file.write(second_content)

    with open(result_file_2, "wb") as second_file:
        second_file.write(first_content)


swap_files("test_files/first.bin", "test_files/second.bin", "result/first.bin", "result/second.bin")
