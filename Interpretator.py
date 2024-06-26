from dublib.Terminalyzer import ArgumentsTypes, Command, Terminalyzer, NotEnoughArguments
from dublib.Methods.System import Cls
from Manager import Manager
from Row import Row
from datetime import date
import dateparser
import readline
import shlex

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
		Com.add_key_position(["name", "color"], ArgumentsTypes.All, important = True)
		CommandsList.append(Com)

		Com = Command("add")
		Com.add_argument(ArgumentsTypes.Number, important = True)
		Com.add_key_position(["day"], ArgumentsTypes.All, important = True)
		Com.add_key_position(["value"], ArgumentsTypes.All, important = True)
		CommandsList.append(Com)

		Com = Command("remove")
		Com.add_argument(ArgumentsTypes.Number, important = True)
		Com.add_key_position(["day"], ArgumentsTypes.All, important = True)
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
			row.SetNameColor(key, value)

		if "add" in ParsedCommand.name:
			id = int(ParsedCommand.arguments[0])
			if "day" in ParsedCommand.keys:
				day = ParsedCommand.values["day"]
			value = ParsedCommand.values["value"]
			typevalue = type(value).__name__
			if value.isdigit(): typevalue = "int"
			try:
				row = self.__manager.GetRow(id)
				Date = dateparser.parse(day).date()
				Value = row.GetData(Date)
				if Value:
					row.ReplaceData(typevalue, value, Date)
				else:
					row.SetData(typevalue, value, Date)
			except KeyError:
				print("Такого ряда не существует.")

		if "remove" in ParsedCommand.name:
			id = int(ParsedCommand.arguments[0])
			if "day" in ParsedCommand.keys:
				day = ParsedCommand.values["day"]
				Date = dateparser.parse(day).date()
			try:
				row = self.__manager.GetRow(id)
				row.RemoveData(Date)
			except KeyError:
				print("Такого ряда не существует.")


	def Run(self):
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
			
			except NotEnoughArguments:
				print("Недостаточно аргументов в команде.")