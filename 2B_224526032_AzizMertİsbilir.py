from bs4 import BeautifulSoup
import requests

from tkinter import*
from tkinter import ttk

def kuru_bul():

    MIKTAR = ent_miktar.get()
    cevrilecek_kur = cevrilecek_kursec.get()
    kur = cmb_kursec.get()
    
    sayfa = f"https://valuta.exchange/{kur}-to-{cevrilecek_kur}?amount={MIKTAR}"
    data = requests.get(sayfa)
    soup = BeautifulSoup(data.text, 'html.parser')
    veri = soup.find_all(lambda tag: tag.name == "input" and "aria-label" in tag.attrs)[1]
    lbl_hesap_sonucu.configure(text=veri["value"])

anaform = Tk()
anaform.geometry("500x500")

lbl_tlmiktar = Label(
    anaform,
    text="Kur Sec :",
    font=("Helvetica 20 bold italic"))

ent_miktar = Entry(anaform)
lbl_kursec = Label(anaform,
                   text="Cevrilecek Kur Seçiniz")

cmb_kursec= ttk.Combobox(anaform,
                         values=["USD", "EUR", "TRY",])
cevrilecek_kursec = ttk.Combobox(anaform,values=["USD","EUR","TRY"])
lbl_sonuc = Label(anaform,
                  text="Sonuç:")
lbl_hesap_sonucu = Label(anaform,
                         text=".........")
btn_1 = Button(anaform,text="BTN1")
btn_hesapla = ttk.Button(anaform,text="Hesapla",command=kuru_bul)
"""lbl_tlmiktar.pack(expand=YES)
ent_miktar.pack(expand=YES)"""

    
lbl_tlmiktar.grid(row=0, column=0)
lbl_sonuc.grid(row=2, column=0)
ent_miktar.grid(row=0, column=1)
lbl_kursec.grid(row=1,column=0)
cevrilecek_kursec.grid(row=1,column=1)
btn_1.grid(row=3, column=0)
cmb_kursec.grid(row=0, column=2)
lbl_hesap_sonucu.grid(row=2, column=1)
btn_hesapla.grid(row=3,column=1)
anaform.mainloop()

