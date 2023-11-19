# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

#Primeiro declarei as funções:

#funcao validar se o nome é uma string e se contem somente letras e espaços.
def validar_nome(nome):
    if not isinstance(nome, str):
        raise ValueError ("O nome pode ")
    if not nome.replace (" ", "").isalpha():
        raise ValueError ("O nome deve apenas conter letras e espacos")
    return nome.strip()
#funcao validar ano valida se é um nomero inteiro e se está no range correto
def validar_ano(ano):
    if not isinstance (ano, int):
        raise ValueError ("O ano deve conter apenas numeros inteiros")
    if (ano <= 1922 and ano >= 2023):
        raise ValueError ("O ano tem de estar entre 1922 e 2023")
    else:
        return ano
#funcao calcular idade que subtrai o ano de nascimento pelo ano atual
def calcular_idade(ano):
    idade = 2023 - ano
    return idade

#Funcao principal da aplicação, ela inicia o programa e é executada caso haja alguma exception nas validações de nome e ano
def main ():
    #esta validação é diferente da validação de ano pois numeros podem ser strings mas letras não podem ser inteiros, a validação numerica é mais
    nome = input("Digite seu nome completo: ", )
    try:
        nome = validar_nome(nome)
    except ValueError as erro:
        print(erro)
        return main()
    
    ano = input("Digite o ano de nascimento: ")
    try:
        #neste caso valido o nome somente tipando o dado ou seja tentando converte-lo, caso ele não seja inteiro
        #nao  será compatível com a conversão e vai retornar false e entrará no bloco da exception
        ano = int(ano)
    except ValueError:
        print("O ano deve conter apenas numeros inteiros")
    try:
        ano = validar_ano(ano)
    except ValueError as erro:
        print(erro)
        return(main)

    idade = calcular_idade(ano)
    print("Seu nome é", nome,"e sua idade é", idade)
    
main()
