# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з ліва записувати не потрібно)
import re

input_file = "вихідний_файл.txt"
output_file = "новий_файл.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

gmail_emails = []
for line in lines:
    match = re.search(r"\b[A-Za-z0-9._%+-]+@gmail.com\b", line)
    if match:
        gmail_emails.append(match.group())

with open(output_file, "w") as file:
    file.write("\n".join(gmail_emails))

    # 2) Створити записну книжку покупок:
    # - у покупки повинна бути id, назва і ціна
    #                                      - всі покупки зберігаємо в файлі
    # з функціоналу:
    # * вивід всіх покупок
    #              * має бути змога додавати покупку в книгу
    #                                                  * має бути змога шукати по будь якому полю покупку
    #                                                                                             * має бути змога показати найдорожчу покупку
    #                                                                                                                                  * має бути можливість видаляти покупку по id
    # (ну і меню на це все)
import json

def load_shopping_list():
    try:
        with open("shopping_list.json", "r") as file:
            shopping_list = json.load(file)
        return shopping_list
    except FileNotFoundError:
        return []

def save_shopping_list(shopping_list):
    with open("shopping_list.json", "w") as file:
        json.dump(shopping_list, file)

def display_shopping_list():
    shopping_list = load_shopping_list()
    if len(shopping_list) == 0:
        print("Записна книжка покупок порожня.")
    else:
        print("Записна книжка покупок:")
        for item in shopping_list:
            print(f"ID: {item['id']}, Назва: {item['назва']}, Ціна: {item['ціна']}")

def add_shopping_item():
    shopping_list = load_shopping_list()
    id = input("Введіть ID покупки: ")
    назва = input("Введіть назву покупки: ")
    ціна = float(input("Введіть ціну покупки: "))
    item = {
        "id": id,
        "назва": назва,
        "ціна": ціна
    }
    shopping_list.append(item)
    save_shopping_list(shopping_list)
    print("Покупку додано до записної книжки.")

def search_shopping_item():
    shopping_list = load_shopping_list()
    field = input("Введіть поле для пошуку (id, назва, ціна): ")
    value = input("Введіть значення для пошуку: ")
    found_items = []
    for item in shopping_list:
        if str(item[field]) == value:
            found_items.append(item)
    if len(found_items) == 0:
        print("Покупки не знайдено.")
    else:
        print("Результати пошуку:")
        for item in found_items:
            print(f"ID: {item['id']}, Назва: {item['назва']}, Ціна: {item['ціна']}")

def find_most_expensive_item():
    shopping_list = load_shopping_list()
    if len(shopping_list) == 0:
        print("Записна книжка покупок порожня.")
    else:
        most_expensive_item = max(shopping_list, key=lambda item: item["ціна"])
        print("Найдорожча покупка:")
        print(f"ID: {most_expensive_item['id']}, Назва: {most_expensive_item['назва']}, Ціна: {most_expensive_item['ціна']}")

def delete_shopping_item():
    shopping_list = load_shopping_list()
    id = input("Введіть ID покупки для видалення: ")
    found_item = None
    for item in shopping_list:
        if item["id"] == id:
            found_item = item
            break
    if found_item:
        shopping_list.remove(found_item)
        save_shopping_list(shopping_list)
        print("Покупку видалено з записної книжки.")
    else:
        print("Покупку з таким ID не знайдено.")

def main_menu():
    while True:
        print("Меню:")
        print("1. Вивести всі покупки")
        print("2. Додати покупку")
        print("3. Пошук покупки")
        print("4. Показати найдорожчу покупку")
        print("5. Видалити покупку")
        print("6. Вийти")
        choice = input("Виберіть опцію: ")
        if choice == "1":
            display_shopping_list()
        elif choice == "2":
            add_shopping_item()
        elif choice == "3":
            search_shopping_item()
        elif choice == "4":
            find_most_expensive_item()
        elif choice == "5":
            delete_shopping_item()
        elif choice == "6":
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()



# *********Кому буде замало ось завдання з співбесіди
# Є ось такий список:
# data = [
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1111, "field": {}},
#         {"id": 1112, "field": {}},
#         {"id": 1113, "field": {}},
#         {"id": 1114, "field": {}},
#         {"id": 1115, "field": {}},
#     ],
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1120, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1123, "field": {}},
#         {"id": 1124, "field": {}},
#         {"id": 1125, "field": {}},
#
#     ],
#     [
#         {"id": 1130, "field": {}},
#         {"id": 1131, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1132, "field": {}},
#         {"id": 1133, "field": {}},
#
#     ]
# ]
#
# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122, .......]

data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},
    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},
    ]
]

res = []
found = True
while found:
    found = False
    for sublist in data:
        if sublist:
            item = sublist.pop(0)
            if item["id"] not in res:
                res.append(item["id"])
                found = True

print(res)