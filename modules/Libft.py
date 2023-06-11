# Module for accessing files using object-oriented approach
from pathlib import Path

# For using Python from CLI
import subprocess

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Libft:
	#
	def __init__(self):
		self.filePath = self.readFilePath()
		self.fileNames = self.readFileNames()
	
	#
	def readFilePath(self):
		possibleFilePaths = ['../libft/', './', '../']
		keyFile = "ft_isalpha.c"

		# MolyNet automatically searches for libft files from possibleFilePaths
		for onePath in possibleFilePaths:
			test_file = Path(onePath + keyFile)
			if test_file.is_file():
				return onePath

		# If no libft files found in possibleFilePaths, ask the user to input their Libft dir path 
		while not test_file.is_file():
			test_path = input(Fore.YELLOW + "Enter dir of your libft. Example ./ or ~/ or /home/\n: ")
			if not test_path.endswith('/'):
				test_path = test_path + '/'
			test_file = Path(test_path + "ft_isalpha.c")
			if test_file.is_file():
				# Add this newly found dir path into the list of directories in possibleFilePaths
				subprocess.run(['sed', '-i', f's#possibleFilePaths = \[#possibleFilePaths = \[\'{test_path}\', #', './modules/Libft.py'], capture_output=True)
				return test_path
			print(f"{Fore.RED}Unable to find your LILibft in directory ", test_path)
		
		raise SystemExit(1)
	
	#
	def readFileNames(self):
		return ({
			"ft_atoi.c": self.filePath + "ft_atoi.c",
			"ft_bzero.c": self.filePath + "ft_bzero.c",
			"ft_calloc.c": self.filePath + "ft_calloc.c",
			"ft_isalnum.c": self.filePath + "ft_isalnum.c",
			"ft_isalpha.c": self.filePath + "ft_isalpha.c",
			"ft_isascii.c": self.filePath + "ft_isascii.c",
			"ft_isdigit.c": self.filePath + "ft_isdigit.c",
			"ft_isprint.c": self.filePath + "ft_isprint.c",
			"ft_itoa.c": self.filePath + "ft_itoa.c",
			"ft_lstadd_back.c": self.filePath + "ft_lstadd_back.c",
			"ft_lstadd_front.c": self.filePath + "ft_lstadd_front.c",
			"ft_lstclear.c": self.filePath + "ft_lstclear.c",
			"ft_lstdelone.c": self.filePath + "ft_lstdelone.c",
			"ft_lstiter.c": self.filePath + "ft_lstiter.c",
			"ft_lstlast.c": self.filePath + "ft_lstlast.c",
			"ft_lstmap.c": self.filePath + "ft_lstmap.c",
			"ft_lstnew.c": self.filePath + "ft_lstnew.c",
			"ft_lstsize.c": self.filePath + "ft_lstsize.c",
			"ft_memchr.c": self.filePath + "ft_memchr.c",
			"ft_memcmp.c": self.filePath + "ft_memcmp.c",
			"ft_memcpy.c": self.filePath + "ft_memcpy.c",
			"ft_memmove.c": self.filePath + "ft_memmove.c",
			"ft_memset.c": self.filePath + "ft_memset.c",
			"ft_putchar_fd.c": self.filePath + "ft_putchar_fd.c",
			"ft_putendl_fd.c": self.filePath + "ft_putendl_fd.c",
			"ft_putnbr_fd.c": self.filePath + "ft_putnbr_fd.c",
			"ft_putstr_fd.c": self.filePath + "ft_putstr_fd.c",
			"ft_split.c": self.filePath + "ft_split.c",
			"ft_strchr.c": self.filePath + "ft_strchr.c",
			"ft_strdup.c": self.filePath + "ft_strdup.c",
			"ft_striteri.c": self.filePath + "ft_striteri.c",
			"ft_strjoin.c": self.filePath + "ft_strjoin.c",
			"ft_strlcat.c": self.filePath + "ft_strlcat.c",
			"ft_strlcpy.c": self.filePath + "ft_strlcpy.c",
			"ft_strlen.c": self.filePath + "ft_strlen.c",
			"ft_strmapi.c": self.filePath + "ft_strmapi.c",
			"ft_strncmp.c": self.filePath + "ft_strncmp.c",
			"ft_strnstr.c": self.filePath + "ft_strnstr.c",
			"ft_strrchr.c": self.filePath + "ft_strrchr.c",
			"ft_strtrim.c": self.filePath + "ft_strtrim.c",
			"ft_substr.c": self.filePath + "ft_substr.c",
			"ft_tolower.c": self.filePath + "ft_tolower.c",
			"ft_toupper.c": self.filePath + "ft_toupper.c"			
		})
	
	def norminette(self, filePath):
		test_path = Path(filePath)
		if test_path.is_file():
			retVal = subprocess.run(['norminette', filePath], capture_output=True) 
			return retVal.returncode	
		return 1

# Init the class
libft = Libft()
