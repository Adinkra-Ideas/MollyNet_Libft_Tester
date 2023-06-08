# --------------------------------------------------------
# About the Project: MollyNet Libft Tester is written in 
# Python3 for testing the 42 Schools LIBFT Project.
#
# Author: Daniel E. Uyi (euyi@student.42wolfsburg.de)
# Date of Creation: 8th June 2023
#
# RFC: Couldn't add comments because my Nails hurt ;)
# ---------------------------------------------------------

# Importing our Display class for handling print actions
from modules.Display import Display
display = Display()

# Column rules for aligning the display in terminal
setColumn = 19
noSetColumn = 0

# 
EOL = "\r\n"
noEOL = ""

RED = "red"
GREEN = "green"
YELLOW = "yellow"

import os
if os.name != "posix":
	display.print(['Fatal ERROR! Please Run Tester on POSIX Image!'], RED, noSetColumn, EOL)
	raise SystemExit(1)

from modules.Files import Files
test_file = Files()

os.system("clear")

from modules.Utils import HEADER
display.print(HEADER, GREEN, noSetColumn, noEOL)

display.print(['Function', 'Norminette', 'Compile', 'Tests', 'Leaks'], YELLOW, setColumn, noEOL)
print()



#TODO 
# hANDLE SIGNAL TO make program exit gracefully on interrupt at filepath request
# In display.py, I repeated myself in passBig type 4X

# display.PassBig()
# display.PassSmall()
# display.FailBig()
# display.FailSmall()



