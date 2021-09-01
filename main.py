from tkinter import *
from display import Display
import datetime
import threading
import time

# main_display.input_line(position)

window = Tk()
window.title('Scientific Calculator')
window.geometry("850x539")
window.configure(bg = "#ebf2fa")

position = 0

def btn_clicked(command):
    try:
        main_display.stack.remove("|")
    except:
        pass
    global position 
    position += 1
    main_display.evaluate_screen(command)


def input_display():
    global position
    while(True):
        print(position)
        main_display.input_line(position)

topcanvas = Canvas(
    window,
    bg = "#ebf2fa",
    height = 896,
    width = 414,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
topcanvas.place(x = 0, y = 0)


lowercanvas = Canvas(
    window,
    bg = "#00FF00",
    height = 100,
    width = 414,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
lowercanvas.place(x = 0, y = 200)


canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 400,
    width = 315,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 535, y = 0)


main_display = Display([], lowercanvas, topcanvas)
threading.Thread(target = input_display).start()
img0 = PhotoImage(file = f"assets/img0.png")


img0 = PhotoImage(file = f"assets/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b0.place(
    x = 239, y = 481,
    width = 51,
    height = 41)

img1 = PhotoImage(file = f"assets/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b1.place(
    x = 165, y = 481,
    width = 49,
    height = 38)

canvas.create_text(
    10, 10,
    text = "History",
    fill = "#427aa1",
    font = ("Abel-Regular", int(22.39285659790039)),
    anchor="nw")

img2 = PhotoImage(file = f"assets/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b2.place(
    x = 429, y = 480,
    width = 20,
    height = 40)

img3 = PhotoImage(file = f"assets/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b3.place(
    x = 344, y = 482,
    width = 20,
    height = 40)

img4 = PhotoImage(file = f"assets/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b4.place(
    x = 255, y = 406,
    width = 20,
    height = 40)

img5 = PhotoImage(file = f"assets/img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b5.place(
    x = 45, y = 419,
    width = 39,
    height = 16)

img6 = PhotoImage(file = f"assets/img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b6.place(
    x = 101, y = 418,
    width = 39,
    height = 16)

img7 = PhotoImage(file = f"assets/img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b7.place(
    x = 101, y = 489,
    width = 39,
    height = 16)

img8 = PhotoImage(file = f"assets/img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b8.place(
    x = 40, y = 490,
    width = 39,
    height = 16)

img9 = PhotoImage(file = f"assets/img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b9.place(
    x = 165, y = 418,
    width = 39,
    height = 16)

img10 = PhotoImage(file = f"assets/img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b10.place(
    x = 344, y = 406,
    width = 20,
    height = 40)

img11 = PhotoImage(file = f"assets/img11.png")
b11 = Button(
    image = img11,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b11.place(
    x = 432, y = 406,
    width = 20,
    height = 40)

img12 = PhotoImage(file = f"assets/img12.png")
b12 = Button(
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b12.place(
    x = 255, y = 326,
    width = 20,
    height = 40)

img13 = PhotoImage(file = f"assets/img13.png")
b13 = Button(
    image = img13,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b13.place(
    x = 180, y = 325,
    width = 20,
    height = 40)

img14 = PhotoImage(file = f"assets/img14.png")
b14 = Button(
    image = img14,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b14.place(
    x = 101, y = 249,
    width = 58,
    height = 33)

img15 = PhotoImage(file = f"assets/img15.png")
b15 = Button(
    image = img15,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b15.place(
    x = 60, y = 250,
    width = 18,
    height = 33)

img16 = PhotoImage(file = f"assets/img16.png")
b16 = Button(
    image = img16,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b16.place(
    x = 190, y = 236,
    width = 20,
    height = 60)

img17 = PhotoImage(file = f"assets/img17.png")
b17 = Button(
    image = img17,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b17.place(
    x = 107, y = 313,
    width = 43,
    height = 53)

img18 = PhotoImage(file = f"assets/img18.png")
b18 = Button(
    image = img18,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b18.place(
    x = 50, y = 313,
    width = 34,
    height = 52)

img19 = PhotoImage(file = f"assets/img19.png")
b19 = Button(
    image = img19,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b19.place(
    x = 344, y = 326,
    width = 20,
    height = 40)

img20 = PhotoImage(file = f"assets/img20.png")
b20 = Button(
    image = img20,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b20.place(
    x = 432, y = 326,
    width = 20,
    height = 40)

img21 = PhotoImage(file = f"assets/img21.png")
b21 = Button(
    image = img21,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b21.place(
    x = 255, y = 246,
    width = 20,
    height = 40)

img22 = PhotoImage(file = f"assets/img22.png")
b22 = Button(
    image = img22,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b22.place(
    x = 190, y = 192,
    width = 20,
    height = 40)

img23 = PhotoImage(file = f"assets/img23.png")
b23 = Button(
    image = img23,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b23.place(
    x = 344, y = 246,
    width = 20,
    height = 40)

img24 = PhotoImage(file = f"assets/img24.png")
b24 = Button(
    image = img24,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b24.place(
    x = 432, y = 246,
    width = 20,
    height = 40)


canvas.create_text(
    305, 125,
    text = "120",
    fill = "#002a3c",
    font = ("Abel-Regular", int(36.0)),
    anchor="se")

canvas.create_text(
    305, 160,
    text = "50 - 10 - 10 - 10 + 100",
    fill = "#427aa1",
    font = ("Abel-Regular", int(14)),
    anchor="se")

img25 = PhotoImage(file = f"assets/img25.png")
b25 = Button(
    image = img25,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b25.place(
    x = 252, y = 196,
    width = 20,
    height = 33)

img26 = PhotoImage(file = f"assets/img26.png")
b26 = Button(
    image = img26,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b26.place(
    x = 337, y = 196,
    width = 26,
    height = 33)

img27 = PhotoImage(file = f"assets/img27.png")
b27 = Button(
    image = img27,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b27.place(
    x = 425, y = 199,
    width = 27,
    height = 27)

img28 = PhotoImage(file = f"assets/img28.png")
b28 = Button(
    image = img28,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b28.place(
    x = 422, y = 200,
    width = 30,
    height = 22)

img29 = PhotoImage(file = f"assets/img29.png")
b29 = Button(
    image = img29,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b29.place(
    x = 478, y = 472,
    width = 47,
    height = 48)

img30 = PhotoImage(file = f"assets/img30.png")
b30 = Button(
    image = img30,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b30.place(
    x = 492, y = 406,
    width = 20,
    height = 40)

img31 = PhotoImage(file = f"assets/img31.png")
b31 = Button(
    image = img31,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b31.place(
    x = 493, y = 325,
    width = 20,
    height = 40)

img32 = PhotoImage(file = f"assets/img32.png")
b32 = Button(
    image = img32,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b32.place(
    x = 492, y = 246,
    width = 20,
    height = 40)

img33 = PhotoImage(file = f"assets/img33.png")
b33 = Button(
    image = img33,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked("2"),
    relief = "flat")

b33.place(
    x = 491, y = 193,
    width = 20,
    height = 40)


window.resizable(False, False)
window.mainloop()


