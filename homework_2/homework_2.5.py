tests_count = int(input("Введите количество тестов: "))

passed = 0
failed = 0
skipped = 0

for test in range(tests_count):
    status = input("Введите результат теста: ")

    if status.upper() == "PASS":
        passed += 1
    elif status.upper() == "FAIL":
        failed += 1
    elif status.upper() == "SKIP":
        skipped += 1
    else:
        continue

print("PASSED: ", passed)
print("FAILED: ", failed)
print("SKIPPED: ", skipped)

if failed > 0:
    print("Есть упавшие тесты: ", failed)
else:
    print("Все выполненные тесты прошли успешно: ", passed)