def count_pass(results: list[str], index: int = 0) -> int:
    if index == len(results):
        return 0

    if results[index] == "PASS":
        return 1 + count_pass(results, index + 1)

    return count_pass(results, index + 1)


results = ["PASS", "FAIL", "PASS", "SKIP", "PASS", "FAIL"]

pass_count = count_pass(results)

print("Количество PASS:", pass_count)
