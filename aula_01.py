"""ex 1
carrinho = []

carrinho.append(("produto 1",20.0))
carrinho.append(("produto 2",40.0))
carrinho.append(("produto 3",8050))

total = sum((v[1] for v in carrinho))


print(total)
"""


""" ex 2"""
"""cidade = ["teste","teste3","teste5",'12321']
estado = ["1",'2','3']
from itertools import zip_longest
for indice in zip_longest(cidade,estado):
    print(indice)"""

"""ex 3"""

"""from itertools import combinations, permutations, product, groupby

alunos = [
    {"nome":"joao","nota":'A'},
    {"nome":"joao","nota":'A'},
    {"nome":"eufranio","nota":'C'},
    {"nome":"eufranio2","nota":'B'},
    {"nome":"eufranio3","nota":'D'},
    {"nome":"eufranio5","nota":'D'}
]
alunos.sort(key=lambda item: item["nota"])

agrupado = groupby(alunos, lambda item: item["nota"])
for grupo,valores_agrupados in agrupado:
    print(len(list(valores_agrupados)))"""


produtos = [
    {"nome":"p1","preco":10},
    {"nome":"p2","preco":90},
    {"nome":"p3","preco":80},
    {"nome":"p4","preco":10},
    {"nome":"p5","preco":70},
    {"nome":"p6","preco":20},
    {"nome":"p7","preco":15},
]

pessoa = [
    {"nome":"joao","idade":15},
    {"nome":"joao","idade":20 },
    {"nome":"eufranio","idade":30},
    {"nome":"eufranio2","idade":35},
    {"nome":"eufranio3","idade":15},
    {"nome":"eufranio5","idade":18}
]


lista = [1,2,3,4,5,6,7,8,9,10]
"""
nova_lista = map(lambda x: x*2, lista)
print(lista)
print('===========')
print(list(nova_lista))
nova_lista = list(( x*2 for x in lista))

print('=====')
print('=====')
print(nova_lista)

novo_produto = map(lambda produto: produto["nome"]+" - "+str(produto["preco"] * 2),produtos)
print(novo_produto)"""

# nova_lista = [numero for numero in lista if numero > 5]
# for x in nova_lista:
#     print(x)

# nova_lista = [produto for produto in produtos if produto["preco"] >= 80]
# for x in nova_lista:
#     print(x)
#
# from functools import reduce
# soma_lista = reduce(lambda contador,produto:contador + produto["preco"],produtos,0)

# print(soma_lista)