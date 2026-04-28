from src.main import * 

def gerar_senha(tamanho_pass):
    # garante o tipo e valor são válidos
    assert isinstance(tamanho_pass, int), "tamanho_pass deve ser inteiro"
    assert tamanho_pass > 0, "tamanho_pass deve ser maior que zero"
    letras = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(letras) for _ in range(tamanho_pass))

    # garante que a senha gerada tem o tamanho correto
    assert len(password) == tamanho_pass, "Senha gerada com tamanho incorreto"

    # garante que só usamos caracteres permitidos
    for char in password:
        assert char in letras, f"Caractere inválido encontrado: {char}"

    return password

def main():
    try:
        tamanho_pass = int(input("Digite o tamanho da senha: "))

        # Debug antes de chamar a função
        assert tamanho_pass < 10_000, "gosta de senha grande em (pode travar o programa)"

        password = gerar_senha(tamanho_pass)
        print(f"Senha gerada: {password}")

    except ValueError:
        print("Letra não é número, somente NÚMEROS seu tolo :|")
    except AssertionError as e:
        print(f"Erro de validação:/ : {e}")


if __name__ == "__main__":
    main()