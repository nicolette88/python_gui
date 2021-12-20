# https://pythongeeks.org/gui-programming-in-python/
from tkinter import *
import tkinter.messagebox


def entry_message():
    tkinter.messagebox.showinfo(
        "Köszönöm az értékelést!",
        "Ön: '" + ent.get() + "' értékelte az alkalmazást.")


class Calk():
    def __init__(self):
        self.kifejezes = ""
        self.egyenlet = StringVar()
        self.muvelet = {"+", "-", "*", "/"}

    def get_egyenlet(self):
        return self.egyenlet

    # bemeneti gomb kezelő
    def billentyu(self, num):
        if num in self.muvelet:
            if len(self.kifejezes) > 0:
                if self.kifejezes[-1] != str(num):
                    self.kifejezes = self.kifejezes + str(num)
                    self.egyenlet.set(self.kifejezes)
        else:
            self.kifejezes = self.kifejezes + str(num)
            self.egyenlet.set(self.kifejezes)

    # kiértékelő függvény
    def egyenloseg(self):
        try:
            total = str(eval(self.kifejezes))
            self.egyenlet.set(total)
            self.kifejezes = str(total)
        except:
            self.egyenlet.set(" hiba ")
            self.kifejezes = ""

    def torles(self):
        self.kifejezes = ""
        self.egyenlet.set("")


if __name__ == "__main__":
    # gui létrehozás
    gui = Tk()
    # gui háttérszín beállítás
    gui.configure(background="light blue")
    # gui címe & mérete
    gui.title("Számológép")
    gui.geometry("265x200")
    calk = Calk()
    # kifejezés mező
    kifejezes_mezo = Entry(gui, textvariable=calk.egyenlet)
    kifejezes_mezo.grid(columnspan=4, ipadx=70)

    # bekérés és kiírás
    Label(gui,
          text='Kérem pár szóban értékelje a számológépet: ',
          bg="light blue").grid(row=6, columnspan=4)
    ent = Entry(gui)
    ent.grid(row=7, columnspan=4, ipadx=50)
    entryText = ent.get()
    print(entryText)

    # tkinter lambda használat:
    # https://www.tutorialspoint.com/tkinter-button-commands-with-lambda-in-python
    button1 = Button(gui,
                     text=' 1 ',
                     fg='black',
                     bg='light gray',
                     command=lambda: calk.billentyu(1),
                     height=1,
                     width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui,
                     text=' 2 ',
                     fg='black',
                     bg='light gray',
                     command=lambda: calk.billentyu(2),
                     height=1,
                     width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui,
                     text=' 3 ',
                     fg='black',
                     bg='light gray',
                     command=lambda: calk.billentyu(3),
                     height=1,
                     width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui,
                     text=' 4 ',
                     fg='black',
                     bg='light gray',
                     command=lambda: calk.billentyu(4),
                     height=1,
                     width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui,
                     text=' 5 ',
                     fg='black',
                     bg='light gray',
                     command=lambda: calk.billentyu(5),
                     height=1,
                     width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui,
                     text=' 6 ',
                     fg='black',
                     bg='light gray',
                     command=lambda: calk.billentyu(6),
                     height=1,
                     width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui,
                     text=' 7 ',
                     fg='black',
                     bg='light gray',
                     command=lambda: calk.billentyu(7),
                     height=1,
                     width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui,
                     text=' 8 ',
                     fg='black',
                     bg='light gray',
                     command=lambda: calk.billentyu(8),
                     height=1,
                     width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui,
                     text=' 9 ',
                     fg='black',
                     bg='light gray',
                     command=lambda: calk.billentyu(9),
                     height=1,
                     width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui,
                     text=' 0 ',
                     fg='black',
                     bg='light gray',
                     command=lambda: calk.billentyu(0),
                     height=1,
                     width=7)
    button0.grid(row=5, column=1)

    plusz = Button(gui,
                   text=' + ',
                   fg='black',
                   bg='light gray',
                   command=lambda: calk.billentyu("+"),
                   height=1,
                   width=7)
    plusz.grid(row=2, column=3)

    minusz = Button(gui,
                    text=' - ',
                    fg='black',
                    bg='light gray',
                    command=lambda: calk.billentyu("-"),
                    height=1,
                    width=7)
    minusz.grid(row=3, column=3)

    szorzas = Button(gui,
                     text=' x ',
                     fg='black',
                     bg='light gray',
                     command=lambda: calk.billentyu("*"),
                     height=1,
                     width=7)
    szorzas.grid(row=4, column=3)

    osztas = Button(gui,
                    text=' ÷ ',
                    fg='black',
                    bg='light gray',
                    command=lambda: calk.billentyu("/"),
                    height=1,
                    width=7)
    osztas.grid(row=5, column=3)

    egyenlo = Button(gui,
                     text=' = ',
                     fg='black',
                     bg='light gray',
                     command=calk.egyenloseg,
                     height=1,
                     width=7)
    egyenlo.grid(row=5, column=2)

    torol = Button(gui,
                   text='C',
                   fg='black',
                   bg='light gray',
                   command=calk.torles,
                   height=1,
                   width=7)
    torol.grid(row=5, column=0)

    kuldes = Button(gui,
                    text='Küldés',
                    fg='black',
                    bg='light gray',
                    command=entry_message,
                    height=1,
                    width=7)
    kuldes.grid(row=8, columnspan=4)

    # GUI indítása
    gui.mainloop()
