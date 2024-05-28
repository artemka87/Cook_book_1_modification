def great_my_book(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        name_text = file.read().split('\n\n')
        for text in name_text:
            list1 = []
            name, num, *args = text.split('\n')
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split('|'))
                list1.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})
            cook_book[name] = list1
    return cook_book


def get_shop_list_by_dishes(person_count: int, dishes: list, cook_book):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],
                                                          'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)


book = great_my_book('book.txt')
print(book, '\n')
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'], book)
