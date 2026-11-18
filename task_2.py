def get_cats_info(path):
    cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat = {
                        'id': parts[0],
                        'name': parts[1],
                        'age': parts[2]
                    }
                    cats.append(cat)
                else:
                    print(f" Невірний формат рядка: {line.strip()}")
        return cats

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []

cats_info = get_cats_info(r"D:\Python files\goit-pycore-hw-04\cats.txt")
for cat in cats_info:
    print(cat)