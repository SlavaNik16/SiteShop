
class Language:
    __language = dict(
                    zip(
                        map(
                            ord,
                            "qwertyuiop[]asdfghjkl;'zxcvbnm,./`" 
                            'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'
                            ),
                            "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                            'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'
                        )
                    )
    __english = list()
    def __init__(self):
        for i in range(65, 91):
            self.__english.append(chr(i))

    def GetLanguage(self, text:str):
        result = ""
        for simvol in text:
            if simvol.upper() in self.__english:
                result += simvol.translate(self.__language)
                continue
            result += simvol
        return result
