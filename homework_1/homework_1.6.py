# Вариант по первому занятию:
school_1 = {
    "1а": 29,
    "1б": 31,
    "1в": 26,
    "2a": 25,
    "2б": 28,
    "3a": 23,
    "3б": 24,
    "4a": 26,
    "4б": 30,
    "4в": 19
}

print(school_1)

# Вариант после второго занятия:
school_2 = {}

for i in range(10):
    class_name = input("Введите название класса: ")
    students_count = int(input("Введите количество учеников: "))

    school_2[class_name] = students_count

print(school_2)