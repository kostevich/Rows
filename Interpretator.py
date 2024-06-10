from dublib.Terminalyzer import *
from dublib.Methods import Cls
from Manager import *
from Row import *

class Interpretator():
    def __init__(self) -> None:

        self.__manager = Manager()

        self.__AddCommands()

    def __AddCommands(self):

        CommandsList = list()

        Com = Command("exit")
        CommandsList.append(Com)

        Com = Command("clear")
        CommandsList.append(Com)

        Com = Command("createrow")
        CommandsList.append(Com)

        Com = Command("deleterow")
        Com.add_argument(ArgumentsTypes.Number, important = True)
        CommandsList.append(Com)

        Com = Command("listrows")
        CommandsList.append(Com)

        Com = Command("set")
        Com.add_argument(ArgumentsTypes.Number, important = True)
        Com.add_key_position(["name", "color", "owner"], ArgumentsTypes.All)
        CommandsList.append(Com)

        return CommandsList
    
    def __HandlerCommandLine(self, ParsedCommand):
        if "exit" in ParsedCommand.name:
            exit(0)
        
        if "clear" in ParsedCommand.name:
            Cls()

        if "createrow" in ParsedCommand.name:
            self.__manager.CreateRow()
        
        if "deleterow" in ParsedCommand.name:
            self.__manager.DeleteRow(ParsedCommand.arguments[0])

        if "listrows" in ParsedCommand.name:
            AllId = self.__manager.GetRowsID()

            for Id in AllId:
                print(f"{self.__manager.GetRow(Id).ID}. {self.__manager.GetRow(Id).name}")
        
        if "set" in ParsedCommand.name:
            key = ParsedCommand.keys[0]
            id = int(ParsedCommand.arguments[0])
            value = ParsedCommand.values[f"{key}"]
            row = self.__manager.GetRow(id)
            row.SetBaseValue(key, value)

    def Run(self):
        while True:
            
            CommandLine = input("Rows: ")
            ParsedCommand = Terminalyzer(CommandLine.split(" ")).check_commands(self.__AddCommands())

            if ParsedCommand: self.__HandlerCommandLine(ParsedCommand)
            else: print("Команда не найдена.")
