# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 22:44:11 2023

@author: xd
"""
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

anaform = Tk()
anaform.geometry("600x200")
anaform.title("Kur Hesaplayıcı")

def get_currency(url, class_name):
    yanit = requests.get(url)
    soup = BeautifulSoup(yanit.content, "html.parser")
    para_birimi = soup.find("div", class_=class_name).text.strip()
    a = para_birimi.replace(",", ".")
    return round(float(a), 2)

url_usd = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
usd = get_currency(url_usd, "YMlKec fxKbKc")

url_euro = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"
euro = get_currency(url_euro, "YMlKec fxKbKc")

url_yen = "https://www.google.com/finance/quote/TRY-JPY?hl=tr"
yen = get_currency(url_yen, "YMlKec fxKbKc")

def hesapla():
    lbl_girilenm_val = float(ent_miktar.get())
    secilen_kur1 = cmb_kursecme.get()
    secilen_kur2 = cmb_kursecme1.get()

    if secilen_kur1 == "TL":
        if secilen_kur2 == "USD":
            sonuc = lbl_girilenm_val / usd
            lbl_sonuc.config(text=f"{sonuc:.2f} dolar")
        elif secilen_kur2 == "Euro":
            sonuc = lbl_girilenm_val / euro
            lbl_sonuc.config(text=f"{sonuc:.2f} euro")
        elif secilen_kur2 == "Yen":
            sonuc = lbl_girilenm_val / yen
            lbl_sonuc.config(text=f"{sonuc:.2f} yen")
        else:
            sonuc = lbl_girilenm_val
            lbl_sonuc.config(text=f"{sonuc:.2f} TL")

    elif secilen_kur1 == "USD":
        if secilen_kur2 == "Euro":
            sonuc = lbl_girilenm_val * usd / euro
            lbl_sonuc.config(text=f"{sonuc:.2f} euro")
        elif secilen_kur2 == "Yen":
            sonuc = lbl_girilenm_val * usd / yen
            lbl_sonuc.config(text=f"{sonuc:.2f} yen")
        elif secilen_kur2 == "USD":
            sonuc = lbl_girilenm_val
            lbl_sonuc.config(text=f"{sonuc:.2f} dolar")
        elif secilen_kur2 == "TL":
            sonuc = lbl_girilenm_val * usd
            lbl_sonuc.config(text=f"{sonuc:.2f} TL")

    elif secilen_kur1 == "Euro":
        if secilen_kur2 == "USD":
            sonuc = lbl_girilenm_val * euro / usd
            lbl_sonuc.config(text=f"{sonuc:.2f} dolar")
        elif secilen_kur2 == "Yen":
            sonuc = lbl_girilenm_val * euro / yen
            lbl_sonuc.config(text=f"{sonuc:.2f} yen")
        elif secilen_kur2 == "Euro":
            sonuc = lbl_girilenm_val
            lbl_sonuc.config(text=f"{sonuc:.2f} euro")
        elif secilen_kur2 == "TL":
            sonuc = lbl_girilenm_val * euro
            lbl_sonuc.config(text=f"{sonuc:.2f} TL")

    elif secilen_kur1 == "Yen":
        if secilen_kur2 == "USD":
            sonuc = lbl_girilenm_val * yen / usd
            lbl_sonuc.config(text=f"{sonuc:.2f} dolar")
        elif secilen_kur2 == "Euro":
            sonuc = lbl_girilenm_val * yen / euro
            lbl_sonuc.config(text=f"{sonuc:.2f} euro")
        elif secilen_kur2 == "Yen":
            sonuc = lbl_girilenm_val
            lbl_sonuc.config(text=f"{sonuc:.2f} yen")
        elif secilen_kur2 == "TL":
            sonuc = lbl_girilenm_val * yen
            lbl_sonuc.config(text=f"{sonuc:.2f} TL")


lbl_girilenm = ttk.Label(anaform, text="Miktar Giriniz:", font=("Arial", 12))
ent_miktar = ttk.Entry(anaform, width=33)
lbl_kursecme = ttk.Label(anaform, text="Bir Kur Seçiniz", font=("Arial", 12))
cmb_kursecme = ttk.Combobox(anaform, values=["TL", "USD", "Euro", "Yen"], font=("Arial", 12))
lbl_cvrkur = ttk.Label(anaform, text="Çevrilecek Kur:", font=("Arial", 12))
cmb_kursecme1 = ttk.Combobox(anaform, values=["TL", "USD", "Euro", "Yen"], font=("Arial", 12))
lbl_sonuc = ttk.Label(anaform, text="Sonuç:", font=("Arial", 12))
style = ttk.Style()
style.configure("TButton", font=("Arial", 15))
style.configure("TLabel", background="yellow")

btn_hesapla = ttk.Button(anaform, text="Hesapla", command=hesapla, style="TButton")

lbl_girilenm.grid(row=1, column=0)
ent_miktar.grid(row=1, column=1)
lbl_kursecme.grid(row=0, column=3)
cmb_kursecme.grid(row=1, column=3)
lbl_cvrkur.grid(row=2, column=0)
cmb_kursecme1.grid(row=2, column=1)
lbl_sonuc.grid(row=3, column=0)
btn_hesapla.grid(row=3, column=1)

anaform.mainloop()
