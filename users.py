# Твоя задача реализовать четыре функции.
# Одна будет добавлять новый словарь(пользователя) в массив,
# вторая будет удалять словарь(пользователя),
# третья будет изменять уже готовый словарь(данные пользователя),
# четвертая самая простая будет получать массив со словарями(пользователями).
# Пока всё. Порядок произвольный. Как сделаешь, заливаешь на github.

users = [{
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
}, {
    "id": 2,
    "name": "Patricia Lebsack",
    "username": "Karianne",
    "email": "Julianne.OConner@kory.org",
}, {
    "id": 3,
    "name": "Chelsey Dietrich",
    "username": "Kamren",
    "email": "Lucio_Hettinger@annie.ca",
}]

def users_lst(list):
    return list

# duplicate() - checking for duplication/проверка на дублирование
def duplicate(list):
    name = input('Введите логин: ')
    for x in range(len(list)):
        usr = list[x]['username']
        retry = ''
        if name.lower() == usr.lower():
            return print('Такой пользователь уже существует.')
    return name


# add_aser() - adding a new user/добавление нового пользователя
def add_user(list):
    username = duplicate(list)
    if username == None:
        add_user(list)
    else:
        id = int(input('Введите id: '))
        name = input('Введите имя: ')
        email = input('Введите e-mail: ')
        list.append({
            "id": id,
            "name": name,
            "username": username,
            "email": email,
        })
    return list


# del_user() - deleting a user/удаление пользователя
def del_user(list):
    name = input('Введите логин пользователя для удаления: ')
    for i in range(len(list)):
        for x in range(len(list)):
            usr = list[x]['username']
            if name.lower() == usr.lower():
                del list[x]
                return list
            elif name.lower() != usr.lower():
                continue
    else:
        print('Такого пользователя не существует.')
        print('Повторить еще раз?')
        retry = input('Нажмите любую клавишу чтобы повторить, Q - выйти')
        if retry.upper() == 'Q':
            pass
        else:
            del_user(list)
            return list

# edit_user() - changing user data/изменение данных пользователя
def edit_user(list):
    login = input('Введите логин пользователя для изменения: ')
    for i in range(len(list)):
        for x in range(len(list)):
            usr = list[x]['username']
            if login.lower() == usr.lower():
                list[x] = {
                    "id": int(input('Введите id: ')),
                    "name": input('Введите имя: '),
                    "username": input('Введите логин: '),
                    "email": input('Введите e-mail: '),
                }
                return list
            elif login.lower() != usr.lower():
                continue
    else:
        print('Такого пользователя не существует.')
        print('Повторить еще раз?')
        retry = input('Нажмите любую клавишу чтобы повторить, Q - выйти')
        if retry.upper() == 'Q':
            pass
        else:
            edit_user(list)
            return list


print(edit_user(users_lst(users)))
