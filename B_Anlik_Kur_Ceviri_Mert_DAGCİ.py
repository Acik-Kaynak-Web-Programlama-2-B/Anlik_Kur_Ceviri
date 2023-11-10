import tkinter as tk
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup 
import requests
#kütüphaneler


def hesapla():
        link = f"https://valuta.exchange/{kur.get()}-to-{kurSec.get()}?amount={kutu.get()}"
        y = requests.get(link)
        soup = BeautifulSoup(y.text, 'html.parser')
        i = soup.find_all(lambda tag: tag.name == "input" and "aria-label" in tag.attrs)[1]
        sonuc.configure(text = "Sonuç : " + i["value"])
#link verileri

pencere = tk.Tk()
pencere.geometry("490x200")
pencere.title("Canlı Döviz Çevirici")
pencere.configure(background="lightgray")
#arka plan verileri

kurSec = StringVar()
kur = StringVar()
kutu = StringVar()
#değişkenler



lbl_miktar = tk.Label(pencere, text="Miktarı giriniz : ",font=("Helvatica 12 bold italic"))


kutu = Entry(pencere, textvariable = kutu, font = ("Helvatica 10 bold italic"))


kur = ttk.Combobox(pencere, values=["TRY", "USD", "EUR", "JPY", "AZN"])


kurSec = ttk.Combobox(pencere, values=["TRY", "USD", "EUR", "JPY", "AZN"])


cevirileckKur = Label(pencere, text="Çevirilecek Kur : ", font=("Helvatica 12 bold italic"))


btn_hesapla = ttk.Button(pencere, text="Hesapla", command=hesapla)


label = Label(pencere, text="Sonuç : ",font=("Helvatica 12 bold italic"))


sonuc = Label(pencere, text="",font=("Helvatica 12 bold italic"))
#form


lbl_miktar.grid(row=0, column=0, padx="12")
kutu.grid(row=0, column=1, padx="12")
kur.grid(row=0, column=2, padx="12")
kurSec.grid(row=1, column=1, padx="12")
cevirileckKur.grid(row=1, column=0, padx="12", pady="20")
btn_hesapla.grid(row=3, column=1, padx="12", pady="20")
label.grid(row=2, column=0)
sonuc.grid(row=2, column=1, padx="12")
#form özellikler

pencere.mainloop()
