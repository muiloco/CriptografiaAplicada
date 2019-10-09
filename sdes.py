#Parametros de entrada 

texto = "01000001"
chave = "1001011101"

# Vetores de permutação para o S-DES para texto e chave
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
def geradorKs(chave,k1k2):


chave_ip = permutacao(IP,texto)
L0 = chave_ip[:4]
R0 = chave_ip[4:]
