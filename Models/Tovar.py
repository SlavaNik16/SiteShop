class Tovar:
    __tovars = {
        "Видеокарта": 23432,
        "Материнская плата": 7423,
        "Блок питания": 292,
        "Монитор": 34193,
        "Клавиатура": 6812,
        "Мышь": 2250
    }
    def GetTovars(self):
        return self.__tovars

    def GetTovarNameById(self, index):
        if(index >= 0 and index < len(self.__tovars)):
            return list(self.__tovars.keys())[index]
        return False#"Нет такого продукта"

    def GetTovarByKey(self, key):
        if (key in self.__tovars.keys()):
            return dict({(key, self.__tovars[key])})
        return False #"Неправильный ключ"

    def PrintTovars(self):
        print("Список товаров:")
        i = 0
        for key, value in self.GetTovars().items():
            print(f"{i + 1}) {key} - {value}")
            i+=1
        if i == 0:
            print("Товаров нет в наличие!")

    def __str__(self):
        print("Список товаров и их цен: ")
        for key, value in self.__tovars.items():
            print(f"{key} - {value}")
        return ""
