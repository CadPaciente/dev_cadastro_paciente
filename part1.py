'''
CRIANDO A TELA PRINCIPAR COM AS LABELS
'''

from tkinter import *

root = Tk()

class principa():
    def __init__(self):
        self.root = root
        self.tela()
        self.cor_widgets()
        self.widgets_frame1()

        root.mainloop()

# Tela principal
        def tela(self):
        self.root.title("PACIENTE")
        self.root.configure(bg='#008888')
        self.root.geometry("1366x768+0+0")
        #self.root.overrideredirect(True)

    def cor_widgets(self):
# Botões
        self.bt_bg = '#008888'
        self.bt_fg = 'white'
        self.bt_font = ('verdana', 13, 'bold')
# Label
        self.lb_bg = '#008888'
        self.lb_fg = 'white'
        self.lb_font = ('arial', 15, 'bold')

# Entrada de dados
        self.et_bg = '#008888'
        self.et_bg_branco = 'white'
        self.et_fg_branco = "#ffffff"
        self.et_fg_preto = '#000000'
        self.et_font = ('arial', 15, 'bold')

    def widgets_frame1(self):
# Label Nome PACIENTE tela principal
        self.lb_cadastro = Label(self.root, text='P  A  C  I  E  N  T  E', bg=self.lb_bg, fg=self.lb_fg, font=('arial black', 40, 'bold'))
        self.lb_cadastro.place(x=420, y=0)

# Label id
        self.lb_codigo = Label(self.root, text='id:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_codigo.place(x=137, y=46)

# Label Nome
        self.lb_nome = Label(self.root, text='Nome:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_nome.place(x=100, y=85)

# Label Est. Civíl
        self.lb_civil = Label(self.root, text='Estado Civíl:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_civil.place(x=40, y=155)

# Label Religião
        self.lb_religiao = Label(self.root, text='Religião:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_religiao.place(x=75, y=225)

# Label Profissão
        self.lb_profissao = Label(self.root, text='Profissão:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_profissao.place(x=58, y=290)

# Label Cidade
        self.lb_cidade = Label(self.root, text='Cidade:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_cidade.place(x=388, y=155)

# Label Estado
        self.lb_estado = Label(self.root, text='Estado/UF:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_estado.place(x=355, y=225)

# Label Telefone
        self.lb_telefone = Label(self.root, text='Telefone:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_telefone.place(x=375, y=290)

# Label Nascimento
        self.lb_nascimento = Label(self.root, text='Nasc.:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_nascimento.place(x=730, y=155)

# Label Observação
        self.lb_observacao = Label(self.root, text='Obs.:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_observacao.place(x=20, y=370)

# Label Receita
        self.lb_receita = Label(self.root, text='RECOMENDAÇÕES TERAPÊUTICAS:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_receita.place(x=700, y=210)

principa()

