import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізуємо colorama для кросплатформеного використання кольорів
init(autoreset=True)

def print_directory_structure(path, indent=0):
    try:
        for item in path.iterdir():
            # Відступ для візуального представлення рівня вкладеності
            spacer = ' ' * 4 * indent
            if item.is_dir():
                # Виведення піддиректорії зеленим кольором
                print(f"{spacer}{Fore.GREEN}📂 {item.name}")
                print_directory_structure(item, indent + 1)
            else:
                # Виведення файлів синім кольором
                print(f"{spacer}{Fore.CYAN}📜 {item.name}")
    except PermissionError:
        print(f"{Fore.RED}Доступ до {path} заборонено.")
    except Exception as e:
        print(f"{Fore.RED}Помилка: {e}")

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії як аргумент.")
        return

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + "Вказаний шлях не існує.")
        return
    if not dir_path.is_dir():
        print(Fore.RED + "Вказаний шлях не веде до директорії.")
        return

    print(f"{Fore.YELLOW}Структура директорії {dir_path}:\n")
    print_directory_structure(dir_path)

if __name__ == "__main__":
    main()
