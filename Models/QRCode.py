import enum
import random


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

    @staticmethod
    def RandomQR():
        SixteenABC = 'ABCDEF'
        qrCode = ""
        while len(qrCode) < 5:
            rnd = random.randint(0, 16)
            if rnd > 9:
                rnd = random.choice(SixteenABC)
            qrCode += str(rnd)
        return qrCode

    def __str__(self):
        return "Класс возвращает QR код в любом доступном виде"
