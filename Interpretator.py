
class Interpretator():
    def __init__(self) -> None:
        self.__CommandList = list()
        self.__AddCommands()

    def __HandlerCommandLine(self, CommandLine):
        try:
            if CommandLine in self.__CommandList: self.__HandlerCommands()
        except TypeError as e: print(e)

    def __HandlerCommands(self):
        pass

    def __AddCommands(self):
        self.__CommandList.append("createrow")
        self.__CommandList.append("deleterow")

        return self.__CommandList

    def Run(self):
        while True:
            CommandLine = input()

            if CommandLine != "": self.__HandlerCommandLine(CommandLine)

Interpretator().Run()
