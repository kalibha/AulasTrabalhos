def calcular_idade(ano_nascimento):
    ano_atual = 2022
    return ano_atual - ano_nascimento

def obter_dados_usuario():
    while True:
        try:
            nome_completo = input("Por favor, digite seu nome completo: ")
            ano_nascimento = int(input("Por favor, digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return nome_completo, ano_nascimento
            else:
                print("Erro: O ano deve estar entre 1922 e 2021. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, digite um número válido para o ano.")

nome_usuario, ano_nascimento_usuario = obter_dados_usuario()
idade_usuario = calcular_idade(ano_nascimento_usuario)
print(f"{nome_usuario}, você tem {idade_usuario} anos.")
