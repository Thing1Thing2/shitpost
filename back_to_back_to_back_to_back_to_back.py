import keyboard
from image import DrawImage

"I don't wanna go back back to back to back..."

cut_it_out = False
while not cut_it_out:
    print("back to back to back to back to back")
    if keyboard.is_pressed("q"):
        cut_it_out = True

print("to you.")
print("I don't wanna fall right back to us.")
print("maybe you should run right back to her")

# show the damn image
image = DrawImage.from_file("./brat.png")
image.draw_image()  # shitty library
