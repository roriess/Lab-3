import tkinter as tk
import random

minimum_sum = 30
maximum_sum = 35


def generate_key():
    weights = {chr(i): i - 64 for i in range(65, 91)}
    blocks = []

    for _ in range(3):
        while True:
            block = ''.join(random.choices(list(weights.keys()), k=4))
            if minimum_sum <= sum(weights[c] for c in block) <= maximum_sum:
                blocks.append(block)
                break

    key = '-'.join(blocks)
    key_var.set(key)


root = tk.Tk()
root.title("Keygen")


background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


key_var = tk.StringVar()
key_entry = tk.Entry(root, textvariable=key_var, font=("Arial", 24), justify='center')
key_entry.pack(pady=20)


generate_button = tk.Button(root, text="Сгенерировать ключ", command=generate_key)
generate_button.pack(pady=20)


root.mainloop()

























# from tkinter import*
# from tkinter import messagebox 


# window = Tk()  
# window.title("Добро пожаловать в приложение PythonRu")  
# window.geometry('600x300') 


# background = PhotoImage(file = "background.png")
# bg = Label(window, image = background) 
# bg.place(x = 0, y = 0) 


# lbl = Label(window, text="Введите ключ:", font=("Arial Bold", 25))
# lbl.grid(column=1, row=3)  


# btn = Button(window, text="Пуск")
# btn.grid(column=1, row=5)


# txt = Entry(window,width=10)  
# txt.grid(column=1, row=4)  
# txt.focus()


# interval = [int(i) for i in range(30, 36)] 
# alphabet = [chr(i) for i in range(97, 123)]


# def clicked():
#     messagebox.showinfo('Заголовок', 'Текст')

# btn = Button(window, text="Пуск", command=clicked)


# window.mainloop()
