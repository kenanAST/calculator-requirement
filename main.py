from tkinter import *
from display import Display

def btn_clicked():
    print("Hemlo World")
    main_display = Display("25", canvas)
    main_display.update_screen("total")


# def update_screen(value):

#     if(value == "total"):
#         canvas.create_text(
#         290.0, 160.5,
#         text = str(eval()),
#         fill = "#002a3c",
#         font = ("Abel-Regular", int(89.57142639160156)))


#     canvas.create_text(
#         256.0, 234.0,
#         text = "50 - 10 - 10 - 10 + 100",
#         fill = "#427aa1",
#         font = ("Abel-Regular", int(22.39285659790039)))


window = Tk()
window.title('Scientific Calculator')
window.geometry("414x896")
window.configure(bg = "#ebf2fa")


canvas = Canvas(
    window,
    bg = "#ebf2fa",
    height = 896,
    width = 414,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)



img10 = PhotoImage(file = f"assets/img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b10.place(
    x = 153, y = 549,
    width = 20,
    height = 40)


window.resizable(False, False)
window.mainloop()