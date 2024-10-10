import customtkinter as ctk
import tkinter as tk
from Chatbot import GerarConteudo

app = ctk.CTk()
app.geometry("400x600")
app.title("Meu WhatsApp")
app.resizable(False, False)

label_title = ctk.CTkLabel(app, text='Chat Bot', font=('Arial', 32))
label_title.pack(pady=(30,0))

label_text = ctk.CTkLabel(app, text='', font=('Arial', 14), text_color='black')
label_text.pack(pady=(50,0))

label_res = ctk.CTkLabel(app, text='', font=('Arial', 14), text_color='black')
label_res.pack(pady=(40, 0))

entry = ctk.CTkTextbox(app, width=300, height=80, wrap='word')
entry.pack(pady=(180, 0))

button = ctk.CTkButton(app, text='Enviar', width=100, command=lambda: funcao_enviar())
button.pack(pady=(40, 0))

def funcao_enviar():
    entry_user = entry.get('1.0', tk.END).strip()
    label_text.configure(text=entry_user, fg_color='gray')

    conversa = GerarConteudo(entry_user)
    label_res.configure(text=conversa.gerar_texto(), fg_color='gray')

app.mainloop()