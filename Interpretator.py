
class Interpretator():
    def __init__(self) -> None:

        self.__CommandList = list()
        self.__AddCommands()

    def __HandlerCommandLine(self, CommandLine):
        
        if CommandLine in self.__CommandList: self.__HandlerCommands()
        else: print("Command not found")

    def __HandlerCommands(self):
        print("Processing the command")

    def __AddCommands(self):
        self.__CommandList.append("createrow")
        self.__CommandList.append("deleterow")

        return self.__CommandList

    def Run(self):
        while True:
            CommandLine = input("Rows: ")

            if CommandLine != "": self.__HandlerCommandLine(CommandLine)
            else: CommandLine = input("Rows: ")

Interpretator().Run()
