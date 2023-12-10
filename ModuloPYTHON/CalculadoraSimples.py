def Calculadorabasica(numero1, numero2, operacao):
    match operacao:
        case 1:
            ResultadoDaSoma = numero1 + numero2
            print("O resultado é: ", ResultadoDaSoma)
        case 2:
            ResultadoDaSubtracao = numero1 - numero2
            print("O resultado é: ", ResultadoDaSubtracao)
        case 3:
            ResultadoDaMultiplicacao = numero1 * numero2
            print("O resultado é: ", ResultadoDaMultiplicacao)
        case 4:
            ResultadoDaDivisao = numero1 / numero2
            print("O resultado é: ", ResultadoDaDivisao) 
        case _:
            print("0")
        
print("- Bem vindo à Calculadora -")

SelecionadorOperacao = int(input("Digite a operacao que deseja executar:Soma = 1 Sub = 2 Mult = 3 Div = 4: " ))
Numero1 = int(input("Digite o primeiro número inteiro da operacao: "))
Numero2 = int(input("Digite o segundo número inteiro da operacao: "))

Calculadorabasica(Numero1, Numero2, SelecionadorOperacao)
