import customtkinter as ctk
import tkinter as tk
from Chatbot import GerarConteudo
from Perguntas import InteracaoChatBot
from nltk.tokenize import sent_tokenize
import random

class Interface_Chat():
    def __init__(self):
        self.app = ctk.CTk()
        self.saudacoes = InteracaoChatBot()
        self.conversas = []
        self.conteudo_completo = ''
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

        self.text_conversa = ctk.CTkTextbox(self.frame_chat, width=600, height=380, state="disabled", fg_color='#D7D8D7', wrap=tk.WORD)
        self.text_conversa.configure(font=('Arial', 12))
        self.text_conversa.pack(pady=(20, 0))

        self.entry = ctk.CTkTextbox(self.frame_chat, width=500, height=60, fg_color='#D7D8D7')
        self.entry.pack(pady=(20, 0))
        self.entry.bind('<Return>', lambda event: self.funcao_enviar())

        self.entry.bind('<Control-v>', lambda event: self.paste_text())

        button = ctk.CTkButton(self.frame_chat, text='Enviar', width=100, command=self.funcao_enviar)
        button.pack(pady=(20, 0))

    def paste_text(self, event):
        self.entry.insert(tk.END, self.app.clipboard_get())
        return 'break'

    def funcao_enviar(self):
        entry_user = self.entry.get('1.0', tk.END).strip()

        if entry_user:
            self.entry.delete('1.0', tk.END)
            self.conversas.append(f'Você: {entry_user}\n\n')
            self.conteudo_completo += f'Você: {entry_user}\n\n'
            self.atualizar_conversa()

            if entry_user.lower() == 'resuma' or entry_user == 'Resuma':
                resumo = self.resumir_conversa()
                self.conversas.append(f'Bot: {resumo}\n\n')
                self.atualizar_conversa()
            else:
                conversa = GerarConteudo(entry_user)
                resposta = conversa.gerar_texto()

            self.conversas.append('Bot: ')
            self.conteudo_completo += 'Bot: '
            self.atualizar_conversa()

            self.animar_resposta(resposta  + '\n\n')

    def resumir_conversa(self):
        frases = sent_tokenize(self.conteudo_completo)  # Divide o texto em frases
        # Apenas um exemplo simples de resumo: pega as 2 primeiras frases
        resumo = ' '.join(frases[:2]) if len(frases) >= 2 else self.conteudo_completo
        return resumo

    def animar_resposta(self, resposta):
        self.text_conversa.configure(state="normal")
        
        self.index = 0 
        self.resposta = resposta
        self.text_conversa.insert(tk.END, 'Bot: ')
        self.atualizar_conversa()
        self.escrever_letra()

    def escrever_letra(self):
        if self.index < len(self.resposta):
            self.conversas[-1] += self.resposta[self.index]
            self.atualizar_conversa()
            self.index += 1
            self.text_conversa.see(tk.END)
            self.app.after(3, self.escrever_letra)
        else:
            self.text_conversa.configure(state="disabled")

    def atualizar_conversa(self):
        self.text_conversa.configure(state="normal")
        self.text_conversa.delete('1.0', tk.END)

        for conversa in self.conversas:
            conversa_str = str(conversa)
            
            if conversa_str.startswith('#'):
                texto_sem_simbolo = conversa_str[1:].strip()  
                self.text_conversa.insert(tk.END, texto_sem_simbolo + '\n', 'bold')  

            elif conversa_str.startswith('**'):
                texto_sem_simbolos = conversa_str[2:].strip()  
                self.text_conversa.insert(tk.END, texto_sem_simbolos + '\n', 'bold')  

            else:
                self.text_conversa.insert(tk.END, conversa + '\n') 

        self.text_conversa.configure(state="disabled")
        self.text_conversa.yview(tk.END)

Interface_Chat()
