from tkinter import *

# declare the window
window = Tk()

# set window title
window.title("My First Super Duper App oh yeah")

# set window width and height
window.configure(width=500, height=300)

# set window background color
window.configure(bg='green')

# move window center
winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

window.mainloop()