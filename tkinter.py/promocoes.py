import tkinter as tk


def  abrir_janela():
    janela2 = tk.Toplevel()
    janela2.title('janela nova')
    botao_fechar = tk.Button(janela2 , text = "fechar" , command= janela2.destroy)
    botao_fechar.grid(row=1, column=0)

janela = tk.Tk()
botao = tk.Button(janela, text = "ir para outra janela" , command= abrir_janela)
botao.grid(row=2 , column=3)
tk.mainloop()

var_aviao= tk.StringVar()
botao_classeeconomica = tk.Radiobutton(text="classe econômica" , variable= var_aviao , value= "Classe Economica")
botao_classeexecutiva = tk.Radiobutton(text="classe executiva" , variable= var_aviao , value= "Classe Executiva")
botao_primeiraclasse = tk.Radiobutton(text="primeira classe" , variable= var_aviao , value= "Primeira Classe" )
botao_classeeconomica.grid(row=0, column=0)
botao_classeexecutiva.grid(row=0, column=1)
botao_primeiraclasse.grid(row=0,column=2)
tk.mainloop()



var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text="deseja receber e-mail promocionais?", variable = var_promocoes )
checkbox_promocoes.grid(row=0, column = 0)

var_politicas = tk.IntVar()
checkbox_politicas = tk.Checkbutton(text = "aceiter termos de uso e Politicas de privacidade?", variable= var_politicas )
checkbox_politicas.grid(row=1, column = 0)

def enviar():
    if var_politicas.get():
        print('usuario deseja receber promoções')
    else:
        print('usuario não deseja receber promoções')
    if var_politicas.get():
        print('usuario concordou com os termos de uso de politicas de privacidade')
    else:
        print('usuario NÃO concordou')
    
botao_enviar = tk.Button (text = "enviar" , command= enviar)
botao_enviar.grid(row = 1 ,column=0)

def enviar():
    print(var_aviao.get())
botao_enviar = tk.Button (text = "enviar" , command= enviar)
botao_enviar.grid(row = 1 ,column=0)

janela.mainloop()

from tkinter.filedialog import askopenfilename
import pandas as pd

caminho_arquivo= askopenfilename(title=" selecione um arquivo em exel para abrir")
df = pd.read_excel(caminho_arquivo)
print (df)