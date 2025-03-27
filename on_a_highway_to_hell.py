print("One way trip to unemployment.")

print(
    """
Give me a call if you ever get lonely.
I'll be like one of your girls.
"""
)

print("FACE CARD, NO CASH NO CREDIT")


print("look at you, skip the application interview.")

# v is really creepy

from tkinter import *
from PIL import Image, ImageTk


class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq = []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq))  # skip to next frame
        except EOFError:
            pass  # we're done

        try:
            self.delay = im.info["duration"]
        except KeyError:
            self.delay = 100

        first = seq[0].convert("RGB")
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert("RGB")
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)


class Main:
    def __init__(self):
        root = Tk()
        self.anim = MyLabel(root, "troyee.gif")
        self.anim.pack()
        Button(root, text="stop", command=self.stop_it).pack()
        root.mainloop()

    def stop_it(self):
        self.anim.after_cancel(self.anim.cancel)


main = Main()
