from datetime import datetime
import pytz
import tkinter as tk
from time import strftime

from PIL import ImageTk, Image

class PageOne(tk.Tk):
    def __init__(self):
        super().__init__()

        self.mycolor = '#%02x%02x%02x' % (2, 30, 110)  # set your favourite rgb color

        self.attributes("-fullscreen", True)

        def times():
            home = pytz.timezone("America/Los_Angeles")
            local_time = datetime.now(home)
            datime = local_time.strftime('%H:%M:%S %p')
            clock1.config(text=datime)
            name1.config(text="Time in Eugene Oregon")
            clock1.after(200, times)


        self.background_image = ImageTk.PhotoImage(Image.open("/home/tester/PycharmProjects/TVProject/LockScreen-Eugene.png"))
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.pack(fill=tk.BOTH)


        name1 = tk.Label(self, fg="white", bg=self.mycolor, font=("calibri", 20, "bold"))
        name1.place(rely=.1, relx=.8)
        clock1 = tk.Label(self, fg="white", bg=self.mycolor, font=("calibri", 25, "bold"))
        clock1.place(rely=.2, relx=.8)

        times()


class PageTwo(tk.Tk):
    def __init__(self):
        super().__init__()

        self.mycolor = '#%02x%02x%02x' % (2, 30, 110)  # set your favourite rgb color

        self.attributes("-fullscreen", True)

        def times():
            home = pytz.timezone("America/Los_Angeles")
            local_time = datetime.now(home)
            datime = local_time.strftime('%H:%M:%S %p')
            clock1.config(text=datime)
            name1.config(text="Time in Easdfasfasfdasfdugene Oregon")
            clock1.after(200, times)


        self.background_image = ImageTk.PhotoImage(Image.open("/home/tester/PycharmProjects/TVProject/LockScreen-Bologna.png"))
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.pack(fill=tk.BOTH)


        name1 = tk.Label(self, fg="white", bg=self.mycolor, font=("calibri", 20, "bold"))
        name1.place(rely=.1, relx=.8)
        clock1 = tk.Label(self, fg="white", bg=self.mycolor, font=("calibri", 25, "bold"))
        clock1.place(rely=.2, relx=.8)

        times()

class PageThree(tk.Tk):
    def __init__(self):
        super().__init__()

        self.mycolor = '#%02x%02x%02x' % (2, 30, 110)  # set your favourite rgb color

        self.attributes("-fullscreen", True)

        def times():
            home = pytz.timezone("America/Los_Angeles")
            local_time = datetime.now(home)
            datime = local_time.strftime('%H:%M:%S %p')
            clock1.config(text=datime)
            name1.config(text="Time in Easdfasfasfdasfdugene Oregon")
            clock1.after(200, times)


        self.background_image = ImageTk.PhotoImage(Image.open("/home/tester/PycharmProjects/TVProject/LockScreen-Vietnam.png"))
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.pack(fill=tk.BOTH)


        name1 = tk.Label(self, fg="white", bg=self.mycolor, font=("calibri", 20, "bold"))
        name1.place(rely=.1, relx=.8)
        clock1 = tk.Label(self, fg="white", bg=self.mycolor, font=("calibri", 25, "bold"))
        clock1.place(rely=.2, relx=.8)

        times()
