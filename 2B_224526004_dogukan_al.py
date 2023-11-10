import customtkinter as ctk
import requests
from bs4 import BeautifulSoup


class App(ctk.CTk):
    def __init__(self):
        super().__init__(
            fg_color="#f1f3f5")
        
        self.geometry("400x400")
        self.title("app")
        self.type_list =["USD","TRY","EUR"]
        
        self.price = ctk.IntVar()
        self.one = ctk.StringVar()
        self.two = ctk.StringVar()
        
        self.setup()
        self.mainloop()
        
    def setup(self):
        self.frame_one = FrameOne(self,self.type_list)
        self.frame_two = FrameTwo(self,self.type_list)
        self.result = ctk.CTkLabel(self,text = "Sonuç:",font = (None,16))
        self.result.pack(expand = True)
        ctk.CTkButton(self,text = "Hesapla",font = (None,16), command = self.hesapla).pack(expand = True)
        
    def hesapla(self):
        link = f"https://valuta.exchange/{self.frame_one.combobox.get()}-to-{self.frame_two.combobox.get()}?amount={self.frame_one.entry.get()}"
        y = requests.get(link)
        soup = BeautifulSoup(y.text, 'html.parser')
        i = soup.find_all(lambda tag: tag.name == "input" and "aria-label" in tag.attrs)[1]
        self.result.configure(text =  self.frame_one.combobox.get() + "-" + self.frame_two.combobox.get() + ":" + i["value"])
        
class FrameOne(ctk.CTkFrame):
    def __init__(self,parent,type_list):
        super().__init__(
            parent,
            fg_color = "#f1f3f5"
        )
        self.columnconfigure((0,1,2,3,4), weight = 1, uniform = "x")
        self.rowconfigure(0, weight = 1, uniform = "x")
        ctk.CTkLabel(self,text = "Kur",font = (None,16)).grid(row = 0,column = 1, sticky = "nswe",padx = 5)
        self.entry = ctk.CTkEntry(self)
        self.entry.grid(row = 0,column = 2, sticky = "nswe",padx = 5)
        self.combobox = ctk.CTkComboBox(self, values=type_list)
        self.combobox.grid(row = 0,column = 3, sticky = "nswe",padx = 5)
        self.pack(expand = True)
        
class FrameTwo(ctk.CTkFrame):
    def __init__(self,parent,type_list):
        super().__init__(
            parent,
            fg_color = "#f1f3f5"
        )
        self.columnconfigure((0,1), weight = 1, uniform = "x")
        self.rowconfigure(0, weight = 1, uniform = "x")
        self.entry = ctk.CTkLabel(self,text = "Çevrilecek Kur",font=(None,16))
        self.entry.grid(row = 0,column = 0, sticky = "nswe")
        self.combobox = ctk.CTkComboBox(self, values=type_list)
        self.combobox.grid(row = 0,column = 1, sticky = "nswe")
        self.pack(expand = True)
        
if __name__ == '__main__':
    app = App()
