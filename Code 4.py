import tkinter as tk
from PIL import Image, ImageTk

def showImage():
    img = Image.open('bedroom.png')
    img = img.resize((800,700))
    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo)
    image_label.image = photo

root = tk.Tk()
root.title('pip')
root.geometry('1200x800')

font = ('Comic Sans MS',22)

label=tk.Label(root,text='YOU FOUND ME YOU WIN YAYYYY YOU BEAT THE GAME YAYYYYY YAYYYYY :D',font = font)
label.pack()

button=tk.Button(root,text="CLICK ME  = sleepy zzzzzzzzzzzzzzzzzzzzzzzz ",font = font,command=showImage)
button.pack()

image_label = tk.Label(root)
image_label.pack()

root.mainloop()
