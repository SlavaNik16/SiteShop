from Models.Settings import *
from Models.Person import *
from Models.Tovar import *
import sys

users = {
    "user_123": Person(False, "Алексей"),
    "u_777": Person(False, "Влад", "Владимир"),
    "a_a": Person(True),
    "a_pas": Person(True, surname="Иванов")
}

def Site(user):
    tovars = Tovar()
    if user.GetStatus() == STATUS_USER:
        SiteUser(tovars, user)
    else:
        SiteAdmin(tovars, user)

def SiteUserViewTovars(tovars, user):
    tovars.PrintTovars()
    if (user.GetCountValidate()):
        print(f"\nХотите что-нибудь купить? Выберите до 5 индивидуальных товаров включительно"
          f"(Кол-во : {user.GetCount()}) или пропишите n - Для выхода: ")
    else:
        print("\nВы уже выбрали максимальное число покупок! Зайдите в корзину и удалите некоторые покупки!")
    while (user.GetCountValidate()):
        try:
            answer = input("Ваш номер: ")
            if answer == "n":
                break
            num = int(answer)
            tovarName = tovars.GetTovarNameById(num - 1)
            if (tovarName):
                user.SetBasket(tovars.GetTovarByKey(tovarName))
                print(f"\nВаш товар занесен в корзину! Кол-во {user.GetCount()}\n")
            else:
                print("Товар не найден! Повторите попытку!")
        except ValueError:
            print("Такого номера не существует! \n")
            tovars.PrintTovars()

def SiteUserViewBaskets(tovars, user):
    while (user.GetCount() != 0):
        print(f"Кол-во покупок: {user.GetCount()}/5")
        print(f"Полная цена: {sum(user.GetBasket().values())}")
        user.PrintBaskets()
        try:
            answer = input("\nВведите номер продукта, который вы хотите удалить или n - Для выхода: ")
            if answer == "n":
                break
            num = int(answer)
            tovarName = tovars.GetTovarNameById(num - 1)
            if (tovarName):
                if (user.DeleteBasket(tovars.GetTovarByKey(tovarName).keys())):
                    print(f"\nВаш товар удален из корзины!\n")
                else:
                    print("Произошла непредвиденная ошибка: Вашего товара нет в корзине!")
            else:
                print("Товар не найден! Повторите попытку!")
        except ValueError:
            print("Такого номера не существует! \n")
    if user.GetCount() == 0:
        print("Корзина пуста!")

def SiteUser(tovars, user):
    while True:
        print(
            "\nВам доступны такие действия:\n\t1) Просмотреть товары\n\t2) Просмотреть корзину\n\tВыйти из аккаунта - нажать любую кнопку")
        answer = input("Ваш выбор:")
        print()
        match answer:
            case "1":
                SiteUserViewTovars(tovars, user)
            case "2":
                SiteUserViewBaskets(tovars, user)
            case _:
                break

def SiteAdminViewUsers():
    print("\nВсе пользователи: ")
    i = 0
    listUser = list()
    for key, value in users.items():
        if (value.GetStatus() == STATUS_USER):
            listUser.append(key)
            print(f"\t{i + 1})Привет {value.name} {value.surname}")
            i += 1
    return listUser

def SiteAdminRemoveUsers():
    usersListKey = SiteAdminViewUsers()
    while True:
        answer = input("Выберите номер блокировки пользователя или n - для выхода назад: ")
        if answer == "n":
            break
        try:
            num = int(answer)
            if ((num - 1) > -1 and (num - 1) < len(usersListKey)):
                userKey = usersListKey[num - 1]
                print(f"\nПользователь: {users.pop(userKey)} - удален!\n")
            else:
                print("Не найден пользователь")
        except Exception:
            print("Неверный формат!")

def SiteAdminAddTovars(tovars, user):
    tovars.PrintTovars()
    print()
    nameTovars = input("Введите название товара: ")
    try:
        price = float(input("Введите цену товара: "))
        if (tovars.AddTovars(user.GetStatus(), nameTovars, price)):
            print("Товар успешно добавлен")
        else:
            print("Товар не добавлен!!! Недостаточно прав!")
    except ValueError:
        print("Данные введены неверно!")

def SiteAdminDeleteTovars(tovars, user):
    tovars.PrintTovars()
    print()
    while True:
        answer = input("Введите номер товара, которого вы хотите удалить или n - для выхода: ")
        if (answer == "n"):
            break
        try:
            num = int(answer)
            nameTovar = tovars.GetTovarNameById(num - 1)
            if (tovars.DeleteTovars(user.GetStatus(), nameTovar)):
                print("Товар успешно удален")
            else:
                print("Товар не удален!!! Недостаточно прав!")
        except ValueError:
            print("Данные введены неверно!")
def SiteAdmin(tovars, user):
    while True:
        print(
            "Вам доступны такие действия:\n\t1) Просмотреть всех пользователей \n\t2) Удалить пользователя \n\t3) Просмотреть товары \n\t4) Добавить товары \n\t5) Удалить товары\n\tВыйти из аккаунта - нажать любую кнопку");
        answer = input("Ваш выбор:")
        match answer:
            case "1":
                SiteAdminViewUsers()
            case "2":
                SiteAdminRemoveUsers()
            case "3":
                tovars.PrintTovars()
            case "4":
                SiteAdminAddTovars(tovars, user)
            case "5":
                SiteAdminDeleteTovars(tovars, user)
            case _:
                break

def EnterSite(users):
    print("Введите данные для входа в аккаунт!")
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    str = f"{login}_{password}"
    if str in users:
        user = users[str]
        print(f"\nПользователь найден!\n\tИмя: {user.name}\n\tФамилия: {user.surname}\n\tСтатус: {user.GetStatus()}")
        Site(user)
    else:
        print("\nПользователь не найден! Повторите попытку снова или зарегистрируйтесь!\n")

def RegisterSite():
    print("Заполните ваши данные(те которые отмечены звездочками обязательные): \n")
    name = input("Введите ваше Имя: ")
    surname = input("Введите вашу Фамилию: ")
    login = input("Введите ваш *Логин: ")
    password = input("Введите ваш *Пароль: ")
    if (login == "" or password == ""):
        print("Неверно введены данные!")
        return
    str = f"{login}_{password}"
    if (str in users.keys()):
        print("Пользователь уже создан!")
        return
    users[str] = Person(False, name, surname)
    print("\nПользователь успешно зарегистрирован!\n")

def main():
    while True:
        print(
            "Добро пожаловать на сайт Собери ПК. Выберите одно из двух действий:\n\t1) Войти \n\t2) Зарегистрироватся\n\tВыйти - введите любую букву\n")
        answer = input("Ваш выбор: ")
        print()
        match answer:
            case "1":
                EnterSite(users)
            case "2":
                RegisterSite()
            case _:
                sys.exit(0)

if __name__ == '__main__':
    main()