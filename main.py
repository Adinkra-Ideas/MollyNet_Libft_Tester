# --------------------------------------------------------
# About the Project: MolyNet Libft Tester is written in 
# Python3 for testing the 42 Schools LIBFT Project.
#
# Author: Daniel E. Uyi (euyi@student.42wolfsburg.de)
# Date of Creation: 8th June 2023
#
# RFC: Couldn't add comments because my Nails hurt ;)
# ---------------------------------------------------------

# Importing our Display class for handling print actions
from modules.Display import display

# Importing our libft class that contains the filename and filepaths
# of our libfts
from modules.Libft import libft

# For the Love of Adinkra!
from modules.Utils import HEADER

# This program should run only on 'posix' OS
import os
if os.name != "posix":
	display.print(['Fatal ERROR! Please Run Tester on POSIX Image!'], RED, noSetColumn, EOL)
	raise SystemExit(1)

# I, almighty Adinkra, Maintainer of the Matrix and Ordainer of all Humans' Destiny, declare this CLI cleared!
os.system("clear")

# Todo: Here we will add guard for python 3 as well 

# Column rules for aligning the display in terminal
setColumn = 19
noSetColumn = 0

# 
EOL = "\r\n"
noEOL = ""

#
RED = "red"
GREEN = "green"
YELLOW = "yellow"
MAGENTA = "magenta"
CYAN = "cyan"

display.print(HEADER, GREEN, noSetColumn, noEOL)

display.print(['Function', 'Norminette', 'Compile', 'Tests', 'Leaks'], YELLOW, setColumn, noEOL)
print()

for fileName, filePath in libft.fileNames.items():
	display.print([fileName], MAGENTA, setColumn, noEOL)
	display.grade("✔" if not libft.norminette(filePath) else "✘", setColumn, noEOL)
	# continue from here AKA grading for compilation
	print()


# TODO 
# hANDLE SIGNAL TO make program exit gracefully on interrupt at filepath request

