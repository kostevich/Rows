class Templater():
	def __init__(self) -> None:
		pass
	
	def GetCommands(self, path: str) -> list[str]:
		with open(path) as template:
			lines = template.readlines()
			for line in lines:
				splitline = line.rstrip().split(" ")

		return splitline
	
	def GetTemplateExpressions(self, splitline: list[str]) -> set:
		Data = set()
		for segment in splitline:
			if segment.startswith("{") and segment.endswith("}"): Data.add(segment.replace("{" , "").replace("}" , ""))

		return Data
	