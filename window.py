from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("939x896")
window.configure(bg = "#002a3c")
canvas = Canvas(
    window,
    bg = "#002a3c",
    height = 896,
    width = 939,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    469.5, 448.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 277, y = 669,
    width = 442,
    height = 99)

window.resizable(False, False)
window.mainloop()
