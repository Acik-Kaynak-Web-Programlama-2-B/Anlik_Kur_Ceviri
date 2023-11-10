import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

def get_currency(url, class_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    currency = soup.find("div", class_=class_name).text.strip()
    a = currency.replace(",", ".")
    return round(float(a))

url_usd = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
url_euro = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"

rounded_dolar = get_currency(url_usd, "YMlKec fxKbKc")
rounded_euro = get_currency(url_euro, "YMlKec fxKbKc")


def hesapla():
    tl_miktar = float(ent_miktar.get())
    secilen_kur = cmb_kursec.get()
    secilen_doviz = cmb_dovizsec.get()
    if secilen_doviz == "TL":
        if secilen_kur == "USD":
            sonuc = tl_miktar / rounded_dolar
            lbl_hesap_sonuc.config(text=f"{sonuc:.2f} dolar")
        else:
            secilen_kur == "EURO"
            sonuc = tl_miktar / rounded_euro
            lbl_hesap_sonuc.config(text=f"{sonuc:.2f} euro")
    if secilen_doviz == "USD":
        if secilen_kur == "EURO":
            sonuc = tl_miktar * rounded_dolar / rounded_euro
            lbl_hesap_sonuc.config(text=f"{sonuc:.2f} euro")
    if secilen_doviz == "USD":
       if secilen_kur == "USD":
           sonuc = tl_miktar
           lbl_hesap_sonuc.config(text=f"{sonuc:.2f} dolar")
    if secilen_doviz == "EURO":
       if secilen_kur == "USD":
           sonuc = tl_miktar * rounded_euro / rounded_dolar
           lbl_hesap_sonuc.config(text=f"{sonuc:.2f} dolar")
    if secilen_doviz == "EURO":
        if secilen_kur == "EURO":
         sonuc = tl_miktar
         lbl_hesap_sonuc.config(text=f"{sonuc:.2f} euro")
        
   
anaform = tk.Tk()
anaform.geometry("500x500")
anaform.title("Döviz Çevirici")
anaform.configure(bg='purple')  

lbl_tlmiktar = tk.Label(
    anaform,
    text="Miktar Giriniz ",
    font=("Helvetica 10 bold italic"),
    bg='purple',  
    fg='white'  
)

ent_miktar = tk.Entry()

lbl_kursec = tk.Label(
    anaform,
    text="Döviz Kuru Seçiniz",
    font=("Helvetica 10 bold italic"),
    bg='purple',  
    fg='white'  
)

cmb_kursec = ttk.Combobox(anaform, values=["USD", "EURO"])
cmb_dovizsec = ttk.Combobox(anaform, values=["USD","EURO","TL"])
lbl_sonuc = tk.Label(anaform, text="Sonuç: ", font=("Helvetica 10 bold italic"), bg='purple', fg='white')
lbl_hesap_sonuc = tk.Label(anaform, text="...", bg='purple', fg='white')

btn_hesapla = ttk.Button(anaform, text="Hesapla", command=hesapla)

lbl_tlmiktar.grid(row=0, column=0)
ent_miktar.grid(row=0, column=1)
lbl_kursec.grid(row=1, column=0)
cmb_kursec.grid(row=1, column=1)
lbl_sonuc.grid(row=2, column=0)
lbl_hesap_sonuc.grid(row=2, column=1)
btn_hesapla.grid(row=3, column=1)
cmb_dovizsec.grid(row=0, column=3)
anaform.mainloop()
