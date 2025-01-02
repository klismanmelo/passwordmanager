import random
import string

def gerar_senha(tamanho):
    if tamanho < 4:
        raise ValueError("O tamanho da senha deve ser pelo menos 4 para incluir todos os tipos de caracteres.")

    caracteres = string.ascii_letters + string.digits + string.punctuation

    senha = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    senha += random.choices(caracteres, k=tamanho - 4)

    random.shuffle(senha)

    return ''.join(senha)

