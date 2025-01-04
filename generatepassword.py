import random
import string

def gerar_senha(tamanho, mai, minus, num, esp):
    if tamanho < 4:
        raise ValueError("O tamanho da senha deve ser pelo menos 4 para incluir todos os tipos de caracteres.")

    senha = []
    caracteres = ''

    if mai:
        senha.append(random.choice(string.ascii_uppercase))
        caracteres += string.ascii_uppercase
    if minus:
        senha.append(random.choice(string.ascii_lowercase))
        caracteres = string.ascii_lowercase
    if num:
        senha.append(random.choice(string.digits))
        caracteres = string.digits
    if esp:
        senha.append(random.choice(string.punctuation))
        caracteres = string.punctuation

    senha += random.choices(caracteres, k=tamanho - len(senha))

    random.shuffle(senha)

    return ''.join(senha)

