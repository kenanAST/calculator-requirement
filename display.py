from tkinter import *

class Display:

    def __init__(self, stack, canvas):
        self.stack = stack
        self.canvas = canvas


    def format_displayScreen(self):
        lowerText = ""
        for text in self.stack:
            lowerText += text + " "
        return lowerText

    def update_lowerScreen(self):
        self.canvas.create_text(
            256.0, 234.0,
            text = self.format_displayScreen(),
            fill = "#427aa1",
            font = ("Abel-Regular", int(22.39285659790039)))

    def update_totalScreen(self, lsValue):
        self.canvas.create_text(
        290.0, 160.5,
        text = str(eval(lsValue)),
        fill = "#002a3c",
        font = ("Abel-Regular", int(89.57142639160156)))


    def evaluate_screen(self, value):
        if(value == "total"):
            pass
        elif(value == "8"):
            self.stack.append("8")
            print(self.stack)
            self.update_lowerScreen()
