from dublib.Terminalyzer import *
from Manager import *
from Row import *

class Interpretator():
    def __init__(self) -> None:

        self.__manager = Manager()

        self.__AddCommands()

    def __AddCommands(self):

        CommandsList = list()

        Com = Command("createrow")
        CommandsList.append(Com)

        Com = Command("deleterow")
        Com.add_argument(ArgumentsTypes.Number, important = True)
        CommandsList.append(Com)

        Com = Command("listrows")
        CommandsList.append(Com)

        return CommandsList
    
    def __HandlerCommandLine(self, ParsedCommand):
        if "createrow" in ParsedCommand.name:
            self.__manager.CreateRow()
        
        if "deleterow" in ParsedCommand.name:
            self.__manager.DeleteRow(ParsedCommand.arguments[0])

        if "listrows" in ParsedCommand.name:
            AllId = self.__manager.GetRowsID()

            for Id in AllId:
                print(f"Название ряда: {self.__manager.GetRow(Id).name} — ID ряда: {self.__manager.GetRow(Id).ID}")

    def Run(self):
        while True:
            
            CommandLine = input("Rows: ")
            ParsedCommand = Terminalyzer(CommandLine.split(" ")).check_commands(self.__AddCommands())
            print(ParsedCommand)

            if ParsedCommand: self.__HandlerCommandLine(ParsedCommand)
            else: print("Команда не найдена.")

Interpretator().Run()
