import csv

# E
usuarios = []

with open("usuarios.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        usuarios.append(linha)

# T
for usuario in usuarios:
    mensagem = f"""
Olá {usuario['nome']}!

Sua conta {usuario['conta']} está ativa.
Aproveite nossos benefícios exclusivos!

"""
    usuario["mensagem"] = mensagem.strip()

# L 
with open("mensagens.csv", "w", newline="", encoding="utf-8") as arquivo_saida:
    campos = ["nome", "conta", "cartao", "mensagem"]
    escritor = csv.DictWriter(arquivo_saida, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(usuarios)

print("ETL finalizado com sucesso!")
