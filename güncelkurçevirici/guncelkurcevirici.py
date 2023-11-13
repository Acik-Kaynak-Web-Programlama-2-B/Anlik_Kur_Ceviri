
"""
Spyder Editor

This is a temporary script file.
"""
import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

class CurrencyConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()

       
        self.title("Kur Çevirici")
        self.geometry("500x300")
        self.configure(bg="#666666") 

       
        style = ttk.Style()
        self.configure(bg="#87CECB") 
        style.configure("TLabel", font=("Arial", 12), background="#4F94CD", foreground="#FF0000")
        style.configure("TEntry", font=("Arial", 12), fieldbackground="#ffffff", borderwidth=2, relief="solid") 
        style.configure("TButton", font=("Arial", 12), background="#FF6666", foreground="black", borderwidth=0, relief="flat")
        style.configure("TButton.TButton", foreground="red") 

        self.from_currency_label = ttk.Label(self, text="Dönüştürülecek Kur:")
        self.from_currency_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.from_currency_var = tk.StringVar()
        self.from_currency_combobox = ttk.Combobox(self, textvariable=self.from_currency_var,
                                                   values=["USD", "EUR", "TRY"])
        self.from_currency_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.to_currency_label = ttk.Label(self, text="Dönüştürülen Kur:")
        self.to_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.to_currency_var = tk.StringVar()
        self.to_currency_combobox = ttk.Combobox(self, textvariable=self.to_currency_var,
                                                 values=["USD", "EUR", "TRY"])
        self.to_currency_combobox.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.amount_label = ttk.Label(self, text="Miktar:")
        self.amount_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.amount_entry = ttk.Entry(self)
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.result_label = ttk.Label(self, text="Sonuç:")
        self.result_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.result_var = tk.StringVar()
        self.result_entry = ttk.Entry(self, state="readonly", textvariable=self.result_var)
        self.result_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

      
        self.cevir_button = ttk.Button(self, text="Çevir", command=self.convert)
        self.cevir_button.grid(row=5, column=0, columnspan=2, pady=10)

      
        style.configure("TButton.TButton", foreground="black")

    def get_currency(self, url, class_name):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            currency_value = soup.find("div", class_=class_name).text.strip()
            formatted_value = currency_value.replace(",", ".")
            return round(float(formatted_value), 2)
        except Exception as e:
            print(f"Hata: {e}")
            return None

    def get_exchange_rate(self, from_currency, to_currency):
        try:
            url = f"https://www.google.com/finance/quote/{from_currency}-{to_currency}?hl=tr"
            return self.get_currency(url, "YMlKec fxKbKc")
        except Exception as e:
            print(f"Hata: {e}")
            return None

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            exchange_rate = self.get_exchange_rate(from_currency, to_currency)

            if exchange_rate is not None:
                result = amount * exchange_rate
                self.result_var.set(result)
            else:
                self.result_var.set("Geçersiz kurlar!")
        except ValueError:
            self.result_var.set("Geçersiz miktar!")

if __name__ == "__main__":
    app = CurrencyConverterApp()
    app.mainloop()
