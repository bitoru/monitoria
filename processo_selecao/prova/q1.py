# Prova de Monitoria para Fundamentos da Computacao
# Questao #1
# Aluno: Vitor Fernandes

# caso o numero seja triangular, retorna os 3 inteiros positivos
# consecutivos que, multiplicados, sao iguais ao numero informado
# caso contrario, retorna None
def numero_triangular(numero):
    # loop percorrendo todos os inteiros, a partir do 3 ate o numero informado
    for i in range(3, numero+1):
        # verifica se os 3 inteiros i, i-1 e i-2 multiplicados eh igual ao numero informado
        if i*(i-1)*(i-2) == numero:
            # caso o numero seja triangular, retorna os inteiros que o tornam triangular
            return [i-2, i-1, i]
    # caso o loop encerre sem retornar nada, o numero nao eh triangular
    return None

# pede ao usuario que informe um numero inteiro nao-negativo e retorna o mesmo
def ler_numero():
    # bloco try-except para validar se o numero eh inteiro
    try:
        # pede ao usuario o numero
        numero = input('Digite um numero para validar se eh triangular ou nao: ')
        # tenta converter o valor digitado em um inteiro
        # caso nao seja um valor inteiro, ira lancar uma excecao,
        # caindo no bloco except abaixo
        inteiro = int(numero)
        # o inteiro deve ser nao-negativo
        # caso seja negativo, pede novamente ao usuario que digite um valor
        # utilizamos recursao para manter o codigo mais limpo
        if inteiro < 0:
            print('O inteiro deve ser nao-negativo')
            return ler_numero()
        return inteiro
    except:
        # bloco de excecao
        # caso o valor digitado nao seja um numero inteiro, exibe a mensagem de erro
        print('O valor deve ser um numero inteiro nao-negativo')
        # pede-se novamente ao usuario que digite um valor, utilizando recursao
        return ler_numero()

# le o numero e recupera os fatores que o fazem ser triangular
numero = ler_numero()
fatores = numero_triangular(numero)

if fatores is None:
    # caso o numero nao seja triangular, o valor de "fatores" sera "None"
    print('O numero', numero, 'nao eh triangular')
else:
    # caso o numero seja triangular, a variavel "fatores"
    # ira conter os numeros que, multiplicados, sao iguais ao numero informado
    print('O numero', numero, 'eh triangular')
    print('Seus fatores sao:', fatores, 'pois', fatores[0], '*', fatores[1], '*', fatores[2], '=', numero)
