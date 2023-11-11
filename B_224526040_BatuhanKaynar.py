# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:28:14 2023

@author: batuh
"""

from tkinter import *
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import requests

def transform():
    link=f"https://valuta.exchange/{exchangeRate.get()}-to-{exchangeRateT.get()}?amount={box_exchangeRate.get()}"
    y = requests.get(link)
    soup = BeautifulSoup(y.text,'html.parser')
    i =soup.find_all(lambda tag: tag.name=="input"and"aria-label"in tag.attrs)[1]
    lbl_calculation.configure(text="Sonuç :"+i["value"])

page=tk.Tk()
page.title("Güncel kur hesaplama")
page.geometry("250x300")

exchangeRate=StringVar()
exchangeRateT=StringVar()
box_exchangeRate_value=StringVar()

lbl_amount=tk.Label(page,text="Miktarı giriniz:",fg="black", font="times 15")
lbl_amount.grid(row=0,column=0)
box_exchangeRate=tk.Entry(textvariable=box_exchangeRate_value)
box_exchangeRate.grid(row=1,column=0)
lbl_pickexchangerate=tk.Label(page,text="Kur seçin:",fg="black", font="times 15" )
lbl_pickexchangerate.grid(row=2,column=0)
cmb_exchangeRate=ttk.Combobox(page,values=["USD","TRY","EUR"])
cmb_exchangeRate.grid(row=3,column=0)
lbl_exchangeRateT=tk.Label(page,text="Dönüştürülecek kuru seçin:",fg="black", font="times 15")
lbl_exchangeRateT.grid(row=4,column=0)
cmb_exchangeRateT=ttk.Combobox(page,values=["USD","TRY","EUR"])
cmb_exchangeRateT.grid(row=5,column=0)
lbl_result=tk.Label(page,text="Sonuç:",fg="black", font="times 15")
lbl_result.grid(row=6,column=0)
lbl_calculation=tk.Label(page,text="",fg="black", font="times 15")
lbl_calculation.grid(row=7,column=0)
btn=ttk.Button(page,text="Sonuç", command=transform)
btn.grid(row=8,column=0)




page.mainloop()