from task_5_with_test.data_file import documents, directories, temp_list, info_text
from pprint import pprint


def prnt(temp_list):
    if temp_list["status"] is None:
        print(info_text)
    pprint(main(temp_list))
    if temp_list["status"] == "exit":
        return
    elif temp_list["status"] == "end":
        temp_list = {"command": None, "mum_doc": None, "doc_unique": None, "type_doc": None, "name": None, "num_shelf": None, "shelf_unique": None, "status": None}
        print()
    prnt(temp_list)

def main(temp_list):
    if temp_list["command"] is None:
        temp_list["command"] = 0
        inp_command(temp_list)

    if temp_list["command"] in ['p', 'people', 's', 'shelf', 'l', 'list']:
        if temp_list["mum_doc"] is None:
            temp_list["mum_doc"] = 0
        if inp_command(temp_list) != "ok": return "Давайте начнем сначала"
        if temp_list["doc_unique"] == "y" or temp_list["doc_unique"] == "yes":
            temp_list["command"] = "a"
            return "Создание нового документа"
        if temp_list["doc_unique"] is not None:
            temp_list["mum_doc"] = temp_list["doc_unique"]
        return search_data(temp_list)

    if temp_list["command"] == 'a' or temp_list["command"] == 'add':
        if temp_list["mum_doc"] == None:
            temp_list["mum_doc"] = 0
        if temp_list["type_doc"] == None:
            temp_list["type_doc"], temp_list["name"], temp_list["num_shelf"] = 0, 0, 0
        if inp_command(temp_list) != "ok":
            temp_list["status"] = "in_process"
            return "Неверный ввод"
        if temp_list["shelf_unique"] == "y" or temp_list["shelf_unique"] == "yes":
            add_shelf(temp_list)
            return add_data(temp_list)
        if temp_list["shelf_unique"] is not None:
            temp_list["num_shelf"] = temp_list["shelf_unique"]
        return add_data(temp_list)

    elif temp_list["command"] == 'd' or temp_list["command"] == 'delete':
        if temp_list["mum_doc"] is None:
            temp_list["mum_doc"] = 0
        if inp_command(temp_list) != "ok": return  "Давайте начнем сначала"
        if temp_list["doc_unique"] == "y" or temp_list["doc_unique"] == "yes":
            temp_list["command"] = "a"
            return "Создание нового документа"
        if temp_list["doc_unique"] is not None:
            temp_list["mum_doc"] = temp_list["doc_unique"]
        return delete_doc(temp_list)

    elif temp_list["command"] == 'm' or temp_list["command"] == 'move':
        if temp_list["mum_doc"] is None:
            temp_list["mum_doc"] = 0
            if inp_command(temp_list) != "ok": return "Попробуйте еще раз"
            temp_list["status"] = "in_process"
            return "Куда переместить документ?"
        if temp_list["num_shelf"] is None:
            temp_list["num_shelf"] = 0
        if inp_command(temp_list) != "ok": return  "Давайте начнем с начала"

        if temp_list["doc_unique"] == "y" or temp_list["doc_unique"] == "yes":
            temp_list["command"] = "a"
            return "Создание нового документа"
        if temp_list["doc_unique"] is not None:
            temp_list["mum_doc"] = temp_list["doc_unique"]

        if temp_list["shelf_unique"] == "y" or temp_list["shelf_unique"] == "yes":
            add_shelf(temp_list)
            return move_shelf(temp_list)
        if temp_list["shelf_unique"] is not None:
            temp_list["num_shelf"] = temp_list["shelf_unique"]
        return move_shelf(temp_list)

    elif temp_list["command"] == 'as' or temp_list["command"] == 'add shelf':
        if temp_list["num_shelf"] is None:
            temp_list["num_shelf"] = 0
        if inp_command(temp_list) != "ok": return "Неверный ввод. Введите числовой номер полки"
        if temp_list["shelf_unique"] == "y" or temp_list["shelf_unique"] == "yes":
            add_shelf(temp_list)
        if temp_list["doc_unique"] == "y" or temp_list["doc_unique"] == "yes":
            temp_list["command"] = "a"
            return "Создание нового документа"
        return add_shelf(temp_list)

    elif temp_list["command"] == 'q' or temp_list["command"] == 'exit':
        temp_list["status"] = "exit"
        return "Работа с программой завершена"

    elif temp_list["command"] == 'bd' or temp_list["command"] == 'print':
        temp_list["status"] = "end"
        return "{}\n{}".format(documents, directories)

    else:
        temp_list["status"] = "end"
        return "Введена неверная команда, попробуйте еще раз"


