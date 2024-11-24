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
