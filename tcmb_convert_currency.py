print("merhaba dolar")
print("merhaba euro")


# tcmb sitesinden efektif dolar satış fiyatını çekelim
# https://www.turkiye.gov.tr/doviz-kurlari

from bs4 import *
import requests
from tkinter import *
# yukarıdaki şekilde import ettiğimizde
# message eklenemiyor, ayrıca çağırmak lazım

# gui oluşturuyoruz.
root = Tk()

root.title("TCMB Currency")
root.configure(background="light blue")
# root.resizable(width=False, height=False)
dolar_label = Label(root, text="dolar:",
                    background="light blue",
                    font="Arial 12 bold")

dolar_label.grid(row=0, column=0, padx=10, pady=10)

#entry oluşturacağız
dolar_text = DoubleVar()
dolar_entry = Entry(root, width=15, textvariable=dolar_text,justify="right")
dolar_entry.grid(row=0, column=1, sticky=E)

# TL

tl_label = Label(root, text="tl:",
                    background="light blue",
                    font="Arial 12 bold")

tl_label.grid(row=1, column=0, padx=10, pady=(5, 0))

# tl entry
tl_text = DoubleVar()
tl_entry = Entry(root, width=15, textvariable=tl_text, justify="right")
tl_entry.grid(row=1, column=1, sticky=E)


def dolar_çevir():
    sayfa = requests.get("https://www.turkiye.gov.tr/doviz-kurlari")
    # bu code başarılıysa 200 kodunu döner.
    #print(sayfa)

    #bu kod sayfa kaynağını çıkarır
    # print(sayfa.text)

    soup = BeautifulSoup(sayfa.text, "html.parser")

    # kodu böleceksem \ koymalıyım
    # fonksiyonun içini direkt aşağı atabilirim.
    #     .find_next_sibling("td") şeklinde de yazılabilir, input vermeden de çalışıyor.

    effective_sell_dolar_1 = soup.find("td",
                                       text="1 ABD DOLARI") \
        .find_next_sibling() \
        .find_next_sibling() \
        .find_next_sibling() \
        .find_next_sibling().text
    tl_miktar = dolar_text.get() * float(effective_sell_dolar_1)
    tl_text.set(tl_miktar)
    print(effective_sell_dolar_1)


# buton ekliyoruz

cevir_btn = Button(root, text="çevir", width=10,
                   command=dolar_çevir)
cevir_btn.grid(row=2, column=0, columnspan=2)

def center_window(w, h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

center_window(280, 150)

# feature-24: programı gui'li hale getirelim.
# feature-25: çevirdiği dövizi text dosyasına loglasın.
# feature-26: çevirdiği dövizi veritabanına kaydetsin.

root.mainloop()
