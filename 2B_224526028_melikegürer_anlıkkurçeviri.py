from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

def get_exchange_rate():
    amount = float(kt_miktar.get())
    base_currency = dvz_kursec.get()
    target_currency = dvz_cvrkur.get()

    if base_currency == target_currency:
        result = amount
    else:
        url = f"https://www.google.com/search?q=1{base_currency}+to+{target_currency}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        conversion_rate = soup.find("span", class_="DFlfde SwHCTb").text
        result = amount * float(conversion_rate.replace(",", ""))
    
    kt_sonuc.delete(0, END)
    kt_sonuc.insert(0, round(result, 2))

pencere = Tk()
pencere.geometry("500x200")

lbl_miktar = Label(pencere, text="Miktar:")
kt_miktar = Entry()

lbl_kursec = Label(pencere, text="Kur Seç")
dvz_kursec = ttk.Combobox(pencere, values=["USD", "EUR", "TRY", "JPY"])

lbl_cvrkur = Label(pencere, text="Çevirilecek Kur")
dvz_cvrkur = ttk.Combobox(pencere, values=["USD", "EUR", "TRY", "JPY"])

lbl_sonuc = Label(pencere, text="Sonuç:")
kt_sonuc = Entry()

btn_hesapla = ttk.Button(pencere, text="Hesapla", command=get_exchange_rate)

lbl_miktar.grid(row=0, column=0)
kt_miktar.grid(row=0, column=1)
lbl_kursec.grid(row=0, column=2)
dvz_kursec.grid(row=0, column=3)
lbl_cvrkur.grid(row=2, column=0)
dvz_cvrkur.grid(row=2, column=1)
lbl_sonuc.grid(row=3, column=0)
kt_sonuc.grid(row=3, column=1)
btn_hesapla.grid(row=4, column=1)

pencere.mainloop()
