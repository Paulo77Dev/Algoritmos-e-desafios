## Conjunto de funções para uma calculadora.
##----------------------------------- PAULO MADSON 142363------------------------------------------------
## Instruções:
    ## Você deve preencher o código das funções nas posições indicadas.
    ## A resposta deve ser sempre retornada e não "printada".
    ## Nenhuma função pré-definida deve conter input() ou print().
    ## Não é permitido usar nenhum módulo (math, numpy, ...)
    ## Não podem haver erros na execução do código, eles devem ser devidamente tratados.
    ##     Por exemplo, não pode haver uma divisão por zero, nesse caso a função deve 
    ##     retornar None.
    ## Não é permitido trocar o nome das funções ou o número de parâmetros.
    ## Caso seja preciso, você pode declarar outras funções e/ou usar mais de uma linha de return.
##--------------------------------------------------------------------------------------------------------------------
## Função para calcular a soma de dois números reais.
## Ex.: 2.3+3.5=5.8
def soma(x,y):
    x = float(x)
    y = float(y)
    resultado = x+y
    return resultado
##--------------------------------------------------------------------------------------------------------------------
## Função para calcular a subtração de dois reais.
## Ex.: 5.3-2.1=3.2
def subtracao(x,y):
    x = float(x)
    y = float(y)
    resultado = x-y
    return resultado
##--------------------------------------------------------------------------------------------------------------------
## Função para calcular a multiplicação de dois números reais.
## Ex.: 5.3*2.1=11.13
def multiplicacao(x,y):
    x = float(x)
    y = float(y)
    resultado = x*y
    return resultado
##--------------------------------------------------------------------------------------------------------------------
## Função para calcular a divisão de dois números reais.
## Seu código deve tratar erros de divisão por zero.
## Ou seja, se y for igual a zero, a função deve retornar None.
## Ex.: 30.2/10=3.2
## Ex.: 1032/0=None ## ERRO
def divisao(x,y):
    x = float(x)
    y = float(y)
    resultado = x/y
    if y != 0:
        return resultado
    else:
        return None
##--------------------------------------------------------------------------------------------------------------------
## Função para calcular a exponenciação (x^y), onde
## x é um valor real e y deve ser um número inteiro (obs.: ele pode ser negativo).
# Caso o expoente não seja inteiro, a função deve retornar None
# Casos especiais: Zero elevevado a zero é 1.
# Zero elevado a número negativo dá erro, retorna None.

# Dica: Use a função type para testar o tipo de uma variável
# Ex.: if (type(x))==int:
#           print("Inteiro")
## Ex.: 2^3=8
## Ex.: 2^(-3)=0.125
def exponenciacao(x,y):
    x = float(x)
    y = int(y)
    if (type(y))==float:
        return None
    elif y < 0:
        return None
    else:
        resultado = x**y
        return resultado
 ##--------------------------------------------------------------------------------------------------------------------
## Função para calcular o valor de pi. Recebe um inteiro N que representa
## o número de termos da série:
## pi = 4 ( 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)
## Caso N não seja inteiro ou seja menor que zero, a função deve retornar None.
## Ex.: pi(10) = 3.0418396189294032
## Ex.: pi(100) = 3.1315929035585537
def pi(N):
    pi = 1
    for mais in range (5,N*2,4):
        pi = pi + 1/mais
    for menos in range (3,N*2,4):
        pi = pi - 1/menos
    resultado=pi*4
    return resultado
##--------------------------------------------------------------------------------------------------------------------
## Função para calcular o fatorial de um número x,
# onde x é um valor inteiro e maior ou igual a zero,
# caso contrário, a função deve retornar None.
# Lembre que fatorial de zero é 1. 
# Ex.: 10!=3628800
def fatorial(x):
    x = int(x)
    if x < 0:
        return None
    elif x == 0:
        return 1 
    elif x > 0:
        a = 1
        for i in range (1,x+1):
            a = a*i
            resultado = a
        return resultado
##--------------------------------------------------------------------------------------------------------------------
## Função para calcular o número de permutações de dois números Permutacao(n,p)=n!/(n-p)!,
# onde n é um número inteiro não negativo e p é um número inteiro e deve ser maior 
# ou igual a 0 e menor ou igual a n, caso contrário, a função deve retornar None
# Dica: Use a função fatorial declarada acima.
# Ex.: P(10,5)=30240
def permutacao(n,p):
    n = int(n)
    p = int(p)
    if p < 0 or p > n:
        return None 
    else:
        a = 1
        for i in range (1,n+1):
            a = a*i
        b = 1 
        for y in range (1,n-p+1):
            b = b*y
        resultado=int(a/b)
        return resultado
