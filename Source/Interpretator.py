from dublib.CLI.Terminalyzer import Command, Terminalyzer, NotEnoughParameters, ParametersTypes, ParsedCommandData
from dublib.Methods.System import Cls
from Source.Manager import Manager
from Source.Row import Row
from Graphics.Painter import Painter
import readline
import shlex
import webbrowser

class Interpretator():
	def __init__(self) -> None:

		self.__manager = Manager()
		self.__painter = Painter()
		self.__AddCommands()

	def __AddCommands(self)-> list:

		CommandsList = list()

		Com = Command("exit")
		CommandsList.append(Com)

		Com = Command("clear")
		CommandsList.append(Com)

		Com = Command("createrow")
		CommandsList.append(Com)

		Com = Command("deleterow")
		Com.add_argument(ParametersTypes.Number, important = True)
		CommandsList.append(Com)

		Com = Command("listrows")
		CommandsList.append(Com)

		Com = Command("set")
		Com.add_argument(ParametersTypes.Number, important = True)
		ComPos = Com.create_position(important = True)
		ComPos.add_key("name")
		ComPos.add_key("color")
		CommandsList.append(Com)

		Com = Command("add")
		Com.add_argument(ParametersTypes.Number, important = True)
		Com.add_key("day", ParametersTypes.Date, important = True)
		Com.add_key("value", ParametersTypes.All, important = True)
		CommandsList.append(Com)

		Com = Command("remove")
		Com.add_argument(ParametersTypes.Number, important = True)
		Com.add_key("day", ParametersTypes.Date, important = True)
		CommandsList.append(Com)

		Com = Command("build")
		Com.add_argument(ParametersTypes.Number, important = True)
		Com.add_key("sday", ParametersTypes.Date, important = True)
		Com.add_key("eday", ParametersTypes.Date, important = True)
		CommandsList.append(Com)

		return CommandsList
	
	def __HandlerCommandLine(self, ParsedCommand: ParsedCommandData) -> None:
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
			if "name" in ParsedCommand.keys:
				key = "name"
			else: key = "color"
			id = int(ParsedCommand.arguments[0])
			value = ParsedCommand.keys[key]
			row = self.__manager.GetRow(id)
			row.SetNameColor(key, value)

		if "add" in ParsedCommand.name:
			id = int(ParsedCommand.arguments[0])
			day = ParsedCommand.keys["day"]
			value = ParsedCommand.keys["value"]
			typevalue = type(value).__name__
			if value.isdigit(): typevalue = "int"
			try:
				row = self.__manager.GetRow(id)
				Value = row.GetData(day)
				if Value:
					row.ReplaceData(typevalue, value, day)
				else:
					row.SetData(typevalue, value, day)
			except KeyError:
				print("Такого ряда не существует.")

		if "remove" in ParsedCommand.name:
			id = int(ParsedCommand.arguments[0])
			day = ParsedCommand.keys["day"]
			try:
				row = self.__manager.GetRow(id)
				row.RemoveData(day)
			except KeyError:
				print("Такого ряда не существует.")

		if "build" in ParsedCommand.name:
			id = int(ParsedCommand.arguments[0])
			row = self.__manager.GetRow(id)
			sday = ParsedCommand.keys["sday"]
			eday = ParsedCommand.keys["eday"]
			if self.__painter.DataSChart(row, sday, eday):
				webbrowser.open_new_tab(f'SimpleChart_{id}.html')

	def Run(self) -> None:
		while True:
			CommandLine = input("->")
			CommandLine = CommandLine.strip()
			CommandLine = shlex.split(CommandLine) if len(CommandLine) > 0 else [""]

			try:
				ParsedCommand = Terminalyzer(CommandLine).check_commands(self.__AddCommands())
				if ParsedCommand != None:
					self.__HandlerCommandLine(ParsedCommand)
				else:
					print("Команда не найдена.")

			except FileNotFoundError:
				print("Этот ряд был удалён.")
			
			except NotEnoughParameters:
				print("Недостаточно аргументов в команде.")