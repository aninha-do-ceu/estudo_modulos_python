class Calculadora:

    def soma(a, b):
        return(a + b)

    def subtracao(a, b):
        return(a - b)

    def multiplicacao(a, b):
        return(a*b)

    def divisao(a,b):
        if b == 0:
            return('Erro: Divisor 0')
        else:
            return(a/b)
