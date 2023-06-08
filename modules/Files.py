# Module for accessing files using object-oriented approach
from pathlib import Path

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Files:
	def __init__(self):
		self.filePath = self.readFilePath()
	
	def readFilePath(self):
		test_file = Path("./ft_isalpha.c")
		if test_file.is_file():
			return "./"
		
		test_file = Path("../ft_isalpha.c")
		if test_file.is_file():
			return "../"
		
		while not test_file.is_file():
			test_path = input(Fore.YELLOW + "Enter dir of your libft. Example ./ or ~/ or /home/\n: ")
			if not test_path.endswith('/'):
				test_path = test_path + '/'
			test_file = Path(test_path + "ft_isalpha.c")
			if test_file.is_file():
				return test_path
			print(f"{Fore.RED}Unable to find your LIBFT Files in directory ", test_path)
		
		raise SystemExit(1)
