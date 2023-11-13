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
    dönüşecek_kur = cmb_dönüşecek_kur.get()
    dönüştürülecek_kur = cmb_dönüştürülecek_kur.get()

    if dönüşecek_kur == "TL":
        if dönüştürülecek_kur == "USD":
            sonuc = tl_miktar / rounded_dolar
            lbl_hesap_sonuc.config(text=f"{sonuc:.2f} dolar")
        elif dönüştürülecek_kur == "EURO":
            sonuc = tl_miktar / rounded_euro
            lbl_hesap_sonuc.config(text=f"{sonuc:.2f} euro")
    elif dönüşecek_kur == "USD":
        if dönüştürülecek_kur == "EURO":
            sonuc = tl_miktar * rounded_dolar / rounded_euro
            lbl_hesap_sonuc.config(text=f"{sonuc:.2f} euro")
        elif dönüştürülecek_kur == "USD":
            sonuc = tl_miktar
            lbl_hesap_sonuc.config(text=f"{sonuc:.2f} dolar")
    elif dönüşecek_kur == "EURO":
        if dönüştürülecek_kur == "USD":
            sonuc = tl_miktar * rounded_euro / rounded_dolar
            lbl_hesap_sonuc.config(text=f"{sonuc:.2f} dolar")
        elif dönüştürülecek_kur == "EURO":
            sonuc = tl_miktar
            lbl_hesap_sonuc.config(text=f"{sonuc:.2f} euro")

anaform = tk.Tk()
anaform.geometry("500x500")
anaform.title("Döviz Çevirici")
anaform.configure(bg='black')

lbl_tlmiktar = tk.Label(
    anaform,
    text="Miktar Giriniz ",
    font=("Helvetica 10 bold italic"),
    bg='black',
    fg='white'
)

ent_miktar = tk.Entry()

lbl_dönüşecek_kur = tk.Label(
    anaform,
    text="Dönüşecek Kur",
    font=("Helvetica 10 bold italic"),
    bg='black',
    fg='white'
)

cmb_dönüşecek_kur = ttk.Combobox(anaform, values=["USD", "EURO", "TL"])
cmb_dönüşecek_kur.set("TL")

lbl_dönüştürülecek_kur = tk.Label(
    anaform,
    text="Dönüştürülecek Kur",
    font=("Helvetica 10 bold italic"),
    bg='black',
    fg='white'
)

cmb_dönüştürülecek_kur = ttk.Combobox(anaform, values=["USD", "EURO", "TL"])
cmb_dönüştürülecek_kur.set("USD")

lbl_sonuc = tk.Label(anaform, text="Sonuç: ", font=("Helvetica 10 bold italic"), bg='black', fg='white')
lbl_hesap_sonuc = tk.Label(anaform, text="...", bg='black', fg='white')

btn_hesapla = ttk.Button(anaform, text="Hesapla", command=hesapla)

lbl_tlmiktar.grid(row=0, column=0)
ent_miktar.grid(row=0, column=1)
lbl_dönüşecek_kur.grid(row=1, column=0)
cmb_dönüşecek_kur.grid(row=1, column=1)
lbl_dönüştürülecek_kur.grid(row=2, column=0)
cmb_dönüştürülecek_kur.grid(row=2, column=1)
lbl_sonuc.grid(row=3, column=0)
lbl_hesap_sonuc.grid(row=3, column=1)
btn_hesapla.grid(row=4, column=1)

anaform.mainloop()
