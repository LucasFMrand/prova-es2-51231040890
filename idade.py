MINIMA = 12  # TROQUE pelo seu LIMITE


def idade_permitida(idade):
    if not isinstance(idade, int) or isinstance(idade, bool):
        return False
    if idade > 100:
        return False
    return idade >= MINIMA
