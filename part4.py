'''
CONFIGURANDO OS BOTÕES CONVERTENDO OS PNG PARA BASE 64 E CONFIGURANDO AS ENTRADAS AUTOcompleteENTRY
'''

from tkinter import *
from ttkwidgets.autocomplete import AutocompleteEntry
from tkinter import ttk

from datetime import datetime

import sys
import base64

root = Tk()

class principal():
    def __init__(self):
        self.root = root
        self.tela()
        self.cor_widgets()
        self.widgets_frame1()
        self.grid_cliente()
        self.grid_cliente2()

        root.mainloop()
# Tela principal
    def tela(self):
        self.root.configure(bg='#008888')
        self.root.geometry("1366x768+0+0")
        self.root.overrideredirect(True)

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
# Data Local
        self.dia_atual = (datetime.today().strftime('Goiânia, %d de %B de %Y'))
        self.hj = Label(self.root, text=f'{self.dia_atual}', bg=self.lb_bg, fg=self.lb_fg, font=('arail', 10, 'bold'))
        self.hj.place(x=0, y=0, width=220, height=51)


# Label Nome PACIENTE tela principal
        self.lb_cadastro = Label(self.root, text='P  A  C  I  E  N  T  E', bg=self.lb_bg, fg=self.lb_fg, font=('arial black', 40, 'bold'))
        self.lb_cadastro.place(x=420, y=0)

