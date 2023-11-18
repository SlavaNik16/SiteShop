import enum


class TypeQR(enum.Enum):
    two = 2,
    eight = 8,
    sixteen = 16,


class QR:

    @staticmethod
    def GetTranslate(text, type: TypeQR):
        try:
            return int(text, type.value[0])
        except ValueError:
            return "Преобразование невозможно!"

    def __str__(self):
        return "Класс возвращает QR код в любом доступном виде"
