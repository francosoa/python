#uma função pode ser vazia, sem nenhuma ação:

def noaction():
    """
    :return: Não retorna nada
    """
    pass

#Posso utilizar uma função para fazer uma rotina básica, como colocar divisórias:

def divide():
    """
    :return: Função retorna um print de 30 riscos para separar contextos
    """
    return print("-" *30)

divide()


#Funções recebendo parâmetros:
#Abaixo temos uma função não obrigatória

def find_the_letter(name=None):
    """
    Verifica se o parametro passado tem a letra o ou a
    :param name: String
    :return: --
    """
    if 'a' or 'o' in name:
        print('This name got a vogal')
    if name == None:
        print("This app is empty")

find_the_letter()


#Posso utilizar a saída de uma função como a entrada de outra função:

def somar(numero_1, numero_2):
    """
    Essa função tem o objetivo de realizar a soma\
    de dois número
    :param numero_1: Recebe o numero de 0 até infinito
    :param numero_2: Recebe o numero de 0 até infinito
    :return: numero_1 + numero_2
    """
    soma_total = numero_1 + numero_2
    return soma_total

def dividir(entrada, saida, divisao):
    divisao = somar(entrada, saida) / divisao
    return divisao

def condicoes(cond1, cond2, cond3):
    condicional = dividir(cond1, cond2, cond3)
    if condicional >= 100:
        print(f'The value is {int(condicional)} you are good')
    elif condicional < 100:
        print('You are not so good')
    else:
        print('The input is not valid')

condicoes(100,300,2)
