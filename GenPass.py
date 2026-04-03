import random
import string
import tkinter as tk


janela = tk.Tk()
janela.title("Gerador de senhas")

def gerar_senha(tamanho_pass):
    letras = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letras) for _ in range(tamanho_pass))
    return password

def genpass():
    try:
        tamanho_pass = int(campo.get())
        password = gerar_senha(tamanho_pass)
        resultado.config(text=password)
    except:
        resultado.config(text="não aceito letra >:|")

campo = tk.Entry(janela)
campo.pack()
botao = tk.Button(janela, text="Clique em mim", command=genpass)
resultado = tk.Label(janela, text="")
botao.pack()
resultado.pack()
janela.mainloop()



    #   def genpass(tamanho):
    #         letras = string.ascii_letters + string.digits + string.punctuation
    #         password = ''.join(random.choice(letras) for _ in range(tamanho))
    #         return password

    #     tamanho_pass = int(input("digite o tamanho da senha"))
    #     pass_gensucess = genpass(tamanho_pass)
    #     print(f"senha gerada {pass_gensucess}")



