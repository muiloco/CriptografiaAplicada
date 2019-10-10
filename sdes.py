#Parametros de entrada 

texto = "01000001"
chave = "1001011101"

# Vetores de permutação para o S-DES para texto e chave e matrizes para parte da operacao
P4 = (2,4,3,1)
P8 = (6,3,7,4,8,5,10,9)
P10 = (3,5,2,7,4,10,1,9,8,6)
IP = (2,6,3,1,4,8,5,7)
iIP = (4,1,3,5,7,2,8,6)
EP = (4,1,2,3,2,3,4,1)
S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]

# funcao de permucao de algo com um dos vertores de permutacao
def permutacao(permut,chave):
    textoPermutado = ""
    for i in permut:
        textoPermutado += chave[i-1]
    return textoPermutado

# funcoes de geracao de chaves K1 e K2
def movimentoCircular(chave,qntMov):
    i = 0
    while i <= qntMov:
        a = chave[0]
        chave.replace(chave[0],chave[4])
        chave.replace(chave[4],a)
        i += 1
    return chave

def geradorKs(key):
    k1 = permutacao(P10,key)
    C0 = movimentoCircular(k1[:5],1)
    D0 = movimentoCircular(k1[5:],1)
    k1 = C0+D0
    k1 = permutacao(P8, k1)
    k2 = movimentoCircular(C0,2) + movimentoCircular(D0,2)
    k2 = permutacao(P8, k2)
    return k1,k2

chave_ip = permutacao(IP,texto)
L0 = chave_ip[:4]
R0 = chave_ip[4:]
k1,k2 = geradorKs(chave)
ep = permutacao(EP,R0)
#ep_xor_k1 =
k1[0] = k1[1]
print(k1) 
