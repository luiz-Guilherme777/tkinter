import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("cotação de moedas",)
janela.rowconfigure(0,weight=1)
janela.columnconfigure(0,weight=1)

mensagem = tk.Label(text = "sistema de busca de cotação de Moedas", fg='white', bg='#111111' , width=40 , height= 5)
mensagem.grid(row=0, column=0 , columnspan= 2 , sticky="new")


mensagem2 = tk.Label(text = "selecione a Moeda desejada")
mensagem2.grid(row=1, column=0)



caixa_texto = tk.Text(width = 10 , height = 5)
caixa_texto.grid(row= 5, column = 0, sticky = 'nswe')

dicionario_cotacoes = {
    'dolar':5.47,
    'euro':6.89,
    'bitcoin':20.000
}



def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text = 'cotação não encontrada')
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f'cotação do {moeda_preenchida} é de R${cotacao_moeda} reais'

botao = tk.Button(text= "buscar cotação" , command=buscar_cotacao)
botao.grid(row=2, column= 1 )

mensagem3=tk.Label(text = "caso queira pagar mais de uma otação ao mesmo tempo digite")
mensagem.grid(row=4, column=0 , columnspan= 3) 

#moeda = tk.Entry()
#moeda.grid(row=1, column=1)
moedas = list(dicionario_cotacoes.keys())
moeda = ttk.Combobox(janela,values = moedas)
moeda.grid(row=1, column = 1)


mensagem_cotacoes = []
def buscar_cotacoes():    
    texto = caixa_texto.get("1.0" , tk.END)
    lista_moedas = texto.split('\n')
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f'{item}:{cotacao}')
    mensagem4 = tk.Label(text = '\n'.join(mensagem_cotacoes))
    mensagem4.grid(row= 6, column = 1)

botao_multiplacotacoes = tk.Button(text = "buscar cotações", command= buscar_cotacoes)
botao_multiplacotacoes.grid(row=5 , column= 1 )

janela.mainloop()
