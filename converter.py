from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Задаем название и размер окна
root = Tk()
root.title('Конвертер валют')  
root.geometry('600x600') 

my_notebook = ttk.Notebook(root) 
my_notebook.pack(pady=5)

# Создаем вкаладки 
currency_frame = Frame(my_notebook, width=480, height=480)
conversion_frame = Frame(my_notebook, width=480, height=480)

currency_frame.pack(fill='both', expand=1)
conversion_frame.pack(fill='both', expand=1)

# Называем ярлыки
my_notebook.add(currency_frame, text = 'Введите что будем конвертировать')      
my_notebook.add(conversion_frame, text='Расчет')

my_notebook.tab(1, state='disabled')

def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():   # предупреждение о незаполнении
        messagebox.showwarning('ВНИМАНИЕ!','Что то не то нажали') 
    else:

        home_entry.config(state='disabled')
        conversion_entry.config(state='disabled')
        rate_entry.config(state='disabled')
        
        my_notebook.tab(1, state='normal')

        amount_label.config(text =f'Введите сколько {home_entry.get()} будем переводить в {conversion_entry.get()}')
        converted_label.config(text=f'Данная сумма будет в  {conversion_entry.get()}')
        convert_button.config(text=f'Переводим {home_entry.get()}')

def unlock():

    home_entry.config(state='normal')
    conversion_entry.config(state='normal')
    rate_entry.config(state='normal')
    my_notebook.tab(1, state='disabled')  
# Что переводим 
home = LabelFrame(currency_frame, text ='Чьи деньги переводим')
home.pack(pady=20)

home_entry = Entry(home, font=('Avenir Next', 24)) 
home_entry.pack(pady=10, padx=10)

# во что переводим 
conversion = LabelFrame(currency_frame, text='Валюта/Курс')
conversion.pack(pady=20)

conversion_label = Label(conversion, text = 'Переводим в')
conversion_label.pack(pady=10)

conversion_entry = Entry(conversion, font=('Avenir Next', 24))
conversion_entry.pack(pady=10, padx=10)

rate_label = Label(conversion, text = 'Введите курс ЦБ')
rate_label.pack(pady=10)

rate_entry = Entry(conversion, font=('Avenir Next', 24))
rate_entry.pack(pady=10, padx=10)

button_frame = Frame(currency_frame)
button_frame.pack(pady=20)

lock_button = Button(button_frame, text = 'Закрыть', command=lock)
lock_button.grid(row=0, column=0, padx=10)

unlock_button = Button(button_frame, text = 'Открыть', command=unlock)
unlock_button.grid(row=0, column=1, padx=10 )

def convert():

    converted_entry.delete(0, END)

    conversion = float(rate_entry.get()) * float(amount_entry.get())
    conversion = round(conversion,2)
    conversion = '{:,}'.format(conversion)
    converted_entry.insert(0,f'{conversion}')

def clear():
    amount_entry.delete(0, END)
    converted_entry.delete(0, END)

amount_label = LabelFrame(conversion_frame, text='Итоги перевода')
amount_label.pack(pady=20)

amount_entry = Entry(amount_label, font=('Avenir Next', 24))
amount_entry.pack(pady=10, padx=10)

convert_button = Button(amount_label, text='Перевести',command=convert)
convert_button.pack(pady=20)

converted_label = LabelFrame(conversion_frame, text='Переведенная валюта')
converted_label.pack(pady=20)

converted_entry = Entry(converted_label, font=('Avenir Next', 24), bd=0, bg='green') 
converted_entry.pack(pady=10, padx=10)

clear_button = Button(conversion_frame, text='Очистить', command = clear )
clear_button.pack(pady=20)

spacer = Label(conversion_frame, text='', width=68) # fake
spacer.pack()


root.mainloop()