afnd = {}

estados = input().split(" ")
for estado in estados:
    afnd[estado] = {}

simbolos = input().split(" ")
nTransicoes = int(input())

for i in range(0,nTransicoes):
    o, c, d = input().split(" ")
    if c not in afnd[o]:
        afnd[o][c] = []
    afnd[o][c].append(d)

estadoInicial = input()
estadosFinais = input().split(" ")
palavras = input().split(" ")

def testaPalavra(palavra):
    estadoAtual = [estadoInicial]
    pValida = False
    
    for letra in palavra:
        destinos = []
        for i in estadoAtual:
            if(afnd[i].get(letra)):
                for j in range(0,len(afnd[i][letra])):
                    if(afnd[i][letra] not in destinos):
                        destinos.append(afnd[i][letra][j])
        estadoAtual = destinos
    for i in estadoAtual:
        if i in estadosFinais:
            pValida = True
    return pValida

for palavra in palavras:   
    if  testaPalavra(palavra):
        print('S')
    else:
        print('N')