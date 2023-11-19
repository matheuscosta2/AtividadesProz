#  Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
#  O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
#  No início, o programa mostrará a seguinte lista de operações:

#  1: Soma
#  2: Subtração
#  3: Multiplicação
#  4: Divisão
#  0: Sair

#  Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, 
#  o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.
#  Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. 
#  Depois precisa executar a operação e mostrar o resultado na tela. 
#  Quando o usuário escolher a opção “Sair”, o sistema irá parar.
#  É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 
#  Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link 
#  desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

#Variaveis
OperacaoSelecionada = True
#Estrutura de repeticao com condicional que mantem o código executando até que a condição seja obedecida.
while OperacaoSelecionada != False:
     
    print("Bem vindo à calculadora:")
    print("Qual operação deseja fazer?")
    print("1: Soma 2: Subtracao 3: Multiplicacao 4: Divisao 0: Sair")
    TipoOperacao = int(input("Digite o numero da operacao: "))    
    
    def Calcular(Numero1:int, Numero2:int, Operacao:int):
        if Operacao == 1:
            ResultadoCalculo = Numero1 + Numero2
        elif Operacao == 2:
            ResultadoCalculo = Numero1 - Numero2
        elif Operacao == 3:
            ResultadoCalculo = Numero1 * Numero2
        elif Operacao == 4:
            ResultadoCalculo = Numero1 / Numero2
        return ResultadoCalculo
    
    try:
        if TipoOperacao in range (1, 4):           
            Numero1 = int(input("Digite o primeiro número da operacao: "))
            Numero2 = int(input("Digite o primeiro número da operacao: "))
            ResultadoFinal = Calcular(Numero1, Numero2, TipoOperacao)
            print(f"O resultado da operação é: {ResultadoFinal}")
        elif TipoOperacao == 0:
            OperacaoSelecionada = False
            exit()
    except ValueError:
        print("Essa opção não existe, tente novamente.") 
    
    
    
    
