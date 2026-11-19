import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)  # Автоматичне скидання кольору після кожного рядка

def print_dir_tree(path: Path, indent: str = ""):
    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}{item.name}/")
            print_dir_tree(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}{item.name}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED} Використання: python task_3.py <шлях_до_директорії>")
        return

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"{Fore.RED} Вказаний шлях не існує: {dir_path}")
        return

    if not dir_path.is_dir():
        print(f"{Fore.RED} Це не директорія: {dir_path}")
        return

    print(f"{Fore.YELLOW} Структура директорії: {dir_path.resolve()}\n")
    print_dir_tree(dir_path)

if __name__ == "__main__":
    main()