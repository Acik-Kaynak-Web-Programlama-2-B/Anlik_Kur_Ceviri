from tkinter import * 
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

anaform = Tk()
anaform.geometry("450x450")

def hesapla():
    kur = cmb_kursec.get()
    cevrilecek_kur = cevrilecek_kursec.get()
    miktar = ent_miktar.get()
    link = f"https://valuta.exchange/{kur}-to-{cevrilecek_kur}?amount={miktar}"
    y = requests.get(link)
    soup = BeautifulSoup(y.text, 'html.parser')
    i = soup.find_all(lambda tag: tag.name == "input" and "aria-label" in tag.attrs)[1]
    lbl_hesap_sonuc.configure(text=i["value"])


lbl_tlmiktar = Label(
    anaform,
    text="Kur Seçiniz :",
    font="Arial 20 bold italic",
    fg="red",bg="white")

ent_miktar = Entry()

lbl_kursec = Label(anaform,
    text="Çevrilecek Kur Seçiniz :",
    font="Arial 20 bold",
    fg="red",bg="white")


cevrilecek_kursec = ttk.Combobox(anaform,
                          values=["USD","EUR","TRY"])
cmb_kursec = ttk.Combobox(anaform,
                            values=["USD","EUR","TRY"])

lbl_sonuc = Label(anaform,
                  text="SONUÇ: ",font="Arial 15 bold",bg="white")

lbl_hesap_sonuc = Label(anaform,
                        text="....")


btn_hesapla = ttk.Button(anaform,
                         text="HESAPLA",command=hesapla)

lbl_tlmiktar.grid(row=0,column=0)
ent_miktar.grid(row=0,column=1)
lbl_kursec.grid(row=1,column=0)
cevrilecek_kursec.grid(row=1,column=1)
cmb_kursec.grid(row=0,column=2)
lbl_sonuc.grid(row=2,column=0)
lbl_hesap_sonuc.grid(row=2,column=1)
btn_hesapla.grid( row=3 , column=1)

anaform.mainloop()
