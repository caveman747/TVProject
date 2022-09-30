import tkinterclasses




def main():

    i = 0

    while i < 3:

        pageone = tkinterclasses.PageOne()

        pageone.after(3000, pageone.destroy)

        pageone.destroy()

        pagetwo = tkinterclasses.PageOne()

        pagetwo.after(3000, pagetwo.destroy)

        pagetwo.mainloop()

        i = i + 1



if __name__ == "__main__":
    main()