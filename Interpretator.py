from dublib.Terminalyzer import *

class Interpretator():
    def __init__(self) -> None:

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

    def Run(self):
        while True:
            
            CommandLine = input("Rows: ")
            ParsedCommand = Terminalyzer(CommandLine.split(" ")).check_commands(self.__AddCommands())

            if CommandLine != "": self.__HandlerCommandLine(CommandLine)
            else: CommandLine = input("Rows: ")

Interpretator().Run()