###--------------------------------------------------------------------------------------------------------------------
##Função para calcular o número de combinações de dois números Combinacao(n,p)=n!/((n-p)! * p!),
# onde n é um número inteiro não negativo e p é um número inteiro e deve ser maior 
# ou igual a 0 e menor ou igual a n, caso contrário, a função deve retornar None.
# Dica: Use a função fatorial declarada acima.
# Ex.: C(10,5)=252
def combinacao(n,p):
    n = int(n)
    p = int(p)
    if n < 0:
        return None
    if p < 0 or p > n:
        return None 
    else:
        a = 1
        for i in range (1,n+1):
            a = a*i
        b = 1 
        for y in range (1,n-p+1):
            b = b*y
        c = 1 
        for z in range (1,p+1):
            c = c*z 
        resultado=(int(a/(b*c)))
        return resultado
##--------------------------------------------------------------------------------------------------------------------
## Função para calcular o somatório de todos os valores entre dois números inteiros (inclusive).
# Caso o primeiro número seja maior que o segundo, o resultado deve ser zero.
# Caso o primeiro número seja igual ao segundo, o resultado deve ser igual ao primeiro número.
# Caso contrário, fazer a soma de todos os valores do intervalo.
# Deve retornar None caso os valores não sejam inteiros.
# Ex.: Sum(1,10)=55
def somatorio(i,f):
    if i > f:
        return 0
    if i == f:
        return i
    if (type(i))==float:
        return None
    if (type(f))==float:
        return None
    else:
        somar = 0
         for z in range (i,f+1):
            somar = somar + z
        resultado = somar
        return resultado
##--------------------------------------------------------------------------------------------------------------------
## Função para calcular o número de Euler elevado a x (e^x ou expˆx), 
## onde x é um número real.
## A função deve calcular 100 termos da série:
## e^x = x^0/0!+x^1/1!+x^2/2!+x^3/3!+...
## Ex.: exp(1)==2.7182818285
## Ex.: exp(0)==1
## Ex.: exp(-1)==0.3678794412
def exp(x):
    fat = 1
    n = 1
    for i in range (1,99):
        fat = fat*i
        n += (x**i)/fat
    resultado = n
    return resultado
##--------------------------------------------------------------------------------------------------------------------
## Função para calcular o logaritmo neperiano (ln x ou log_e x)
## onde x é um real maior que zero.
## A função deve calcular 100 termos da série:
## ln x = 2*((x-1)/(x+1))*(  1/1*((x-1)/(x+1))^0 + 1/3*((x-1)/(x+1))^2 + 1/5*((x-1)/(x+1))^4 + ... )
##
## Ex.: ln(exp(x))==x
## Ex.: ln(1)==0
## Ex.: ln(2)==0.6931471806
## Ex.: ln(3)==1.0986122887
## Ex.: ln(10)==2.302585093
def ln(x):
    n=0
    b=0
    if x < 0:
        return None
    else:
        for i in range(0,100):
            b+=(1/((2*i)+1))*((x-1)/(x+1))**(i*2)
    n=b*(2*((x-1)/(x+1)))
        resultado = n
    return resultado
##--------------------------------------------------------------------------------------------------------------------
## Função para calcular a exponenciação com números reais no expoente (x^y),
## onde x é um número real maior que zero e y é um número real.
## A função ser calculada pela fórmula: 
##   x^y = exp(y*ln(x))
## Dica: Use as funções declaradas acima.
## Ex.: 2^(3.5)=11.313708499
def superExponenciacao(x,y):
    if x > 0:
        xy = x**y
        resultado = xy
        return resultado
    else:
        return None
##--------------------------------------------------------------------------------------------------------------------
## Função para calcular a raiz quadrada de um número real não negativo x.
## Use a função superExponenciação acima ou faça um algoritmo iterativo
## (tentativa e erro) para descobrir a 
## a raiz quadrada. Considere que pode haver erro de até 0.00001.
## Ex.: raiz(4) = 2 ## Erro de +/- 0.00001
## Ex.: raiz(4.41) = 2.1 ## Erro de +/- 0.00001
    def raizQuadrada(x):
    if x < 0:
        return None
    else:
        n = (x**(0.5))
        resultado=n
    return resultado
    ##--------------------------------------------------------------------------------------------------------------------