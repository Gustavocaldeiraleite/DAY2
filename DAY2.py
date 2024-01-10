text = input('Procurando Nemo.\nDigite uma frase e irei tentar encontrar Nemo')
def findnemo(words):
    number= words.find('Nemo')
    nemo = words.count(' ', 0, number)
    return nemo+1
if 'Nemo' in text:
    print(f'Encontrei Nemo em {findnemo(text)}!.')
else:
    print('não consegui encontrar o Nemo :(')
    