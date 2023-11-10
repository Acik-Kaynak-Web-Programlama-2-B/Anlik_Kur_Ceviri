from tkinter import *
from bs4 import BeautifulSoup 
import requests
from tkinter import ttk

window = Tk()
window.title("Kur Çevirme")
window.geometry("350x250")
window.configure(background="lightblue")


def hesapla():
        link = f"https://valuta.exchange/{kur1.get()}-to-{kur2.get()}?amount={money_amount.get()}"
        y = requests.get(link)
        soup = BeautifulSoup(y.text, 'html.parser')
        i = soup.find_all(lambda tag: tag.name == "input" and "aria-label" in tag.attrs)[1]
        sonuc.configure(text = "Sonuç : " + i["value"])

kur1 = StringVar()
kur2 = StringVar()
money = StringVar()

miktar = Label(window, text="Miktar: ",font=('Comic Sans MS',10))
miktar.grid(row=0, column=0, padx="10")

money_amount = Entry(window, textvariable = money, font=('Comic Sans MS',10,'normal'))
money_amount.grid(row=0, column=1, padx="10")

kur1sec = ttk.Combobox(window, values=['USD', 'EUR', 'AUD', 'TRY'], textvariable=kur1, state="readonly")
kur1sec.grid(row=1, column=1, padx="10")

sec = Label(window, text="Girilen kuru seç: ",font=('Comic Sans MS',10))
sec.grid(row=1, column=0, padx="10", pady="15")

kur2sec = ttk.Combobox(window, values=['USD', 'EUR', 'AUD', 'TRY'], textvariable=kur2, state="readonly")
kur2sec.grid(row=2, column=1, padx="10")

sec = Label(window, text="Dönüştürelecek kuru seç: ",font=('Comic Sans MS',10))
sec.grid(row=2, column=0, padx="10", pady="15")

btn_hesap = ttk.Button(window, text="Hesapla", command=hesapla)
btn_hesap.grid(row=4, column=1, padx="10", pady="15")

label1 = Label(window, text="Dönüştürülmüş paranız --> ",font=('Comic Sans MS',10))
label1.grid(row=3, column=0)

sonuc = Label(window, text="",font=('Comic Sans MS',15))
sonuc.grid(row=3, column=1, padx="10")

window.mainloop()