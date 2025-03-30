# Визначення класу Teacher
class Teacher:
    def __init__(self, data):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.email = data["email"]
        self.can_teach_subjects = data["subjects"]
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    selected_teachers = []

    while remaining_subjects:
        best_teacher = None
        best_coverage = set()

        for teacher in teachers:
            coverage = teacher.can_teach_subjects & remaining_subjects
            # Якщо знайдено вчителя, який покриває більше предметів, ніж попередньо
            # обраний вчитель, або якщо пепередній і поточний вчителі покривають
            # однакову кількість предметів - обираємо молодшого
            if len(coverage) > len(best_coverage) or (
                len(coverage) == len(best_coverage)
                and teacher.age < (best_teacher.age if best_teacher else float("inf"))
            ):
                best_teacher = teacher
                best_coverage = coverage

        # Якщо вчителя не знайдено
        if not best_teacher:
            return None  # Неможливо покрити всі предмети

        best_teacher.assigned_subjects = best_coverage
        selected_teachers.append(best_teacher)
        remaining_subjects -= best_coverage

    return selected_teachers


if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}
    # Створення списку викладачів
    teachers = [
        Teacher(
            {
                "first_name": "Олександр",
                "last_name": "Іваненко",
                "age": 45,
                "email": "o.ivanenko@example.com",
                "subjects": {"Математика", "Фізика"},
            }
        ),
        Teacher(
            {
                "first_name": "Марія",
                "last_name": "Петренко",
                "age": 38,
                "email": "m.petrenko@example.com",
                "subjects": {"Хімія"},
            }
        ),
        Teacher(
            {
                "first_name": "Сергій",
                "last_name": "Коваленко",
                "age": 50,
                "email": "s.kovalenko@example.com",
                "subjects": {"Інформатика", "Математика"},
            }
        ),
        Teacher(
            {
                "first_name": "Наталія",
                "last_name": "Шевченко",
                "age": 29,
                "email": "n.shevchenko@example.com",
                "subjects": {"Біологія", "Хімія"},
            }
        ),
        Teacher(
            {
                "first_name": "Дмитро",
                "last_name": "Бондаренко",
                "age": 35,
                "email": "d.bondarenko@example.com",
                "subjects": {"Фізика", "Інформатика"},
            }
        ),
        Teacher(
            {
                "first_name": "Олена",
                "last_name": "Гриценко",
                "age": 42,
                "email": "o.grytsenko@example.com",
                "subjects": {"Біологія"},
            }
        ),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
