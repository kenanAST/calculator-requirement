from tkinter import *

class Display:

    def __init__(self, stack, canvas):
        self.stack = stack
        self.canvas = canvas

    def update_screen(self, value):
        if(value == "total"):
            self.canvas.create_text(
            290.0, 160.5,
            text = str(eval("50 - 10 - 10 - 10 + 100")),
            fill = "#002a3c",
            font = ("Abel-Regular", int(89.57142639160156)))

        self.canvas.create_text(
            256.0, 234.0,
            text = "50 - 10 - 10 - 10 + 100",
            fill = "#427aa1",
            font = ("Abel-Regular", int(22.39285659790039)))