import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Display:
	def PassBig(self):
		"""Prints white " ✔  " on a green BackGround"""
		print(f"{Back.GREEN}{Fore.WHITE} ✔  ")
	def PassSmall(self):
		"""Prints green "✔" sign"""
		print(f"{Fore.GREEN}✔")
	def FailBig(self):
		"""Prints white " ✘  " on a red BackGround"""
		print(f"{Back.RED}{Fore.WHITE} ✘  ")
	def FailSmall(self):
		"""Prints red "✘" sign"""
		print(f"{Fore.RED}✘")
	def print(self, msgs, useColor, column, eolRule):
		colors = {"red":Fore.RED, "green":Fore.GREEN, "yellow":Fore.YELLOW}
		for msg in msgs:
			print(f"{colors[useColor]}{msg: <{column}}", end = eolRule)


		