# Label id
        self.lb_codigo = Label(self.root, text='id:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_codigo.place(x=153, y=46)

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
        self.lb_telefone.place(x=370, y=290)

# Label Nascimento
        self.lb_nascimento = Label(self.root, text='Nasc.:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_nascimento.place(x=730, y=155)

# Label Observação
        self.lb_observacao = Label(self.root, text='Obs.:', bg=self.lb_bg, fg=self.lb_fg, font=self.lb_font)
        self.lb_observacao.place(x=20, y=370)

# Label Receita
        self.lb_receita = Label(self.root, text='RECOMENDAÇÕES TERAPÊUTICAS:', bg=self.lb_bg, fg=self.lb_fg, font=('arial', 13, 'bold'))
        self.lb_receita.place(x=714, y=210)

# Entry Código
        self.entry_codigo = Entry(self.root, bg=self.et_bg, fg=self.et_fg_branco, font=self.et_font, relief=FLAT)
        self.entry_codigo.place(x=187, y=48, width=60, height=27)

# Entry Nome
        self.entry_nome = Entry(self.root, bg=self.et_bg_branco, fg=self.et_fg_preto, font=self.et_font)
        self.entry_nome.place(x=170, y=85, width=500, height=25)

# AutoCompleteENtry Estado Civil
        self.civil = ["CASADO", "SOLTEIRO", "DESQUITADO",
                      "AMASIADO", "SEPARADO", "VIÚVO", "DIVORCIADO"
                      ]
        self.entry_civil = AutocompleteEntry(self.root, font=('arial', 13, 'bold'), completevalues=self.civil)
        self.entry_civil.place(x=170, y=155, width=167, height=25)

# AutoCompleteENtry Religião
        self.lista = ["CATÓLICO", "ESPÍRITA", "EVANGÉLICO",
                      "PROTESTANTE", "MORMO", "CAMDOBLÉ", "ATEU"
                      ]
        self.entry_religiao = AutocompleteEntry(self.root, font=('arial', 13, 'bold'), completevalues=self.lista)
        self.entry_religiao.place(x=170, y=225, width=167, height=25)

# AutoCompleteENtry Profissão
        self.profissao = ["ADVOGADO", "JUÍZ", "AGRICULTOR", "DO LAR", "ENGENHEIRO", "ARQUITETO", "GERENTE",
            "BABÁ", "MOTORISTA", "APOSENTADO", "MÉDICO", "TI",
            "PROFESSOR", "DIARISTA", "TAXISTA", "FARMACÊUTICO"
                      ]
        self.entry_profissao = AutocompleteEntry(self.root, font=('arial', 13, 'bold'), completevalues=self.profissao)
        self.entry_profissao.place(x=170, y=290, width=167, height=25)

# AutoCompleteEntry Cidade
        from cidade import cidades
        self.local = cidades

        self.entry_cidade = AutocompleteEntry(self.root,  font=('arial', 13, 'bold'), completevalues=self.local)
        self.entry_cidade.place(x=470, y=155, width=200, height=25)

# AutoCompleteEntry Estado
        self.estado = ["Acre/AC", "Alagoas/AL", "Amapá/AP", "Amazonas/AM", "Bahia/BA", "Ceará/CE",
                       "Esp. Santo/ES", "Goiás/GO", "Maranhão/MA", "M. Grosso/MT",
                       "M. Grosso Sul/MS", "Minas Gerais/MG",
                       "Pará/PA", "Paraíba/PB", "Paraná/PR", "Pernambuco/PE", "Piauí/PI",
                       "Rio de Janeiro/RJ",
                       "Rio G. do Norte/RN", "Rio G. do Sul/RS", "Rondônia/RO", "Roraima/RR",
                       "Santa Catarina/SC",
                       "São Paulo/SP", "Sergipe/SE", "Tocantins/TO", "D. Federal/DF",
                      ]
        self.entry_estado = AutocompleteEntry(self.root, font=('arial', 13, 'bold'), completevalues=self.estado)
        self.entry_estado.place(x=470, y=225, width=198, height=25)

# Entry Telefone
        self.entry_telefone = Entry(self.root, bg=self.et_bg_branco, fg=self.et_fg_preto, font=self.et_font)
        self.entry_telefone.place(x=472, y=290, width=198, height=25)

# Entry Botão Inserir data da Consulta
        self.lb_dataConsulta = Button(self.root, text='Inserir data da consulta', bg=self.bt_bg, fg=self.bt_fg, font=self.bt_font, command=self.data_consulta)
        self.lb_dataConsulta.place(x=730, y=80, width=240, height=28)

# Entry Data de Nascimento
        self.entry_nascimento = Entry(self.root, font=('arail', 15, 'bold'))
        self.entry_nascimento.place(x=835, y=160, width=105, height=25)

# Text Observações
        self.entry_observacao = Text(self.root, bg=self.lb_bg, fg=self.lb_fg, font=self.et_font)
        self.entry_observacao.place(x=23, y=420, width=1240, height=78)

# Text Recomendações Terapêuticas
        self.entry_receita = Text(self.root, bg=self.lb_bg, fg=self.lb_fg, font=self.et_font)
        self.entry_receita.place(x=693, y=233, width=330, height=140)

# Botão Data Niver
        self.bt_calendario = PhotoImage(file='dataNiver.png')
        self.bt_calendario = self.bt_calendario.subsample(3,3)
        self.bt_calendario1 = Label(self.root, image=self.bt_calendario)
        self.bt_calendario1.image = self.bt_calendario

        self.bt_calendario = Button(self.root, image=self.bt_calendario, bg=self.lb_bg, activebackground=self.lb_bg, bd=0, highlightthickness=0, command='')
        self.bt_calendario.place(x=795, y=145)

# Botão Saida do Sistema
        self.sairSistema = PhotoImage(file='sairSistema.png')
        self.sairSistema = self.sairSistema.subsample(5,5)
        self.sairSistema1 = Label(self.root, image=self.sairSistema)
        self.sairSistema1.image = self.sairSistema

        self.sairSistema = Button(self.root, image=self.sairSistema, bg=self.lb_bg, activebackground=self.lb_bg, bd=0, highlightthickness=0, command=self.sair)
        self.sairSistema.place(x=1280, y=5)

# Botão Limpar Receita
        from botoes_image import deletando

        self.bt_limpa_receita = PhotoImage(data=base64.b64decode(deletando))
        self.bt_limpa_receita = self.bt_limpa_receita.subsample(6, 6)
        self.bt_limpa_receita1 = Label(self.root, image=self.bt_limpa_receita)
        self.bt_limpa_receita1.image = self.bt_limpa_receita

        self.bt_limpa_receita = Button(self.root, bg=self.bt_bg, fg=self.bt_fg, image=self.bt_limpa_receita, activebackground=self.bt_bg, bd=0, highlightthickness=0, command='', relief=FLAT)
        self.bt_limpa_receita.place(x=985, y=333, width=38, height=40)

#Botão Revisão
        from botoes_image import revisao

        self.revisao = PhotoImage(data=base64.b64decode(revisao))
        self.revisao = self.revisao.subsample(6, 6)
        self.revisao1 = Label(self.root, image=self.revisao)
        self.revisao1.image = self.revisao

        self.revisao = Button(self.root, bg=self.bt_bg, fg=self.bt_fg, image=self.revisao,
                                       activebackground=self.bt_bg, bd=0, highlightthickness=0, command='', relief=FLAT)
        self.revisao.place(x=175, y=320, width=55, height=70)


# Botão Consulta
        from botoes_image import consulta

        self.consulta = PhotoImage(data=base64.b64decode(consulta))
        self.consulta = self.consulta.subsample(6, 6)
        self.consulta1 = Label(self.root, image=self.consulta)
        self.consulta1.image = self.consulta

        self.consulta = Button(self.root, bg=self.bt_bg, fg=self.bt_fg, image=self.consulta,
                              activebackground=self.bt_bg, bd=0, highlightthickness=0, command='', relief=FLAT)
        self.consulta.place(x=360, y=320, width=55, height=70)

# Botão Consulta
        from botoes_image import whatsapp

        self.whatsapp = PhotoImage(data=base64.b64decode(whatsapp))
        self.whatsapp = self.whatsapp.subsample(3, 3)
        self.whatsapp1 = Label(self.root, image=self.whatsapp)
        self.whatsapp1.image = self.whatsapp

        self.whatsapp = Button(self.root, bg=self.bt_bg, fg=self.bt_fg, image=self.whatsapp,
                               activebackground=self.bt_bg, bd=0, highlightthickness=0, command='', relief=FLAT)
        self.whatsapp.place(x=535, y=320, width=55, height=70)


# Botão Limpar
        from botoes_image import limpar

        self.bt_limpar = PhotoImage(data=base64.b64decode(limpar))
        self.bt_limpar = self.bt_limpar.subsample(13, 13)
        self.bt_limpar1 = Label(self.root, image=self.bt_limpar)
        self.bt_limpar1.image = self.bt_limpar

        self.bt_limpar = Button(self.root, bg=self.bt_bg, fg=self.bt_fg, image=self.bt_limpar,
                               activebackground=self.bt_bg, bd=0, highlightthickness=0, command='', relief=FLAT)
        self.bt_limpar.place(x=175, y=605, width=80, height=120)



    def data_consulta(self):
        self.dia_atual = (datetime.today().strftime('%d/%m/%Y'))
        self.TextoLabel = StringVar()
        self.TextoLabel.set(self.dia_atual)

        self.entry_dataConsulta = Entry(self.root, textvariable=f'{self.TextoLabel}', bg=self.lb_bg, fg='yellow', font=('arial', 18, 'bold'), relief=FLAT)
        self.entry_dataConsulta.place(x=780, y=112, width=120, height=35)

    def sair(self):
        self.root.destroy()
        sys.exit()

    def grid_cliente2(self):
        self.lista_grid2 = ttk.Treeview(self.root, columns=('col1', 'col2'))

        self.lista_grid2.heading('#1', text='CÓDIGO')
        self.lista_grid2.heading('#2', text='NOME')

        self.lista_grid2.column('#0', width=0)
        self.lista_grid2.column('#1', width=60)
        self.lista_grid2.column('#2', width=120)
        self.lista_grid2.place(x=1055, y=120, width=210, height=290)

        self.delete_grid2 = Button(self.root, text='DELETAR ITEM', bg='red', fg='#ffffff', font=('arial', 10, 'bold'), command='')
        self.delete_grid2.place(x=1055, y=378, width=210, height=35)

    def grid_cliente(self):
        self.lista_grid = ttk.Treeview(self.root, columns=('col1', 'col2', 'col3','col4', 'col5', 'col6','col7', 'col8', 'col9','col10', 'col11', 'col12', 'col13', 'col14'))

        self.lista_grid.heading('#1', text='CÓDIGO')
        self.lista_grid.heading('#2', text='NOME')
        self.lista_grid.heading('#3', text='E.CIVÍL')
        self.lista_grid.heading('#4', text='RELIGIÃO')
        self.lista_grid.heading('#5', text='PROFISSÃO')
        self.lista_grid.heading('#6', text='CIDADE')
        self.lista_grid.heading('#7', text='ESTADO/UF')
        self.lista_grid.heading('#8', text='TELEFONE')
        self.lista_grid.heading('#9', text='D.CONSULTA')
        self.lista_grid.heading('#10', text='NASCIMENTO')
        self.lista_grid.heading('#11', text='IDADE')
        self.lista_grid.heading('#12', text='TIPO')
        #self.lista_grid.heading('#13', text='CÓDIGO')
        #self.lista_grid.heading('#14', text='CÓDIGO')

        self.lista_grid.column('#0', width=0)
        self.lista_grid.column('#1', width=60)
        self.lista_grid.column('#2', width=120)
        self.lista_grid.column('#3', width=90)
        self.lista_grid.column('#4', width=90)
        self.lista_grid.column('#5', width=120)
        self.lista_grid.column('#6', width=150)
        self.lista_grid.column('#7', width=90)
        self.lista_grid.column('#8', width=100)
        self.lista_grid.column('#9', width=130)
        self.lista_grid.column('#10', width=90)
        self.lista_grid.column('#11', width=50)
        self.lista_grid.column('#12', width=120)
        self.lista_grid.column('#13', width=150)
        self.lista_grid.column('#14', width=150)
        self.lista_grid.place(x=22, y=519, width=1240, relheight=0.14)

principal()

