import json


main_menu = ("1. Копирование строк из одного файла в другой\n ",
             "2. Цветы\n ",
             "3. Университет\n ",
             "4. Фирмы\n ",
             "0. Выход")


def task1():
    # Создать программный файл F1 в текстовом формате, записать в него
    # построчно данные, вводимые пользователем. Об окончании ввода данных
    # будет свидетельствовать пустая строка. Скопировать из файла F1 в файл F2
    # все строки, в которых нет слов, совпадающих с первым словом. Определить
    # количество согласных букв в первой строке файла F2.
    english_consonants = ('q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b',
                          'n', 'm')
    russian_consonants = ('й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'в', 'п', 'р', 'л', 'д', 'ж', 'ч',
                          'с', 'м', 'т', 'ь', 'б')
    with open("file_1.txt", "w+") as file_1, open("file_2.txt", "w+") as file_2:
        try:
            flag = False
            while True:
                input_string = input("Введите данные: ")
                for symbol in input_string:
                    if symbol.isdigit():
                        print("Введите слова!")
                        flag = True
                        break
                if flag is True:
                    flag = False
                    continue
                if input_string == '':
                    break
                file_1.write(input_string + "\n")
            file_1.seek(0)
            for line in file_1.readlines():
                is_exist = False
                input_string = "".join(sym.lower() for sym in line if sym.isalpha() or sym.isspace()).split()
                first_word = input_string[0]
                for i in range(len(input_string)-1):
                    if first_word == input_string[i+1]:
                        is_exist = True
                        break
                if is_exist is False:
                    file_2.write(line)
            file_2.seek(0)
            print("Содержание 2 файла:\n", file_2.read(), sep='')
            file_2.seek(0)
            line = file_2.readline()
            counter = 0
            for letter in line:
                if letter.lower() in english_consonants or letter.lower() in russian_consonants:
                    counter += 1
            print("Количество согласных в первой строке:", counter)
        except IOError:
            print("Ошибка в вводе-выводе!")


def task2():
    # Создать текстовый файл (не программно). Построчно записать
    # названия цветов и их стоимость (не менее 10 строк). Вывести на экран все
    # цветы дороже 5 рублей. Найти среднюю стоимость всех цветов. Вывести на
    # экран все цветы с минимальной стоимостью.
    # Пример файла:
    # Роза 12
    # Гвоздика 5
    with open("flowers.txt", "r", encoding="utf-8") as flowers:
        try:
            flowers_dict = {}
            try:
                for line in flowers.readlines():
                    split_line = line.split()
                    flowers_dict.update({split_line[0]: int(split_line[1])})
            except ValueError:
                print("Ошибка преобразования! Проверьте правильность заполнения файла!")
            except IndexError:
                print("Ошибка импорта данных из файла! Проверьте правильность заполнения файла!")
            print("Все цветы:", flowers_dict, sep="\n")
            print("Цветы дороже 5 рублей:", sep="")
            average_price = quantity = min_price = 0
            first_price = True
            for name, price in flowers_dict.items():
                if price > 5:
                    print(name, "->", price, "руб.")
                average_price += price
                quantity += 1
                if first_price is False:
                    if price < min_price:
                        min_price = price
                else:
                    first_price = False
                    min_price = price
            print("Цветы с минимальной стоимостью:", sep="")
            for name, price in flowers_dict.items():
                if price == min_price:
                    print(name, "->", price, "руб.")
            print("Средняя стоимость цветов:", round(average_price/quantity, 2), "руб.")
        except IOError:
            print("Ошибка в вводе-выводе!")


def task3():
    # Сформировать (не программно) текстовый файл. В нём каждая
    # строка должна описывать учебный предмет и наличие лекционных,
    # практических и лабораторных занятий по предмету. Сюда должно входить и
    # количество занятий. Необязательно, чтобы для каждого предмета были все
    # типы занятий.
    # Сформировать словарь, содержащий название предмета и общее
    # количество занятий по нему. Вывести его на экран.
    # Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
    #  Физика: 30(л) 10(лаб)
    #  Физкультура: 30(пр)
    # Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”:
    # 30}
    with open("university.txt", "r", encoding="utf-8") as studies:
        try:
            studies_dict = {}
            try:
                for line in studies.readlines():
                    split_line_to_lessons = line.split(sep=":")
                    digits = ""
                    hours = 0
                    flag_is_digit = False
                    for symbol in split_line_to_lessons[1]:
                        if symbol.isdigit():
                            digits += symbol
                            flag_is_digit = True
                        elif flag_is_digit is True:
                            hours += (int(digits))
                            digits = ""
                            flag_is_digit = False
                    studies_dict.update({split_line_to_lessons[0]: hours})
            except ValueError:
                print("Ошибка преобразования! Проверьте правильность заполнения файла!")
            except IndexError:
                print("Ошибка импорта данных из файла! Проверьте правильность заполнения файла!")
            print("Все предметы:", studies_dict, sep="\n")
        except IOError:
            print("Ошибка в вводе-выводе!")


def task4():
    # Создать вручную и заполнить несколькими строками текстовый
    # файл, в котором каждая строка будет содержать данные о фирме: название,
    # форма собственности, выручка, издержки.
    # Пример строки файла: firm_1 ООО 10000 5000.
    # Необходимо построчно прочитать файл, вычислить прибыль каждой
    # компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт
    # средней прибыли её не включать.
    # Далее реализовать список. Он должен содержать словарь с фирмами и
    # их прибылями, а также словарь со средней прибылью. Если фирма получила
    # убытки, также добавить её в словарь (со значением убытков).
    # Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
    # {“average_profit”: 2000}].
    # Итоговый список сохранить в виде json-объекта в соответствующий
    # файл.
    # Пример json-объекта:
    # [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit":
    # 2000}]
    # Подсказка: использовать менеджер контекста.
    companies_list = []
    with open("companies.txt", "r", encoding="utf-8") as companies:
        try:
            companies_dict = {}
            profit_dict = {}
            try:
                average_profit = counter = 0
                for line in companies.readlines():
                    split_line = line.split()
                    revenue = int(split_line[2])
                    losses = int(split_line[3])
                    profit = revenue - losses
                    companies_dict.update({split_line[0]: profit})
                    if profit > 0:
                        average_profit += profit
                    counter += 1
                average_profit /= counter
                profit_dict.update({"average_profit": average_profit})
                companies_list = [companies_dict, profit_dict]
                print(companies_list)
            except ValueError:
                print("Ошибка преобразования! Проверьте правильность заполнения файла!")
            except IndexError:
                print("Ошибка импорта данных из файла! Проверьте правильность заполнения файла!")
        except IOError:
            print("Ошибка в вводе-выводе!")
    with open("companies.json", "w", encoding="utf-8") as companies_json:
        json.dump(companies_list, companies_json, ensure_ascii=False)


def menu():
    while True:
        print("Список заданий:\n", "".join(main_menu))
        variant = input("Выберите задание: ")
        try:
            variant = int(variant)
        except ValueError:
            print("Введите целочисленное число!")
            continue
        if variant > len(main_menu) - 1 or variant < 0:
            print("Ошибка, введите число в заданном интервале!")
        else:
            match variant:
                case 1:
                    task1()
                case 2:
                    task2()
                case 3:
                    task3()
                case 4:
                    task4()
                case 0:
                    break
                case _:
                    print("Ошибка!")
                    return -1
    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    menu()

