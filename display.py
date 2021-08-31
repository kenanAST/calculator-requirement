from time import time
from tkinter import *
import time
from typing import cast

class Display:

    def __init__(self, stack, lowercanvas, topcanvas):
        self.stack = stack
        self.lowercanvas = lowercanvas
        self.topcanvas = topcanvas



    def input_line(self, input_position):
        self.stack.insert(input_position, "|")
        self.update_lowerScreen()
        print("Removes")
        time.sleep(0.5)
        try: 
            self.stack.remove("|")
            self.update_lowerScreen()
            time.sleep(0.5)
        except ValueError:
            pass


    def format_displayScreen(self):
        lowerText = ""
        for text in self.stack:
            lowerText += text
        return lowerText


    # def update_lowerScreen(self):
    #     e = Entry(self.canvas)
    #     self.canvas.create_window(375,100,window=e)
    #     e.insert(len(self.stack),self.format_displayScreen())


    def update_lowerScreen(self):
        self.lowercanvas.delete("all")
        self.lowercanvas.create_text(
            375, 25,
            text = self.format_displayScreen(),
            fill = "#427aa1",
            font = ("Abel-Regular", int(22.39285659790039)),
            anchor = "se")
            # 22.39285659790039

    def update_totalScreen(self):
        self.topcanvas.create_text(
        375, 200,
        text = str(eval(self.format_displayScreen())),
        fill = "#002a3c",
        font = ("Abel-Regular", int(48)),
        anchor = "se")


    def evaluate_screen(self, value):
        if(value == "total"):
            self.update_totalScreen()
        else:
            self.stack.append(value)
            print(self.stack)
            self.update_lowerScreen()
