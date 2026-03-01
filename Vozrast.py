import tkinter as tk
from tkinter import ttk

def get_age_string(age):
    if age % 10 == 1 and age % 100 != 11:
        return f"Мне {age} год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return f"Мне {age} года"
    else:
        return f"Мне {age} лет"

def generate_age_phrases():
    output_text.delete("1.0", tk.END)
    for age in range(1, 100):
        phrase = get_age_string(age)
        output_text.insert(tk.END, phrase + "\n")

root = tk.Tk()
root.title("Возраст")

style = ttk.Style()
style.configure("TButton", padding=5, font=('Arial', 10))
style.configure("TLabel", padding=5, font=('Arial', 12))
style.configure("TFrame", padding=10)

main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True)

generate_button = ttk.Button(main_frame, text="Возраст", command=generate_age_phrases)
generate_button.pack(pady=10)

output_text = tk.Text(main_frame, height=15, width=40, wrap=tk.WORD)
output_text.pack(fill="both", expand=True)

scrollbar = ttk.Scrollbar(main_frame, command=output_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text['yscrollcommand'] = scrollbar.set

root.mainloop()