class MixinInfo:

    def __init__(self, *args):
        super().__init__(*args)
        print(self.__repr__())
