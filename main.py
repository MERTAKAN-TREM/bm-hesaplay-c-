from tkinter import *


window = Tk()
window.title("BMİ hasaplayıcı")
window.minsize(width=300,height=400)
window.config(bg="blue")




def çoktı():
    kilo = kilosu.get()
    boy = boyu.get()
    if boy == "" or kilo == "":
        label_uyarı.pack()
    else:
        try:
            bmı = float(kilo) / (float(boy) / 100) ** 2
            result_string = bmı_hesaplama(bmı)
            label_uyarı.config(text=f"{result_string}", bg="black", fg="red")
            label_uyarı.pack()
        except:
            label_uyarı.config(text="sayı gir",bg="black",fg="red")


def bmı_hesaplama(bmi):
    result_string = f"sen  {round(bmi, 2)} yani .  "
    if bmi <= 16:
        result_string += "aşırı zayıfsın"
    elif 16 < bmi <= 17:
        result_string += "çok zayıfsın"
    elif 17 < bmi <= 18.5:
        result_string += "zayıfsın"
    elif 18.5 < bmi <= 25:
        result_string += "normalsın"
    elif 25 < bmi <= 30:
        result_string += "kilolusun"
    elif 30 < bmi <= 35:
        result_string += "1 derece obezsin"
    elif 35 < bmi <= 40:
        result_string += "2 derece obezsin"
    else:
        result_string += "3 derece obezsin "
    return result_string



# labeler
label_uyarı = Label()
label_uyarı.config(text="Lütfen boş girmeyiniz",bg="black",fg="red")


label_kilo = Label()
label_kilo.config(text="Lütfen Kilonuzu giriniz",bg="black",fg="white",font=("Arial",16,"normal"))
label_kilo.pack()
label_kilo.place(x=50,y=25)

label_boy = Label()
label_boy.config(text="Lütfen Boyunuzu giriniz",bg="black",fg="white",font=("Arial",15,"normal"))
label_boy.pack()
label_boy.place(x=50,y=85)

#entgry ekleme
kilosu = Entry()
kilosu.config(width=30)
kilosu.pack()
kilosu.place(x=50,y=60)

boyu = Entry()
boyu.config(width=30)
boyu.pack()
boyu.place(x=50,y=120)

'''
#butonlar
kilo_buttonu = Button()
kilo_buttonu.config(text="Onayla",bg="white",fg="black",command= kilokontrol)
kilo_buttonu.pack()
kilo_buttonu.place(x=240,y=57)

boy_buttonu = Button()
boy_buttonu.config(text="Onayla",bg="white",fg="black",command=boykontrol)
boy_buttonu.pack()
boy_buttonu.place(x=240,y=117)
'''
hesaplama_buttonu = Button()
hesaplama_buttonu.config(text="Hesapla",bg="white",fg="black",command=çoktı)
hesaplama_buttonu.pack()
hesaplama_buttonu.place(x=150,y=180)


window.mainloop()