#Импортируем библиотеки в код
from tkinter import *
import os 
from tkinter import ttk


#Создаём функции нажатия на клавиши
def click1():
    global newcontxt
    newcontxt = 'C:\\Users\\DarkEnity\\Downloads\\'
def click2():
    global newcontxt
    newcontxt = 'C:\\Users\\DarkEnity\\Desktop\\'
def click3():
    global newcontxt
    newcontxt = 'C:\\Users\\DarkEnity\\Videos\\'
def click4():
    global newcontxt
    newcontxt = 'C:\\Users\\DarkEnity\\Documents\\'
def click5():
    global newcontxt
    newcontxt = 'C:\\Users\\DarkEnity\\Pictures\\'
def click6():
    global newcontxt
    newcontxt = 'C:\\Users\\DarkEnity\\Favorites\\'
    

#Создаём функцию копирования файлов
def run():
    global newcontxt
    filetype = ent.get()
    filepath = ent2.get()
    contxt = 'copy ' + newcontxt + filetype + ' ' + filepath
    print(contxt)
    os.system(contxt)
    
    
#Создаём окнo
root = Tk()


#Создаём переменную для работы в консоли
#contxt = 'copy ' + newcontxt + filetype + filepath


#Создаём параметры для окна root
root.geometry('350x260')
root.resizable(0,0)


#Создаём список из наших функций
list1 = [click1, click2, click3, click4, click5, click6]


#Создаём список координат x и y на которых будут расположены кнопки
x = [5]
y = [5, 45, 90, 135, 180, 225]


#Создаём список содержащий текст для кнопок
btntext = ['Downloads', 'Desktop', 'Videos', 'Documents', 'Images', 'Favorites']


#Прописываем цикл создающий кнопки
for i in range(0, 6):
    ttk.Button(root, command=list1[i], text=btntext[i]).place(width=70, height=30, x=x, y=y[i])


#Создаём первое текстовое окно
ttk.Label(root, text='File Type (mask)').pack() #Выводим с помощью метеда .pack()


#Создаём первое окно для ввода текста
ent = ttk.Entry(root)
ent.pack() #Выводим с помощью метеда .pack()

#Создаём второе текстовое окно
ttk.Label(root, text='Final Folder').pack() #Выводим с помощью метеда .pack()


#Создаём второе окно для ввода текста
ent2 = ttk.Entry(root)
ent2.pack() #Выводим с помощью метеда .pack()


#Создаём кнопку для начала копирования
ttk.Button(root, text='Run', command=run).place(x = 135, y = 100) #Выводим с помощью метеда .place()


#Выводим окно
root.mainloop()
