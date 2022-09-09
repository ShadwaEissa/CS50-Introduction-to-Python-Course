import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

#if there is no arguments after the file name, output text in random font
if len(sys.argv) == 1:
    input = input("Input: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(input))

#if there is 2 arguments after file name:
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
    input = input("Input: ")
    #set the font based on the second argument
    figlet.setFont(font=sys.argv[2])
    #print the text based on the font chosen
    print(figlet.renderText(input))

else:
    sys.exit("Invalid usage")
