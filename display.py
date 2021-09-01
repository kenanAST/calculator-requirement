from time import time
from tkinter import *
import time
import history
import math
from typing import cast

class Display:

    ans = 0

    def __init__(self, stack, lowercanvas, topcanvas, historyCanvas):
        self.historyStack = []
        self.stack = stack
        self.lowercanvas = lowercanvas
        self.topcanvas = topcanvas
        self.historySection = history.History(self.historyStack, historyCanvas)


    def input_line(self, input_position):
        self.stack.insert(input_position, "|")
        self.update_lowerScreen()
        time.sleep(0.4)
        try: 
            self.stack.remove("|")
            self.update_lowerScreen()
            time.sleep(0.4)
        except ValueError:
            pass


    def format_displayScreen(self):
        lowerText = ""
        for text in self.stack:
            lowerText += text
        return lowerText


    def solveFormat(self):
        string = self.format_displayScreen()
        string = string.replace("sin(", "math.sin(")
        string = string.replace("cos(", "math.cos(")
        string = string.replace("tan(", "math.tan(")
        string = string.replace("log(", "math.log(")
        string = string.replace("e", "math.e")
        string = string.replace("π", "math.pi")
        string = string.replace("^", "**")
        print("STRING: " + string)
        return string

    # def update_lowerScreen(self):
    #     e = Entry(self.canvas)
    #     self.canvas.create_window(375,100,window=e)
    #     e.insert(len(self.stack),self.format_displayScreen())


    def update_lowerScreen(self):
        self.lowercanvas.delete("all")
        self.lowercanvas.create_text(
            525, 35,
            text = self.format_displayScreen(),
            fill = "#427aa1",
            font = ("Abel-Regular", int(22.39285659790039)),
            anchor = "se")
            # 22.39285659790039

    def update_totalScreen(self):
        print(self.ans)
        self.topcanvas.delete("all")
        if(self.stack != []):
            try:
                toptext = str(round(eval(self.solveFormat()),2))
            except:
                toptext = "Syntax Error"
            self.topcanvas.create_text(
            525, 75,
            text = toptext,
            fill = "#002a3c",
            font = ("Abel-Regular", int(48)),
            anchor = "se")
            if toptext != "Syntax Error":
                self.historySection.stack.append(([toptext],[self.format_displayScreen()]))
                self.historySection.drawHistoryLine()
                self.ans = toptext


    def evaluate_screen(self, value, position):
        if(value == "total"):
            self.update_totalScreen()
        elif(value == "clear"):
            self.stack = []
            self.update_lowerScreen()
            self.update_totalScreen()
        elif(value == "clearAll"):
            self.stack = []
            self.update_lowerScreen()
            self.update_totalScreen()
            self.historySection.stack = []
            self.historySection.drawHistoryLine()
        elif(value == "pop"):
            print( "POSITIONNNN: " + str(position))
            self.stack.pop(position)
            self.update_lowerScreen()
        else:
            self.stack.insert(position - 1, value)
            self.update_lowerScreen()
