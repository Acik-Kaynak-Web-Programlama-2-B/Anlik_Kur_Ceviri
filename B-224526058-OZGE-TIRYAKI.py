import tkinter as tk
from tkinter import ttk, StringVar, Label, Entry
import requests
from bs4 import BeautifulSoup


def hesapla():
    link = f"https://valuta.exchange/{kur1.get()}-to-{kur2.get()}?amount={miktar.get()}"
    y = requests.get(link)
    soup = BeautifulSoup(y.text, 'html.parser')
    i = soup.find_all(lambda tag: tag.name =="input" and "aria-label" in tag.attrs)[1]
    sonuc.configure(text="Sonuç : " + i["value"])

pencere = tk.Tk()
pencere.title("Kur Hesaplayıcı")
pencere.geometry("400x250")

Label(pencere, text="Miktarı Giriniz:", width=15).grid(row=1, column=0)
Label(pencere, text="Kuru Seçiniz:", width=15).grid(row=2, column=0)
Label(pencere, text="Dönüştürülecek Kuru Seçiniz :", width=25).grid(row=3, column=0)


miktar = Entry(pencere, font=("Helvetica", 10), width=10)
miktar.grid(row=1, column=1, padx=10, pady=10)  

kur1 = ttk.Combobox(pencere, values=['USD', 'EUR', 'TRY'], width=10)
kur1.grid(row=2, column=1, padx=10, pady=10) 

kur2 = ttk.Combobox(pencere, values=['USD', 'EUR', 'TRY'], width=10)
kur2.grid(row=3, column=1, padx=10, pady=10)  

button= ttk.Button(pencere, text="Hesapla", command=hesapla)
button.grid(row=4, column=1, padx="10", pady="15")

sonuc = Label(pencere, text="", font=("Helvetica", 15))
sonuc.grid(row=5, column=1, padx="10")

pencere.mainloop()
