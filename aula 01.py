# Aprendendo sobre listas

'''
lista1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r = lista1 [0][2]
print(r)
'''
'''
import random
cidades = ['São Paulo', 'Rio de Janeiro', 'Porto Alegre']
escolhido = random.choice(cidades)
print(escolhido)
'''

a = [1, 2, 3]
a.append(15)

b = [7, 8, 9]
for i in b:
    a.append(i)
print(a)