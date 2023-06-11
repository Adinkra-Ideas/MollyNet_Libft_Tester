import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Display:
	# For handling printing of checkmarks for grades
	def grade(self, gradeSign, column, eolRule):
		"""Prints white " ✔  " on a green BackGround"""
		print(f"{Fore.WHITE}{Back.GREEN if gradeSign == '✔' else Back.RED}{gradeSign: <{column}}", end = eolRule)
	
	# For handling printing
	def print(self, msgs, useColor, column, eolRule):
		colors = {"red": Fore.RED, "green": Fore.GREEN, "yellow": Fore.YELLOW, "magenta": Fore.MAGENTA, "cyan": Fore.CYAN}
		for msg in msgs:
			print(f"{colors[useColor]}{msg: <{column}}", end = eolRule)

# Init the class
display = Display()
		