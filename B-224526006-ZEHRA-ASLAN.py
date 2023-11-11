from tkinter import *

import tkinter as tk

from tkinter import ttk

from bs4 import BeautifulSoup
import requests



def ceviri():
    link=f"https://valuta.exchange/{cmb_ac.get()}-to-{cmb_cevrilecekAc.get()}?amount={box_kur.get()}"
   
    y = requests.get(link)

    soup =BeautifulSoup(y.text,'html.parser')
 
    i =soup.find_all(lambda tag: tag.name=="input"and"aria-label"in tag.attrs)[1]
  
    lbl_veri.configure(text="Sonuç :"+i["value"])



sayfa=tk.Tk()

sayfa.title("Güncel kur hesaplama")

sayfa.geometry("300x200")



cmb_ac=StringVar()

cmb_cevrilecekAc=StringVar()

box_kur=StringVar()


lbl_adet=tk.Label(sayfa,text="Hesap yapılcak miktarı giriniz:",font=("Verdana 10 bold"))

lbl_adet.grid(row=0,column=0)
box_kur=tk.Entry()

box_kur.grid(row=1,column=0)

lbl_kurtikla=tk.Label(sayfa,text="Kur seçin:",font=("Verdana 10 bold"))

lbl_kurtikla.grid(row=2,column=0)

cmb_ac=ttk.Combobox(sayfa,values=["USD","TRY","EUR","KWD","AZN"])

cmb_ac.grid(row=3,column=0)

lbl_cevrilecekAc=tk.Label(sayfa,text="İşlem görecek kuru seçin:",font=("Verdana 10 bold"))
lbl_cevrilecekAc.grid(row=4,column=0)

cmb_cevrilecekAc=ttk.Combobox(sayfa,values=["USD","TRY","EUR","KWD","AZN"])

cmb_cevrilecekAc.grid(row=5,column=0)

lbl_cikti=tk.Label(sayfa,text="Sonuç:",font=("Verdana 10 bold"))

lbl_cikti.grid(row=6,column=0)
lbl_veri=tk.Label(sayfa,text="",
font=("Verdana 10 bold"))
lbl_veri.grid(row=7,column=0)

btn=ttk.Button(sayfa,text="Sonuç", command=ceviri)

btn.grid(row=8,column=0)





sayfa.mainloop()