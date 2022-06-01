from tkinter import *
import requests
def currency():
    global lab
    global information
    request=requests.get(url='https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=400').json()
    for cur in request['data']['cryptoCurrencyList']:
        if cur['name'].lower() == information.get().lower():
            lab=Label(root, text=f"Название: {cur['name']}\n"
                                 f"Цена: {round(cur['quotes'][0]['price'],2)}$", bg='#ACC3C4', font=('Candara', 14, 'bold'))
            lab.place(x=173,y=299)
def delete():
    lab.destroy()
root=Tk()
root.title('Проект парсер')
root.resizable(height=False,width=False)
root.geometry('500x500')
root['bg']='#D7BCE7'
lab1=Label(root, text='Введите название валюты:', bg='#D7BCE7',font=('Candara', 11, 'bold'),bd=0)
lab1.place(x=150,y=150)
root.iconphoto(True,PhotoImage(file='icon.png'))
information=StringVar()
lab=Label(root)
pole=Entry(root, textvariable=information, bg='#32BFC8', font=('Candara', 14))
pole.place(x=150,y=180)
but=Button(root, text='Парсить', font=('Candara', 12), bg='#32BFC8', command=currency)
but.place(x=150, y=210)
but1=Button(root, text='Очистить',font=('Candara',12), bg='#32BFC8', command=delete)
but1.place(x=230,y=210)
pole1=Label(root, bg='#ACC3C4', width=28, height=10, relief='solid')
pole1.place(x=150,y=250)
lab2=Label(root,text='ParseR', bg='#7AB9BD', font=('Candara', 32,'bold'))
lab2.place(x=185,y=50)
root.mainloop()