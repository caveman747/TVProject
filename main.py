import tkinterclasses
import sys
import signal
import time


def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    sys.exit(0)


while True:

    pageone = tkinterclasses.PageOne()

    pageone.after(3000, pageone.destroy)

    pageone.mainloop()

    time.sleep(3)

    pagetwo = tkinterclasses.PageTwo()

    pagetwo.after(3000, pagetwo.destroy)

    pagetwo.mainloop()

    pagethree = tkinterclasses.PageThree()

    pagethree.after(3000, pagethree.destroy)

    pagethree.mainloop()


