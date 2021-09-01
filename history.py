



class History:

    def __init__(self, stack, canvas):
            self.stack = stack
            self.canvas = canvas


    def drawHistoryLine(self):
        self.canvas.delete("all")
        print(self.stack)
        self.canvas.create_text(
        10, 10,
        text = "History",
        fill = "#427aa1",
        font = ("Abel-Regular", int(22.39285659790039)),
        anchor="nw")
        for count, history in enumerate(reversed(self.stack)):
            self.canvas.create_text(
                305, 125 + (count*90),
                text = history[0],
                fill = "#002a3c",
                font = ("Abel-Regular", int(36.0)),
                anchor="se"
            )

            self.canvas.create_text(
                305, (140 + (count*90)),
                text = history[1],
                fill = "#427aa1",
                font = ("Abel-Regular", int(14)),
                anchor="se"
            )