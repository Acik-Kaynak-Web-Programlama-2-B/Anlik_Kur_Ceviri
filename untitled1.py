from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

pencere = Tk()
pencere.title("Kur Hesaplayıcı")
pencere.geometry("400x250")
pencere.resizable(width=False, height=False)

def focus_miktar(event):
    miktar.focus_set()

def hesapla_kur():
    try:
        url = requests.get("https://www.doviz.com/").content
        soup = BeautifulSoup(url, "html.parser")
        kur1 = soup.find("span", attrs={"data-socket-key": "USD"}).text.strip()
        kur2 = soup.find("span", attrs={"data-socket-key": "EUR"}).text.strip()

        tl_miktar = float(miktar.get())
        secilen_kur = cmb_kursec.get()

        if secilen_kur == "USD":
            sonuc = tl_miktar / float(kur1.replace(",", "."))
            lbl_hesap_sonuc.config(text=f"{sonuc:.2f} Dolar")
        elif secilen_kur == "EURO":
            sonuc = tl_miktar / float(kur2.replace(",", "."))
            lbl_hesap_sonuc.config(text=f"{sonuc:.2f} Euro")
    except Exception as e:
        lbl_hesap_sonuc.config(text="Hata oluştu!")

label6 = Label(text="Miktar:", font="bold")
label6.place(x=30, y=20)

miktar = Entry(width=10, font="bold")
miktar.place(x=100, y=20)
miktar.bind("<Button-1>", focus_miktar)

label7 = Label(text="Kur Seçiniz:", font="bold")
label7.place(x=30, y=50)

cmb_kursec = ttk.Combobox(values=["USD", "EURO"], width=7)
cmb_kursec.place(x=130, y=50)
cmb_kursec.current(0)

btn_hesapla = ttk.Button(text="Hesapla", command=hesapla_kur)
btn_hesapla.place(x=30, y=90)

lbl_hesap_sonuc = Label(text="", font="bold")
lbl_hesap_sonuc.place(x=30, y=130)

miktar.focus_set()  # Bu kod miktar girdi alanına odaklanmayı sağlar

pencere.mainloop()