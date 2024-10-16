import customtkinter as ctk
import tkinter as tk
from Chatbot import GerarConteudo
from Perguntas import InteracaoChatBot

saudacoes = InteracaoChatBot()

app = ctk.CTk()
app.geometry("700x600")
app.title("ChatBot")
app.resizable(False, False)

frame_chat = ctk.CTkFrame(master=app, width=450, height=750, fg_color='#B3B3B3')
frame_chat.pack()

label_title = ctk.CTkLabel(frame_chat, text='Chat Bot', font=('Arial', 32))
label_title.pack(pady=(30,0))

label_saudacao = ctk.CTkLabel(frame_chat, text=saudacoes.IteracaoRam(), font=('Arial', 14))
label_saudacao.pack(pady=(30, 0))

label_text = ctk.CTkLabel(frame_chat, text='', font=('Arial', 10), text_color='black')
label_text.pack(pady=(50,0))

label_res = ctk.CTkLabel(frame_chat, text='', font=('Arial', 10), text_color='black')
label_res.pack(pady=(40, 0))

entry = ctk.CTkTextbox(frame_chat, width=300, height=60)
entry.pack(pady=(180, 0))
entry.bind('<Return>', lambda event: funcao_enviar())

button = ctk.CTkButton(frame_chat, text='Enviar', width=100, command=lambda: funcao_enviar())
button.pack(pady=(50, 0))

def funcao_enviar():
        entry_user = entry.get('1.0', tk.END).strip()
        label_text.configure(text=entry_user)

        conversa = GerarConteudo(entry_user)
        label_res.configure(text=conversa.gerar_texto())

        entry.delete('1.0', tk.END)

app.mainloop()