from tkinter import *
from tkinter import ttk  
import requests
from bs4 import BeautifulSoup

def hesapla():
    kur = kur_sec.get()
    cevrilecek_kur = cevrilecek_kur_sec.get()
    miktar = ent_miktar.get()

    link = f"https://valuta.exchange/{kur}-to-{cevrilecek_kur}?amount={miktar}"
    veri = requests.get(link)
    soup = BeautifulSoup(veri.text, 'html.parser')
    ayıklanan_veri = soup.find_all(lambda tag: tag.name == "input" and "aria-label" in tag.attrs)[1]
    lbl_hesap_sonucu.configure(text=ayıklanan_veri["value"])
    
pencere = Tk()
pencere.geometry("400x600")

lbl_tlmiktar = Label(
    pencere,
    text="Kur Seçiniz :",
    font=("Helvectia 20 bold"))

lbl_miktar = Label(pencere,text="Miktar :",font=("Helvectia 20 bold"))

ent_miktar = Entry(pencere)
lbl_kursec = Label(pencere, 
                   text="Çevrilecek Kur :",
                   font=("Helvectia 20 bold"))

kur_sec = ttk.Combobox(pencere,
                          values=["USD","EUR","TRY"])

cevrilecek_kur_sec = ttk.Combobox(pencere,
                          values=["USD","EUR","TRY"])

lbl_sonuc = Label(pencere,
                  text="Sonuç :",
                  font=("Helvectia 20 bold"))

lbl_hesap_sonucu = Label(pencere,
                         text="............")


btn_1 = Button(pencere,
               text="BTN1",
               font=("Helvectia 10 bold"))

btn_hesapla = ttk.Button(pencere,
                         text="Hesapla",command=hesapla)

"""lbl_tlmiktar.pack(expand=TRUE)
ent_miktar.pack(expand=TRUE)"""


kur_sec.grid(row=0,column=1)
lbl_tlmiktar.grid(row=0,column=0)
lbl_miktar.grid(row=1,column=0)
ent_miktar.grid(row=1,column=1)
lbl_kursec.grid(row=2,column=0)
cevrilecek_kur_sec.grid(row=2,column=1)
lbl_sonuc.grid(row=3,column=0)
lbl_hesap_sonucu.grid(row=3,column=1)
btn_1.grid(row=4,column=0)
btn_hesapla.grid(row=4,column=1)

pencere.mainloop()