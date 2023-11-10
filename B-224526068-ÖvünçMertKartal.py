from tkinter import *
from tkinter import ttk
import requests

API_KEY = '3850c4deef802a82010ca7ed'
BASE_URL = 'https://open.er-api.com/v6/latest/'

def kurlaricek():
    try:
        # API'den döviz kurlarını al
        response_try = requests.get(BASE_URL + 'TRY')
        response_usd = requests.get(BASE_URL + 'USD')
        response_eur = requests.get(BASE_URL + 'EUR')
        response_gbp = requests.get(BASE_URL + 'GBP')
        response_jpy = requests.get(BASE_URL + 'JPY')
        response_cad = requests.get(BASE_URL + 'CAD')
        response_aud = requests.get(BASE_URL + 'AUD')
        response_chf = requests.get(BASE_URL + 'CHF')
        response_inr = requests.get(BASE_URL + 'INR')
        response_brl = requests.get(BASE_URL + 'BRL')
        response_rub = requests.get(BASE_URL + 'RUB')
        response_mxn = requests.get(BASE_URL + 'MXN')
        response_cny = requests.get(BASE_URL + 'CNY')
        response_krw = requests.get(BASE_URL + 'KRW')
        response_sek = requests.get(BASE_URL + 'SEK')
        response_nzd = requests.get(BASE_URL + 'NZD')

        # JSON verilerini çözümle (veriyapısına dönüştür.)
        data_try = response_try.json()
        data_usd = response_usd.json()
        data_eur = response_eur.json()
        data_gbp = response_gbp.json()
        data_jpy = response_jpy.json()
        data_cad = response_cad.json()
        data_aud = response_aud.json()
        data_chf = response_chf.json()
        data_inr = response_inr.json()
        data_brl = response_brl.json()
        data_rub = response_rub.json()
        data_mxn = response_mxn.json()
        data_cny = response_cny.json()
        data_krw = response_krw.json()
        data_sek = response_sek.json()
        data_nzd = response_nzd.json()

        # TRY, USD, EUR, GBP, JPY, CAD, AUD, CHF, INR, BRL, RUB, MXN, CNY, KRW, SEK, NZD kurlarını al
        roundedtry = 1 / data_try['rates']['TRY']
        roundeddolar = 1 / data_usd['rates']['TRY']
        roundedeuro = 1 / data_eur['rates']['TRY']
        roundedgbp = 1 / data_gbp['rates']['TRY']
        roundedjpy = 1 / data_jpy['rates']['TRY']
        roundedcad = 1 / data_cad['rates']['TRY']
        roundedaud = 1 / data_aud['rates']['TRY']
        roundedchf = 1 / data_chf['rates']['TRY']
        roundedinr = 1 / data_inr['rates']['TRY']
        roundedbrl = 1 / data_brl['rates']['TRY']
        roundedrub = 1 / data_rub['rates']['TRY']
        roundedmxn = 1 / data_mxn['rates']['TRY']
        roundedcny = 1 / data_cny['rates']['TRY']
        roundedkrw = 1 / data_krw['rates']['TRY']
        roundedsek = 1 / data_sek['rates']['TRY']
        roundednzd = 1 / data_nzd['rates']['TRY']

        return roundedtry, roundeddolar, roundedeuro, roundedgbp, roundedjpy, roundedcad, roundedaud, roundedchf, roundedinr, roundedbrl, roundedrub, roundedmxn, roundedcny, roundedkrw, roundedsek, roundednzd

    except requests.RequestException as e:
        print(f"Error retrieving exchange rates: {e}")
        return tuple([0] * 16)

def hesapla(*args):
    try:
        # Girdi al
        miktar = float(e_miktar_giris.get())
        giris_kur = cmb_giriskur.get()
        cikis_kur = cmb_cikiskur.get()

        # Hesaplamadan önce döviz kurlarını güncelle
        global kurlar
        kurlar = kurlaricek()

        # Giriş ve çıkış kurlarını belirle
        giris_kur_degeri = kurlar[kur_listesi.index(giris_kur)]
        cikis_kur_degeri = kurlar[kur_listesi.index(cikis_kur)]

        # Çıkış miktarını hesapla ve sonucu göster
        sonuc = miktar * (cikis_kur_degeri / giris_kur_degeri)
        lbl_sonuc.config(text=f"Girilen Miktar: {miktar} {giris_kur}, {cikis_kur} karşılığı {sonuc:.2f} {cikis_kur}")
    except ValueError:
        lbl_sonuc.config(text="Geçersiz miktar!")

def otomatik_döviz_kurlarını_güncelle():
    # Döviz kurlarını otomatik olarak güncelle
    global kurlar
    kurlar = kurlaricek()

    # Her 60000 milisaniye (1 dakika) sonra tekrar et
    anaform.after(60000, otomatik_döviz_kurlarını_güncelle)

# Ana form oluştur
anaform = Tk()
anaform.title("Kur Hesapla")
anaform.geometry("300x200")

# Arayüz elemanlarını oluştur
lbl_miktar = Label(anaform, text="Miktarı Yazınız:" ,bg="orange")
lbl_giriskur = ttk.Label(anaform, text="Giriş Kur:" ,background="orange")
lbl_cikiskur = ttk.Label(anaform, text="Çıkış Kur:" ,background="orange")
lbl_sonuc = ttk.Label(anaform, text="Sonuç:" ,background="#FFD700")

kur_listesi = ["TRY", "USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "INR", "BRL", "RUB", "MXN", "CNY", "KRW", "SEK", "NZD"]

cmb_giriskur = ttk.Combobox(anaform, values=kur_listesi)
cmb_cikiskur = ttk.Combobox(anaform, values=kur_listesi)
e_miktar_giris = ttk.Entry(anaform)

# Elemanları grid'e yerleştir
lbl_miktar.grid(row=0, column=0)
e_miktar_giris.grid(row=0, column=1, padx=20)
lbl_giriskur.grid(row=1, column=0, pady=20)
cmb_giriskur.grid(row=1, column=1, padx=20)
lbl_cikiskur.grid(row=2, column=0, pady=20)
cmb_cikiskur.grid(row=2, column=1, padx=20)
lbl_sonuc.grid(row=3, column=0, columnspan=2)

# Kurları ilk defa güncelle
kurlar = kurlaricek()

# Otomatik döviz kuru güncellemeyi başlat
otomatik_döviz_kurlarını_güncelle()

# Her değer değiştiğinde hesapla fonksiyonunu çağır
e_miktar_giris.bind("<KeyRelease>", hesapla)
cmb_giriskur.bind("<<ComboboxSelected>>", hesapla)
cmb_cikiskur.bind("<<ComboboxSelected>>", hesapla)

# Arkaplan rengini mavi olarak ayarla
anaform.configure(bg="lightblue")

# Main loop'u başlat
anaform.mainloop()
