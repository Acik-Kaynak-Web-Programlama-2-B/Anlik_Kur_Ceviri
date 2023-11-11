# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 23:07:54 2023

@author: gulci
"""


from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

def hesapla():
    link = f"https://valuta.exchange/try-to-{cmb_kursec.get()}?amount={ent_miktar.get()}"
    dönen_sayfa = requests.get(link)
    soup = BeautifulSoup(dönen_sayfa.text, 'html.parser')
    sonuç = çorba.find_all(lambda tag: tag.name == "input" and "aria-label" in tag.attrs)[1]
    lbl_hesap_sonucu.config(text="Sonuç: " + sonuç["value"])

bilgisayar = Tk()
bilgisayar.geometry("400x600")

lbl_tlmiktar = Label(
    bilgisayar,
    text="MİKTAR:",
    font=("Helvetica", 20, "bold")
)

pr_miktar = Entry(bilgisayar)

lbl_kursec = Label(bilgisayar,
                   text="Kur Seçiniz:",
                   font=("Helvetica", 20, "bold"))
cmb_kursec = ttk.Combobox(bilgisayar,
                          values=["USD", "EUR"])

lbl_sonuc = Label(bilgisayar,
                  text="Sonuç:",
                  font=("Helvetica", 20, "bold"))

lbl_hesap_sonucu = Label(bilgisayar,
                         text="..........."
                         )

btn_1 = Button(bilgisayar,
               text="BTN1",
               font=("Helvetica", 10, "bold"))

btn_hesapla = ttk.Button(bilgisayar,
                         text="Hesapla", command=hesapla)

lbl_tlmiktar.grid(row=0, column=0)
pr_miktar.grid(row=0, column=1)
lbl_kursec.grid(row=1, column=0)
cmb_kursec.grid(row=1, column=1)
lbl_sonuc.grid(row=2, column=0)
lbl_hesap_sonucu.grid(row=2, column=1)
btn_1.grid(row=3, column=0)
btn_hesapla.grid(row=3, column=1)

bilgisayar.mainloop()
