Nome = []
Niver = []
def dataniver (list = Niver and Nome, w=0):
    while w != 'fim':
        y = str(input('Nome: '))
        x = int(input('Ano de Nascimento: '))
        w = str(input('qualquer tecla para continuar/ digite fim para parar: '))
        Niver.append(x)
        Nome.append(y)


def animal(list = Niver and Nome):
    signos = ['Macaco','Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']
    for i in Niver :
        i= i%12
        print (Nome[i])
        print ('  -> ',signos[i])
        i = 0
    return '.'


print (dataniver())
print (animal())
