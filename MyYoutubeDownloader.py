
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from tkinter import messagebox as m_box
import subprocess
import threading
#eger bu kitaplik yoksa hata yapmadan indir ve kullan
try:
    from pytube import YouTube
except:
    get_ipython().system('pip install pytube')
    
Folder_Name=""

# kullancıya pencere açıp dizini gösteren bir metodudur
def openLocation():
    global Folder_Name
    Folder_Name=filedialog.askdirectory()
    if(len(Folder_Name)>1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="lutfen dosyayi secin !!! ",fg="red")

#inidrme metodu 
def DownloadVideo():
    choice=ytdchoices.get()
    url=ytdEntry.get()
    if(len(url)>1):
        ytdError.config(text="")
        yt=YouTube(url)
        
        if(choice==choices[0]):
            select=yt.streams.get_highest_resolution()
        elif(choice==choices[1]):
            select=yt.streams.filter(progressive=True).first()
        elif(choice==choices[2]):
            select=yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="linki bir daha giriniz",fg='red')
            
 
    select.download(Folder_Name)
    ytdError.config(text=' ****************** İndirme tamamlandı !! ******************',fg='green')

#-------------arayuzu ve kod islemi-----------------------------    
window = tk.Tk()
window.title("youtube video ve ses indirme programı")
window.geometry('650x410+340+10')
window.resizable(False,False)
window.columnconfigure(0,weight=1)

f1=tk.Frame(window,width=580,height=100,bg='whitesmoke',bd=3,relief=GROOVE)
f1.place(x=30,y=130)
f2=tk.Frame(window,width=580,height=55,bg='whitesmoke',bd=3,relief=GROOVE)
f1.place(x=30,y=250)

title= tk.Label(master=window, text="youtube tan indirme programı",bg='red',fg='white',font=("Tajawal",15,'bold'))
# 
title.pack(fill=X)

ytdLabel= tk.Label(master=window, text="indireceğiniz videonun linki giriniz " ,font=("Tajawal",15,'bold'))
ytdLabel.pack()
ytdLabel= tk.Label(master=window, text="ctrl + C , ctrl + v kullanarak yapabilirsiniz" ,font=("Tajawal",9))
ytdLabel.pack()
 

#giris kutusu
ytdEntryVar=tk.StringVar()
ytdEntry= Entry(window,width=70,justify='center',font=("Tajawal",15 ),fg='blue',textvariable=ytdEntryVar)
ytdEntry.pack()

#hatta  Msj
ytdError=tk.Label(master=window, text="indirme durumu",fg="red" ,font=("Tajawal",10,'bold'))
ytdError.pack()

#asking save file label
saveLabel=tk.Label(master=window, text="Videonun nereye kaydedileceğini seçin ",bg='whitesmoke' ,font=("Tajawal",10,'bold'))
saveLabel.place(x=390,y=140)
 
#btn dosya kaydi
saveEntry=tk.Button(window,width=20,font=("Tajawal",12),bg="red",fg="white",text="kaydedileceği dizin",command=openLocation)
saveEntry.place(x=440,y=180)
 
#lokasiyonu hatali msj
locationError =tk.Label(master=window, text="Videonun nereye kaydedileceğini seçmediniz !!",bg='whitesmoke',fg='red' ,font=("Tajawal",12))
locationError.place(x=100,y=190)

#indirme kalitesi 
ytdQuality=tk.Label(window,text="videonun kalitesi seciniz",bg='whitesmoke',font=("Tajawal",9,'bold'))
ytdQuality.place(x=430,y=255)

#combobox
choices=["720p kalitesi","144p kalitesi","sadece ses"]
ytdchoices=ttk.Combobox(window,values=choices)
ytdchoices.place(x=260,y=265)

#indirme btnu 
downloadbtn=tk.Button(window,text="indirmeyi başlat",width=20,font=("Tajawal",12 ),bg='red',fg='white',command=DownloadVideo)
downloadbtn.place(x=40,y=255)

#tasarlanan metin kutusu

DevLeb1=tk.Label(window,text="BARAA MASRI",fg='blue',bg='whitesmoke',font=("Tajawal",12,'bold'))
DevLeb1.place(x=225,y=350)
DevLeb2=tk.Label(window,text="Tarafından tasarlanmış",fg='blue',bg='whitesmoke',font=("Tajawal",10))
DevLeb2.place(x=250,y=370)
DevLeb3=tk.Label(window,text="ÇANAKKALE üniversitesi",fg='grey',bg='whitesmoke',font=("Tajawal",13,'bold'))
DevLeb3.place(x=460,y=370)

#programi calismakta tutan loopu 
window.mainloop()





