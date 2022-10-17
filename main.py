def get_n():
    n = input('Введите номер телефона')
    n = n.replace("", "").replace("-", "")

    if (n[0] == "8") and (len(n) == 11):
        n = n.replace("8", "+7" , 1 )
    if (n[0] == "7") and (len(n) == 11):
        n =  "+" + n
    if (n[0] == "9") and (len(n) == 10):
        n = "+7" + n
    if  (len(n) == 12) and (n[1:].isdigit()):
        return(n)

    else:
        print("Неправильно набран номер")
        return get_n()


def get_name():
    name = input("Введите название контакта")
    name = name.title()
    return name


def get_con(dict, names, n):
    dict[names] = n
    print("Контакт добавлен")
    return dict

def remove_con(dict, names):
    if not(names in dict ):
        print("Номер не найден")
        return False
    del dict[names]
    return dict

def show_dict(dict):
    print("Список контактов")
    for i in dict:
        print(i, dict[i])

def change_n(dict, names):
    if not(names in dict):
        print("Номера нет ")
        return False
    dict[names]= get_n()
    print("Контакт успешно изменен")
    return(dict)

def menu():
    print("\n\nВыберите функцию:\n\n1. Добавь контакт:\n2. Удалить контакт:\n3. Изменить контакт:")

i = 0
dict = {}
while True:
    menu()
    i = int(input("Введите номер "))
    if i == 1:
        get_con(dict, get_name() , get_n())
    if i == 2:
        remove_con(dict, get_name())
    if i == 3:
        show_dict(dict)
    if i == 4:
        change_n(dict, get_name())
    if i == 5:
        print('Спасибо за использование!')
        break