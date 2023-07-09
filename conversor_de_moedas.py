from tkinter import *
from tkinter import ttk
import requests
import json

#t = low/high
t = 'low'

def focus():
	e_valor.focus()

def limpar():
	txt.delete('1.0',END)
	e_valor.delete('0',END)
	focus()
def preencher():
	lis = ['USD','BRL','EUR','BTC']
	return lis

def converter(event=0):

	dindin = e_valor.get()
	if len(dindin)==0:
		dindin='1'
	e = cb_de_moedas.get()
	s = cb_para_moedas.get()

	url = f'https://economia.awesomeapi.com.br/last/{e}-{s}'
	result = requests.get(url).json()
	consulta = []
	for i in result:
		consulta.append(result[i])

	tempo = consulta[0]['create_date']

	bb = float(consulta[0][t])
	x = float(dindin)
	
	soma=abs(bb*x)

	txt.insert(END,f'Data de Cotação {tempo}\n')
	txt.insert(END,f' valor de {e} para {s} R$: {soma:,.2f}\n\n')
	
	focus()


app = Tk()
app.title('Conversor De Moedas')
app.geometry('520x300')
app.configure(pady=10)
app.resizable(0,0)
l_valor = Label(app,text='Valor')
l_valor.grid(row=0,column=0,stick=W)

e_valor = Entry(app)
e_valor.grid(row=0,column=1,stick=W)
e_valor.bind('<Return>',converter)


l_moedas = Label(app,text='Selecione as Moedas Desejadas')
l_moedas.grid(row=1,column=0,columnspan=2,stick=W)



l_de_moedas = Label(app,text='Da_Moedas')
l_de_moedas.grid(row=2,column=0)
moedas = StringVar()
cb_de_moedas = ttk.Combobox(app,textvariable=moedas)
cb_de_moedas['values'] = preencher()
cb_de_moedas.current(0)
cb_de_moedas.grid(row=2,column=1,stick=W)


l_para_moedas = Label(app,text='Para_Moedas')
l_para_moedas.grid(row=2,column=2)
cb_para_moedas = ttk.Combobox(app)
cb_para_moedas['values'] = preencher()
cb_para_moedas.current(1)
cb_para_moedas.grid(row=2,column=3,stick=W)


frame_text = Frame(app)
frame_text.grid(row=3,column=0,columnspan=4)
txt = Text(frame_text,width=60,height=10)
txt.grid(row=0,column=0,stick=W)


sc = ttk.Scrollbar(frame_text,orient='vertical')
txt['yscrollcommand'] = sc.set
sc.config(command=txt.yview)


sc.grid(row=0,column=1,stick=NS)


frame_btn = Frame(app)
frame_btn.grid(row=4,column=0)

btn_limpar = Button(frame_btn,text='Limpar',command=limpar)
btn_limpar.grid(row=0,column=0,stick=W)


btn_converter = Button(frame_btn,text='Converter',command=converter)
btn_converter.grid(row=0,column=1,stick=W)



btn_sair = Button(frame_btn,text='Sair',command=app.destroy)
btn_sair.grid(row=0,column=2,stick=W)

app.mainloop()
