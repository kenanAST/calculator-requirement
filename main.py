from tkinter import *
from display import Display
import threading


class Calculator:

    def __init__(self):
        self.window = Tk()
        self.window.title('Scientific Calculator')
        self.window.geometry("850x539")
        self.window.configure(bg = "#ebf2fa")

        self.position = 0

        self.topcanvas = Canvas(
            self.window,
            bg = "#ebf2fa",
            height = 80,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.topcanvas.place(x = 0, y = 75)


        self.lowercanvas = Canvas(
            self.window,
            bg = "#ebf2fa",
            height = 40,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.lowercanvas.place(x = 0, y = 150)


        self.historyCanvas = Canvas(
            self.window,
            bg = "#ebf2fa",
            height = 800,
            width = 315,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.historyCanvas.place(x = 535, y = 0)


        self.historyCanvas.create_text(
            10, 10,
            text = "History",
            fill = "#427aa1",
            font = ("Abel-Regular", int(22.39285659790039)),
            anchor="nw"
        )

        self.main_display = Display([], self.lowercanvas, self.topcanvas, self.historyCanvas)
        inputField = threading.Thread(target = self.input_display, daemon=True)
        inputField.start()

        self.img0 = PhotoImage(file = f"assets/img0.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.goRight,
            relief = "flat")

        self.b0.place(
            x = 239, y = 481,
            width = 51,
            height = 41)

        self.img1 = PhotoImage(file = f"assets/img1.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.goLeft,
            relief = "flat")

        self.b1.place(
            x = 165, y = 481,
            width = 49,
            height = 38)

        self.img2 = PhotoImage(file = f"assets/img2.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("."),
            relief = "flat")

        self.b2.place(
            x = 429, y = 480,
            width = 20,
            height = 40)

        self.img3 = PhotoImage(file = f"assets/img3.png")
        self.b3 = Button(
            image = self.img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("0"),
            relief = "flat")

        self.b3.place(
            x = 344, y = 482,
            width = 20,
            height = 40)

        self.img4 = PhotoImage(file = f"assets/img4.png")
        self.b4 = Button(
            image = self.img4,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("1"),
            relief = "flat")

        self.b4.place(
            x = 255, y = 406,
            width = 20,
            height = 40)

        self.img5 = PhotoImage(file = f"assets/img5.png")
        self.b5 = Button(
            image = self.img5,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("sin("),
            relief = "flat")

        self.b5.place(
            x = 45, y = 419,
            width = 39,
            height = 16)

        self.img6 = PhotoImage(file = f"assets/img6.png")
        self.b6 = Button(
            image = self.img6,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("cos("),
            relief = "flat")

        self.b6.place(
            x = 101, y = 418,
            width = 39,
            height = 16)

        self.img7 = PhotoImage(file = f"assets/img7.png")
        self.b7 = Button(
            image = self.img7,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked(")"),
            relief = "flat")

        self.b7.place(
            x = 101, y = 489,
            width = 39,
            height = 16)

        self.img8 = PhotoImage(file = f"assets/img8.png")
        self.b8 = Button(
            image = self.img8,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("("),
            relief = "flat")

        self.b8.place(
            x = 40, y = 490,
            width = 39,
            height = 16)

        self.img9 = PhotoImage(file = f"assets/img9.png")
        self.b9 = Button(
            image = self.img9,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("tan("),
            relief = "flat")

        self.b9.place(
            x = 165, y = 418,
            width = 39,
            height = 16)

        self.img10 = PhotoImage(file = f"assets/img10.png")
        self.b10 = Button(
            image = self.img10,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("2"),
            relief = "flat")

        self.b10.place(
            x = 344, y = 406,
            width = 20,
            height = 40)

        self.img11 = PhotoImage(file = f"assets/img11.png")
        self.b11 = Button(
            image = self.img11,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("3"),
            relief = "flat")

        self.b11.place(
            x = 432, y = 406,
            width = 20,
            height = 40)

        self.img12 = PhotoImage(file = f"assets/img12.png")
        self.b12 = Button(
            image = self.img12,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("4"),
            relief = "flat")

        self.b12.place(
            x = 255, y = 326,
            width = 20,
            height = 40)

        self.img13 = PhotoImage(file = f"assets/img13.png")
        self.b13 = Button(
            image = self.img13,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("π"),
            relief = "flat")

        self.b13.place(
            x = 180, y = 325,
            width = 20,
            height = 40)

        self.img14 = PhotoImage(file = f"assets/img14.png")
        self.b14 = Button(
            image = self.img14,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("log("),
            relief = "flat")

        self.b14.place(
            x = 101, y = 249,
            width = 58,
            height = 33)

        self.img15 = PhotoImage(file = f"assets/img15.png")
        self.b15 = Button(
            image = self.img15,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("ln("),
            relief = "flat")

        self.b15.place(
            x = 60, y = 250,
            width = 18,
            height = 33)

        self.img16 = PhotoImage(file = f"assets/img16.png")
        self.b16 = Button(
            image = self.img16,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("/"),
            relief = "flat")

        self.b16.place(
            x = 190, y = 236,
            width = 20,
            height = 60)

        self.img17 = PhotoImage(file = f"assets/img17.png")
        self.b17 = Button(
            image = self.img17,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("10^"),
            relief = "flat")

        self.b17.place(
            x = 107, y = 313,
            width = 43,
            height = 53)

        self.img18 = PhotoImage(file = f"assets/img18.png")
        self.b18 = Button(
            image = self.img18,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("^"),
            relief = "flat")

        self.b18.place(
            x = 50, y = 313,
            width = 34,
            height = 52)

        self.img19 = PhotoImage(file = f"assets/img19.png")
        self.b19 = Button(
            image = self.img19,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("5"),
            relief = "flat")

        self.b19.place(
            x = 344, y = 326,
            width = 20,
            height = 40)

        self.img20 = PhotoImage(file = f"assets/img20.png")
        self.b20 = Button(
            image = self.img20,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("6"),
            relief = "flat")

        self.b20.place(
            x = 432, y = 326,
            width = 20,
            height = 40)

        self.img21 = PhotoImage(file = f"assets/img21.png")
        self.b21 = Button(
            image = self.img21,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("7"),
            relief = "flat")

        self.b21.place(
            x = 255, y = 246,
            width = 20,
            height = 40)

        self.img22 = PhotoImage(file = f"assets/img22.png")
        self.b22 = Button(
            image = self.img22,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("e"),
            relief = "flat")

        self.b22.place(
            x = 190, y = 192,
            width = 20,
            height = 40)

        self.img23 = PhotoImage(file = f"assets/img23.png")
        self.b23 = Button(
            image = self.img23,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("8"),
            relief = "flat")

        self.b23.place(
            x = 344, y = 246,
            width = 20,
            height = 40)

        self.img24 = PhotoImage(file = f"assets/img24.png")
        self.b24 = Button(
            image = self.img24,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("9"),
            relief = "flat")

        self.b24.place(
            x = 432, y = 246,
            width = 20,
            height = 40)


        self.img25 = PhotoImage(file = f"assets/img25.png")
        self.b25 = Button(
            image = self.img25,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("clear"),
            relief = "flat")

        self.b25.place(
            x = 252, y = 196,
            width = 20,
            height = 33)

        self.img26 = PhotoImage(file = f"assets/img26.png")
        self.b26 = Button(
            image = self.img26,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("clearAll"),
            relief = "flat")

        self.b26.place(
            x = 337, y = 196,
            width = 26,
            height = 33)


        self.img28 = PhotoImage(file = f"assets/img28.png")
        self.b28 = Button(
            image = self.img28,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("pop"),
            relief = "flat")

        self.b28.place(
            x = 422, y = 200,
            width = 30,
            height = 22)

        self.img29 = PhotoImage(file = f"assets/img29.png")
        self.b29 = Button(
            image = self.img29,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("total"),
            relief = "flat")

        self.b29.place(
            x = 478, y = 472,
            width = 47,
            height = 48)

        self.img30 = PhotoImage(file = f"assets/img30.png")
        self.b30 = Button(
            image = self.img30,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("+"),
            relief = "flat")

        self.b30.place(
            x = 492, y = 406,
            width = 20,
            height = 40)

        self.img31 = PhotoImage(file = f"assets/img31.png")
        self.b31 = Button(
            image = self.img31,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("-"),
            relief = "flat")

        self.b31.place(
            x = 493, y = 325,
            width = 20,
            height = 40)

        self.img32 = PhotoImage(file = f"assets/img32.png")
        self.b32 = Button(
            image = self.img32,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("*"),
            relief = "flat")

        self.b32.place(
            x = 492, y = 246,
            width = 20,
            height = 40)

        self.img33 = PhotoImage(file = f"assets/img33.png")
        self.b33 = Button(
            image = self.img33,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("/"),
            relief = "flat")

        self.b33.place(
            x = 491, y = 193,
            width = 20,
            height = 40)

        self.factorial = PhotoImage(file = f"assets/factorial.png")
        self.factorialButton = Button(
            image = self.factorial,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: self.btn_clicked("fact("),
            relief = "flat")

        self.factorialButton.place(
            x = 125, y = 193,
            width = 20,
            height = 40)

        self.window.resizable(False, False)
    
    def btn_clicked(self, command):
        try:
            self.main_display.stack.remove("|")
        except:
            pass
        if(command != "pop" and command != "total"):
            self.position += 1
        elif(command == "pop" and (self.position > 0)):
            self.position-=1
        self.main_display.update_lowerScreen()
        self.main_display.evaluate_screen(command, self.position)


    def goLeft(self):
        print(self.position)
        if(self.position > 0):
            self.position-=1
            self.main_display.update_lowerScreen()

    def goRight(self):
        if(self.position < len(self.main_display.stack) - 1):
            self.position+=1
            self.main_display.update_lowerScreen()


    def input_display(self):
        while(True):
            self.main_display.input_line(self.position)
    
    def run(self):
        self.window.mainloop()
    

if __name__ == "__main__":
    scieCal = Calculator()
    scieCal.run()

