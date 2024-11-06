import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from Chatbot import GerarConteudo
from Perguntas import InteracaoChatBot

class Interface_Chat():
    def __init__(self):
        self.app = ctk.CTk()

        self.app.iconbitmap('images/logo.ico')

        self.font_header = 'League Spartan'
        self.font_body = 'Montserrat Classic'

        self.saudacoes = InteracaoChatBot()
        self.despedidas = InteracaoChatBot()

        self.conversas = []
        
        ctk.set_appearance_mode('system')
        self.definir_cores()

        self.tela()
        self.tela_chat()

        self.criar_menu()

        self.app.mainloop()

    def definir_cores(self):
        self.current_mode = ctk.get_appearance_mode()
        if self.current_mode == "Dark":
            self.bg_color = "#2C2C2C"  # Cor de fundo escura
            self.text_color = "#FFFFFF"  # Texto branco
            self.entry_color = "#3C3C3C"  # Caixa de entrada mais escura
        else:
            self.bg_color = "#FFFFFF"  # Cor de fundo branca
            self.text_color = "#000000"  # Texto preto
            self.entry_color = "#D7D8D7"  # Caixa de entrada clara

    def tela(self):
        largura_janela = 1000
        altura_janela = 650

        largura_tela = self.app.winfo_screenwidth()
        altura_tela = self.app.winfo_screenheight()

        pos_x = (largura_tela // 2) - (largura_janela // 2)
        pos_y = (altura_tela // 2.22) - (altura_janela // 2)

        self.app.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')
        self.app.title("ChatBot")
        self.app.resizable(False, False)

    def tela_chat(self):
        self.frame_chat = ctk.CTkFrame(master=self.app, fg_color=self.bg_color)
        self.frame_chat.pack(fill="both", expand=True)

        self.label_title = ctk.CTkLabel(self.frame_chat, text='Chat Bot', font=(self.font_header, 32), text_color=self.text_color)
        self.label_title.pack(pady=(20, 0))

        self.label_saudacao = ctk.CTkLabel(self.frame_chat, text=self.saudacoes.InteracaoRam(), font=(self.font_body, 14), text_color=self.text_color)
        self.label_saudacao.pack(pady=(20, 0))

        self.text_conversa = ctk.CTkTextbox(self.frame_chat, width=600, height=360, state="disabled", fg_color=self.entry_color, wrap=tk.WORD, text_color=self.text_color)
        self.text_conversa.configure(font=('Arial', 12))
        self.text_conversa.pack(pady=(20, 0))

        self.entry = ctk.CTkTextbox(self.frame_chat, width=500, height=60, fg_color=self.entry_color, text_color=self.text_color)
        self.entry.pack(pady=(30, 0))
        self.entry.bind('<Return>', lambda event: self.funcao_enviar())

        button = ctk.CTkButton(self.frame_chat, text='Enviar', width=100, command=self.funcao_enviar, fg_color='#232DA9', hover_color='#02075D')
        button.pack(pady=(20, 0))

        
    def limpar_chat(self):
        self.conversas.clear()
        self.atualizar_conversa()

    def criar_menu(self):
        # Frame para o menu no canto superior direito
        self.menu_frame = ctk.CTkFrame(self.app, width=100, height=50, fg_color='gray')
        self.menu_frame.place(x=920, y=10)  # Posicionar o menu no canto superior direito

        # Botão de três barrinhas (menu hamburguer)
        self.menu_button = ctk.CTkButton(self.menu_frame, text="≡", width=30, height=30, command=self.menu_opcoes, fg_color=self.bg_color, text_color=self.text_color)
        self.menu_button.pack(pady=10, padx=10)

    def menu_opcoes(self):
        # Criação do menu suspenso
        self.menu = tk.Menu(self.app, tearoff=0)
        self.menu.add_command(label="Sair", command=self.sair, font=('Arial', 16))
        self.menu.add_command(label="Limpar Chat", command=self.limpar_chat, font=('Arial', 16))

        # Exibir o menu suspenso no botão
        self.menu.post(self.menu_button.winfo_rootx(), self.menu_button.winfo_rooty() + self.menu_button.winfo_height())

    def sair(self):
        messagebox.showinfo('Sair', self.despedidas.DespedidaRam())

        self.app.quit()

    def paste_text(self, event):
        self.entry.insert(tk.END, self.app.clipboard_get())
        return 'break'

    def funcao_enviar(self):
        entry_user = self.entry.get('1.0', tk.END).strip()

        if entry_user:
            self.entry.delete('1.0', tk.END)

            self.conversas.append(f'Você: {entry_user}\n\n')
            self.atualizar_conversa()

            conversa = GerarConteudo(entry_user)
            resposta = conversa.gerar_texto()

            self.conversas.append('Bot: ')
            self.atualizar_conversa()

            self.animar_resposta(resposta  + '\n\n')

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
