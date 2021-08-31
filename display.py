from tkinter import *

class Display:

    def __init__(self, stack, canvas):
        self.stack = stack
        self.canvas = canvas


    def format_displayScreen(self):
        lowerText = ""
        for text in self.stack:
            lowerText += text
        return lowerText

    def update_lowerScreen(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            375, 234.0,
            text = self.format_displayScreen(),
            fill = "#427aa1",
            font = ("Abel-Regular", int(22.39285659790039)),
            anchor = "se")
            #22.39285659790039

    def update_totalScreen(self):
        self.canvas.create_text(
        375, 200,
        text = str(eval(self.format_displayScreen())),
        fill = "#002a3c",
        font = ("Abel-Regular", int(72)),
        anchor = "se")


    def evaluate_screen(self, value):
        if(value == "total"):
            self.update_totalScreen()
        else:
            self.stack.append(value)
            print(self.stack)
            self.update_lowerScreen()
