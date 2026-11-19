from pathlib import Path


def total_salary(path):
    try:
        total = 0
        count = 0

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')

                if len(parts) == 2:
                    try:
                        salary = float(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        print(
                            f"Неможливо обробити зарплату у рядку: "
                            f"{line.strip()}"
                        )
                else:
                    print(f"Невірний формат рядка: {line.strip()}")

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return (0, 0)


if __name__ == "__main__":
    path = Path(__file__).parent / "Salary.txt"
    total, average = total_salary(path)

    print(
        f"Загальна сума заробітної плати: {total}, "
        f"Середня заробітна плата: {average}"
    )