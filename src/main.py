import random
import string

def gerar_senha(tamanho_pass):
    letras = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letras) for _ in range(tamanho_pass))
    return password

def main():
    try:
        tamanho_pass = int(input("Digite o tamanho da senha: "))
        password = gerar_senha(tamanho_pass)
        print(f"Senha gerada: {password}")
    except ValueError:
        print("Letra não é número, somente NÚMEROS seu tolo :|")

if __name__ == "__main__":
    main()



    #   def genpass(tamanho):
    #         letras = string.ascii_letters + string.digits + string.punctuation
    #         password = ''.join(random.choice(letras) for _ in range(tamanho))
    #         return password

    #     tamanho_pass = int(input("digite o tamanho da senha"))
    #     pass_gensucess = genpass(tamanho_pass)
    #     print(f"senha gerada {pass_gensucess}")
    #     print(f"senha gerada {pass_gensucess}")


''