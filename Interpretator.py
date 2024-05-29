from dublib.Terminalyzer import *

class Interpretator():
    def __init__(self) -> None:

        self.__CommandsList = list()
        self.__AddCommands()

    def __HandlerCommandLine(self, CommandLine):
        
        if CommandLine in self.__CommandsList: self.__HandlerCommands()
        else: print("Command not found")

    def __HandlerCommands(self):
        
        print("Processing the command")

    def __AddCommands(self):

        Com = Command("createrow")
        self.__CommandsList.append(Com)

        Com = Command("deleterow")
        Com.add_argument(ArgumentsTypes.Number, important = True)
        self.__CommandsList.append(Com)

        Com = Command("listrows")
        self.__CommandsList.append(Com)

        return self.__CommandsList

    def Run(self):
        while True:
            CommandLine = input("Rows: ")
            
            if CommandLine != "": self.__HandlerCommandLine(CommandLine)
            else: CommandLine = input("Rows: ")

Interpretator().Run()
