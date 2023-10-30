from Models.Settings import *
class Person:
    name = ""
    surname = ""
    __basket = dict()
    __count = 0
    def __init__(self, isAdmin, name="", surname=""):
        self.__status = STATUS_ADMIN if isAdmin else STATUS_USER
        self.name = name
        self.surname = surname

    def GetBasket(self):
        return self.__basket

    def SetBasket(self, dictA):
        self.__basket.update(dictA)
        self.__count  = len(self.__basket)
        return "Товар успешно добавлен!"

    def DeleteBasket(self, keys):
        for key in keys:
            if(key not in self.__basket.keys()):
                return False
            self.__basket.pop(key)
            self.__count = len(self.__basket)
        return True

    def GetStatus(self):
        return self.__status

    def GetCount(self):
        return self.__count

    def GetCountValidate(self):
        if (self.__count >= 5):
            return False
        return True

    def PrintBaskets(self):
        print("Список корзины:")
        i = 0
        for key, value in self.GetBasket().items():
            print(f"{i + 1}) {key} - {value}")
            i += 1



    def __str__(self):
        return f"Status - {self.__status}: Name: {self.name}  Surname: {self.surname}"
