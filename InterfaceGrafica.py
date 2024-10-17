import customtkinter as ctk
import tkinter as tk
from Chatbot import GerarConteudo
from Perguntas import InteracaoChatBot

class Interface_Chat():
        def __init__(self):
                self.app = ctk.CTk()
                self.saudacoes = InteracaoChatBot()
                self.conversas = []
                self.tela()
                self.tela_chat()

                self.app.mainloop()

        def tela(self):
                largura_janela = 1000
                altura_janela = 650

                largura_tela = self.app.winfo_screenwidth()
                altura_tela = self.app.winfo_screenheight()

                pos_x = (largura_tela // 2) - (largura_janela // 2)
                pos_y = (altura_tela // 2) - (altura_janela // 2)

                self.app.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')
                self.app.title("ChatBot")
                self.app.resizable(False, False)
                ctk.set_appearance_mode('system')

        def tela_chat(self):
                self.frame_chat = ctk.CTkFrame(master=self.app, fg_color='#fff')
                self.frame_chat.pack(fill="both", expand=True)

                self.label_title = ctk.CTkLabel(self.frame_chat, text='Chat Bot', font=('Arial', 32))
                self.label_title.pack(pady=(20, 0))

                self.label_saudacao = ctk.CTkLabel(self.frame_chat, text=self.saudacoes.InteracaoRam(), font=('Arial', 14))
                self.label_saudacao.pack(pady=(30, 0))

                self.text_conversa = ctk.CTkTextbox(self.frame_chat, width=800, height=380, state="disabled", fg_color='#D7D8D7')
                self.text_conversa.pack(pady=(20, 0))

                '''self.label_text = ctk.CTkLabel(self.frame_chat, text='', font=('Arial', 14), text_color='black')
                self.label_text.pack(pady=(40, 0))

                self.label_res = ctk.CTkLabel(self.frame_chat, text='', font=('Arial', 14), text_color='black')
                self.label_res.pack(pady=(40, 0))'''

                self.entry = ctk.CTkTextbox(self.frame_chat, width=500, height=60, fg_color='#D7D8D7')
                self.entry.pack(pady=(10, 0))
                self.entry.bind('<Return>', lambda event: self.funcao_enviar())

                button = ctk.CTkButton(self.frame_chat, text='Enviar', width=100, command=self.funcao_enviar)
                button.pack(pady=(20, 0))

        def funcao_enviar(self):
                entry_user = self.entry.get('1.0', tk.END).strip()

                if entry_user:
                        self.conversas.append(f'Você: {entry_user}\n')
                        self.atualizar_conversa()

                        conversa = GerarConteudo(entry_user)
                        resposta = conversa.gerar_texto()

                        self.conversas.append(f'Bot: {resposta}\n')
                        self.atualizar_conversa()

                        self.entry.delete('1.0', tk.END)

        def atualizar_conversa(self):
                self.text_conversa.configure(state="normal")
                self.text_conversa.delete('1.0', tk.END)

                for conversa in self.conversas:
                        self.text_conversa.insert(tk.END, conversa + "\n")

                self.text_conversa.configure(state="disabled")
                self.text_conversa.yview(tk.END)

Interface_Chat()
