from idade import idade_permitida


def test_rf01_idade_exatamente_12_e_aceita():
    # Preparar
    idade = 12
    # Agir
    resultado = idade_permitida(idade)
    # Verificar
    assert resultado is True


def test_rf02_idade_11_abaixo_do_limite_e_rejeitada():
    # Preparar
    idade = 11
    # Agir
    resultado = idade_permitida(idade)
    # Verificar
    assert resultado is False


def test_rf03_idade_101_acima_de_100_e_rejeitada():
    # Preparar
    idade = 101
    # Agir
    resultado = idade_permitida(idade)
    # Verificar
    assert resultado is False
