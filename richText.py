
# -------------------------------------------------------------
#  this code tests out the Rich library for text formatting
#  By: Zane Dax
#  Date: April 23, 2021
# -------------------------------------------------------------


#----- rich library

from rich import print


# basic output
print(f'Math print out: 2+4 : {2+4}')
print({'a':[1,2,3], 'b':[5,6,7]})


from rich.console import Console 

console = Console()
console.print(' rich text using console ')
console.print(" rich text using console, style=bold" , style='bold')
console.print(" rich text using console", style='bold underline green')
console.print(" rich text using console" , style='bold underline white on red')

console.print(" [bold]rich text [cyan]using [/]console[/]")


from rich.text import Text

text = Text(" Hello text.stylize() text!")
text.stylize('bold yellow', 1, 13) # start, stop
console.print(text)


msg_1 = " Operation success"
msg_2 = " Operation fail"
msg3 = " Operation [error] failed [/error]"

from rich.theme import Theme 

console.print(msg_1, style='bold green')
console.print(msg_2, style='underline red')
console.print(msg3, style='bold red')



# Emoji
console.print(" :thumbs_up: You did it!")
console.print(" :snake: Python code")
console.print(" :heart: This code snippet!")


import time

for i in range(5):
	console.log(f" Running your code ... {i}")
	time.sleep(0.5)


#---------------- traceback
# from rich.traceback import install
# install()

# def add(x, y):
# 	a= "hello"
# 	console.log("Adding sums ", log_locals=True)
# 	return x+y

#---
# console = Console(record=True)

# try:
# 	add(2,5)
# 	add(-9,45)
# 	add(1, "a")
# except:
# 	console.print_exception()

# console.save_html('demo.html')





# table
from rich.table import Table 
table = Table(title="Star Wars")

table.add_column("Released", style="cyan")
table.add_column("Title", style="magenta")
table.add_column("Box Office", style="green", justify='right')

table.add_row('Dec 9, 2016','Star Wars X','$56,765,867')
table.add_row('Dec 4, 2017','Star Wars XI','$58,765,867')
table.add_row('Nov 2, 2018','Star Wars XII','$96,765,867')
table.add_row('Oct 19, 2019','Star Wars XII','$156,765,867')

console.print(table)





#- markdowm
from rich.markdown import Markdown 

MARKDOWN = """

# This is Header

## subtitle header 

List:

	1. one

	2. two

$\mu\$= 78.9
"""

md= Markdown(MARKDOWN)
# console.print(md)




# progress bar
from rich.progress import track 

for i in track(range(5), description='Processing ...'):
	print(f'working {i}')
	time.sleep(0.5)



























print('\n')