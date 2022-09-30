import tkinter as tk

from PIL import ImageTk, Image


background = tk.Tk()

background.attributes("-fullscreen", True)

background_image = ImageTk.PhotoImage(Image.open("/home/tester/PycharmProjects/TVProject/LockScreen-Eugene.png"))
background_label = tk.Label(background, image=background_image)
background_label.pack(fill=tk.BOTH)

background.mainloop()