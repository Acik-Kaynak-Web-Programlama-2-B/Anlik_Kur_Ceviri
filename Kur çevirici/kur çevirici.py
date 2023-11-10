# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 23:49:45 2023

@author: sentu
"""

import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk

def doviz_kurlarini_al_dovizcom():
    try:
        url = "https://www.doviz.com/"
        cevap = requests.get(url)
        soup = BeautifulSoup(cevap.content, "html.parser")
        doviz_kurlari = {}

        for row in soup.select("tbody tr"):
            columns = row.find_all("td")
            para_birimi = columns[0].get_text(strip=True)
            kur = columns[3].get_text(strip=True)
            doviz_kurlari[para_birimi] = float(kur.replace(",", "."))

        return doviz_kurlari
    except Exception as hata:
        print(f"Hata: {str(hata)}")
        return {}

def doviz_kurlarini_al_google():
    try:
        doviz_kurlari = {}
        for para_birimi in ["USD", "EUR", "CNY"]:
            url = f"https://www.google.com/finance/quote/{para_birimi}-TRY?hl=tr"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            exchange_rate_element = soup.find("div", class_="YMlKec fxKbKc")
            if exchange_rate_element:
                exchange_rate = exchange_rate_element.text.strip()
                doviz_kurlari[para_birimi] = float(exchange_rate.replace(",", "."))
            else:
                doviz_kurlari[para_birimi] = 0.0  # Veya başka bir varsayılan değer
        return doviz_kurlari
    except Exception as e:
        print(f"Hata: {str(e)}")
        return {}

def doviz_hesapla():
    miktar = float(giris_miktar.get())
    secilen_doviz = cmb_doviz_sec.get()

    doviz_kurlari_dovizcom = doviz_kurlarini_al_dovizcom()
    doviz_kurlari_google = doviz_kurlarini_al_google()

    if secilen_doviz in doviz_kurlari_dovizcom and secilen_doviz in doviz_kurlari_google:
        kurlarin_ortalamasi = (doviz_kurlari_dovizcom[secilen_doviz] + doviz_kurlari_google[secilen_doviz]) / 2
        sonuc = miktar * kurlarin_ortalamasi
        lbl_hesap_sonucu.config(text=f"{sonuc:.2f} TRY")
    else:
        lbl_hesap_sonucu.config(text="Geçersiz Döviz")

anaform = Tk()
anaform.geometry("400x600")
anaform.title("Döviz Çevirici")

lbl_tlmiktar = Label(
    anaform,
    text="TL Miktarı:",
    font=("Verdana 20 bold italic"))

giris_miktar = Entry(anaform)
lbl_doviz_sec = Label(anaform,
                   text="Döviz Seçiniz")
cmb_doviz_sec = ttk.Combobox(anaform,
                          values=["USD", "EUR", "CNY"])
lbl_sonuc = Label(anaform,
                  text="Sonuç:")

lbl_hesap_sonucu = Label(anaform,
                         text="...")

btn_hesapla = ttk.Button(anaform,
                         text="Hesapla",
                         command=doviz_hesapla)

lbl_tlmiktar.grid(row=0, column=0)
giris_miktar.grid(row=0, column=1)

lbl_doviz_sec.grid(row=1, column=0)
cmb_doviz_sec.grid(row=1, column=1)

btn_hesapla.grid(row=3, column=0, columnspan=2)

lbl_sonuc.grid(row=2, column=0)
lbl_hesap_sonucu.grid(row=2, column=1)

anaform.mainloop()
