from main import gerar_senha

def test_tamanho_senha():
    senha = gerar_senha(10)
    assert len(senha) == 10


def test_tipo_retorno():
    senha = gerar_senha(5)
    assert isinstance(senha, str)


def test_erro_tamanho_zero():
    try:
        gerar_senha(0)
        assert False, "Deveria ter falhado"
    except AssertionError:
        assert True


def test_contem_elementos():
    senha = gerar_senha(20)

    tem_letra = any(c.isalpha() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_simbolo = any(not c.isalnum() for c in senha)

    assert tem_letra
    assert tem_numero
    assert tem_simbolo