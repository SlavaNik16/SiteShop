class Language():
    def GetLang(self):
        layout = dict(
            zip(
                map(
                    ord,
                    "qwertyuiop[]asdfghjkl;'zxcvbnm,./`" 'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'),
                     "йцукенгшщзхъфывапролджэячсмитьбю.ё"'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))
        lista= layout
        print("Dctv Ghbdtn".translate(lista))
