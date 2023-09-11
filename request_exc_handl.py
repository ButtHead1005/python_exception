
def count_lin_in_file():
    try:
        target_path = input('Укажите путь к файлу текущей директории: ')
        target_file = open(target_path, 'r')
        print(len(target_file.readlines()))
    except FileNotFoundError:
        print('Файл не найден. Укажите корректный путь')
        count_lin_in_file()

count_lin_in_file()