def inp_command(temp_list):
    if temp_list["command"] == 0:
        temp_list["command"] = input("Введите команду: ")

    if temp_list["mum_doc"] == 0:
        temp_list["mum_doc"] = input("Введите номер документа: ")
        if temp_list["doc_unique"] in ['q','exit', 'n', 'no', 'out']:
            temp_list["status"] = "end"
            return 0

    if temp_list["doc_unique"] == 0:
        temp_list["doc_unique"] = input("Если Вы хотите создать новый, введите \"y\" либо \"yes\": ")
        if temp_list["doc_unique"] in ['q','exit', 'n', 'no', 'out']:
            temp_list["status"] = "end"
            return 0

    if temp_list["type_doc"] == 0:
        temp_list["type_doc"] = input("Введите тип документа:  ")
        if temp_list["type_doc"] <= '9':
            temp_list["type_doc"] = 0
            return 0

    if temp_list["name"] == 0:
        temp_list["name"] = input("Введите Имя и Фамилию: ").title()
        name = temp_list["name"].split()
        if len(name) != 2:
            temp_list["name"] = 0
            return 0
        if name[0] <= '9' or name[1] <= '9':
            temp_list["name"] = 0
            return 0

    try:
        if temp_list["num_shelf"] == 0:
            temp_list["num_shelf"] = int(input("Введите № полки для хранения: "))
            if temp_list["num_shelf"] < 0: temp_list["num_shelf"] *= -1
    except:
        temp_list["status"] = "in_process"
        return 0

    if temp_list["shelf_unique"] == 0:
        temp_list["shelf_unique"] = input('Если Вы хотите создать новую, введите \"y\" либо \"yes\": ')
        if temp_list["shelf_unique"] in ['q','exit', 'n', 'no', 'out']:
            temp_list["status"] = "end"
            return 0

    return "ok"


def search_data(temp_list):
    for data in documents:
        if data["number"] == temp_list["mum_doc"]:
            temp_list["status"] = "end"
            if temp_list["command"] == 'p' or temp_list["command"] == 'people':
                return data["name"]
            if temp_list["command"] == 's' or temp_list["command"] == 'shelf':
                for key, val in directories.items():
                    if data["number"] in val:
                        return f"Номер полки: {key}"
            if temp_list["command"] == 'l' or temp_list["command"] == 'list':
                return f"Данные человека: {list(data.values())}"
    temp_list["doc_unique"] = 0
    temp_list["status"] = "in_process"
    return f'Документ №{temp_list["mum_doc"]} не найден!\n Попробуйте ввести ещё раз '


def add_data(temp_list):
    if temp_list["doc_unique"] == "y" or temp_list["doc_unique"] == "yes":
        try:
            temp_list["status"] = "end"
            directories[str(temp_list["num_shelf"])] += [temp_list["mum_doc"]]
        except:
            temp_list["status"] = "in_progress"
            temp_list["shelf_unique"] = 0
            return f'Полки № {temp_list["num_shelf"]} не существует! Введите полку {list(directories.keys())}'
        documents.append({"type": temp_list["type_doc"], "number": temp_list["mum_doc"], "name": temp_list["name"]})
    else:
        temp_list["status"] = "in_progress"
        for data in documents:
            if data["number"] == temp_list["mum_doc"]:
                temp_list["command"] = "l"
                return f'документ {data["number"]} уже существует!'

        temp_list["doc_unique"] = "y"
        return ''
    return "Документ создан"


def add_shelf(temp_list):
    if temp_list["shelf_unique"] == "y" or temp_list["shelf_unique"] == "yes":
        directories[str(temp_list["num_shelf"])] = []
        if temp_list["command"] == 'as' or temp_list["command"] == 'add shelf':
            temp_list["status"] = "end"
        return f'Полка №{temp_list["num_shelf"]} успешно добавлена.'
    else:
        if str(temp_list["num_shelf"]) in directories:
            temp_list["status"] = "end"
            return f'Полка №{temp_list["num_shelf"]} уже существует.'
        else:
            temp_list["shelf_unique"] = "y"
            temp_list["status"] = "in_process"
            return ""


def move_shelf(temp_list):
    for data in documents:
        if data["number"] == temp_list["mum_doc"]:
            if str(temp_list["num_shelf"]) in directories:
                temp_list["status"] = "end"
                directories[str(temp_list["num_shelf"])] += [temp_list["mum_doc"]]
                for key, val in directories.items():
                    if temp_list["mum_doc"] in val:
                        val.remove(temp_list["mum_doc"])
                        return f'Документ № {temp_list["mum_doc"]} перемещен с полки № {key} на полку № {temp_list["num_shelf"]}'
            else:
                temp_list["status"] = "in_progress"
                temp_list["shelf_unique"] = 0
                return f'Полки № {temp_list["num_shelf"]} не существует? Вы можете переместить документ на полку {list(directories.keys())}'

    temp_list["doc_unique"] = 0
    temp_list["status"] = "in_progress"
    return f'документ №{temp_list["mum_doc"]} не найден!\n Попробуйте ввести ещё раз '


def delete_doc(temp_list):
    for index_data, data in enumerate(documents, 0):
        if data["number"] == temp_list["mum_doc"]:
            temp_list["status"] = "end"
            documents.pop(index_data)
            for key, val in directories.items():
                if temp_list["mum_doc"] in val:
                    del directories[key][val.index(temp_list["mum_doc"])]
                    return "Документ удален"

    temp_list["doc_unique"] = 0
    temp_list["status"] = "in_process"
    return f'Документа № {temp_list["mum_doc"]} не найден!\n Попробуйте ввести ещё раз '




if __name__ == "__main__":
    prnt(temp_list)

#   Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:

# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.


# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;
