def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    cat_id, name, age = line.split(',')
                    cat_info = {"id": cat_id, "name": name, "age": age}
                    cats_info.append(cat_info)
        return cats_info
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
