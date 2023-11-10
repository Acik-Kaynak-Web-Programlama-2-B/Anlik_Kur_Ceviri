# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:41:45 2023

@author: C-117
"""
from tkinter import *
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

def ceviri():
    link=f"https://valuta.exchange/{cmb_kur.get()}-to-{cmb_cevrilecekKur.get()}?amount={box_kur.get()}"
    y = requests.get(link)
    soup = BeautifulSoup(y.text,'html.parser')
    i =soup.find_all(lambda tag: tag.name=="input"and"aria-label"in tag.attrs)[1]
    lbl_hesap.configure(text="Sonuç :"+i["value"])

sayfa=tk.Tk()
sayfa.title("Güncel kur hesaplama")
sayfa.geometry("300x200")

cmb_kur=StringVar()
cmb_cevrilecekKur=StringVar()
box_kur=StringVar()

lbl_miktar=tk.Label(sayfa,text="Hesap yapılcak miktarı giriniz:",font=("Verdana 10 bold"))
lbl_miktar.grid(row=0,column=0)
box_kur=tk.Entry()
box_kur.grid(row=1,column=0)
lbl_kursec=tk.Label(sayfa,text="Kur seçin:",font=("Verdana 10 bold"))
lbl_kursec.grid(row=2,column=0)
cmb_kur=ttk.Combobox(sayfa,values=["USD","TRY","EUR","KWD","AZN"])
cmb_kur.grid(row=3,column=0)
lbl_cevrilecekKur=tk.Label(sayfa,text="İşlem görecek kuru seçin:",font=("Verdana 10 bold"))
lbl_cevrilecekKur.grid(row=4,column=0)
cmb_cevrilecekKur=ttk.Combobox(sayfa,values=["USD","TRY","EUR","KWD","AZN"])
cmb_cevrilecekKur.grid(row=5,column=0)
lbl_sonuc=tk.Label(sayfa,text="Sonuç:",font=("Verdana 10 bold"))
lbl_sonuc.grid(row=6,column=0)
lbl_hesap=tk.Label(sayfa,text="",font=("Verdana 10 bold"))
lbl_hesap.grid(row=7,column=0)
btn=ttk.Button(sayfa,text="Sonuç", command=ceviri)
btn.grid(row=8,column=0)




sayfa.mainloop()