import os

mensagens = []

nome = input("Nome: ")

while True:
    # Limpando terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Exibindo mensagens existentes
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("")

    # Obtendo texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    # Adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })
