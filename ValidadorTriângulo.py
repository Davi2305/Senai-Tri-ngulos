# Validador de Triângulo

# Apresentação
print('\n\t\t\t -- Validador de Triângulo \n\n')

#Entrada
a1 = float(input('Informe a medida de um dos lados do triângulo: \n'))
a2 = float(input('Informe a medida de mais um dos lados do triângulo: \n'))
a3 = float(input('Informe a medida do último lado do triângulo: \n'))

# Processamento e saída
if a1<a2+a3 and a2<a1+a3 and a3< a1+a2:
    print('\n Os valores {}, {} e {} formam um triângulo!'.format(a1, a2, a3))
else:
    print('\n Os valores {}, {} e {} NÃO formam um triângulo!'.format(a1, a2, a3))