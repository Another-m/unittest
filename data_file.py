documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

temp_list = {"command": None, "mum_doc": None, "doc_unique": None, "type_doc": None, "name": None, "num_shelf": None, "shelf_unique": None, "status": None}

info_text = 'Список доступных команд:\n   p(people) - найти человека по номеру документа\n   s(shelf) - узнать номер полки, на которой лежит документ\n   l(list) - вся информация о человеке в виде списка\n   a(add) - добавить новый документ\n   d(delete) - удалить документ\n   m(move) - переместить документ на другую полку \n   as(add shelf) - добавить полку \n   q(exit) - выйти из программы'