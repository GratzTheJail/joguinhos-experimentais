# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 14:58:44 2022

@author: Gratz The Jail
"""
#módulos
import random

#funcoes
def colocarLetra(palavra,letra):
    lpalavra = list(palavra)
    lpalavra[ind*2] = letra 
    palavra = ''.join(lpalavra)
    return palavra

#criando uma lista com todas as palavras
arqEntDic = open('C:/Users/guiga/Documents/Pussy/PROG - PUC/DIC.PAL','r')
lpalavras = []
totalDePalavras = 206

for linha in arqEntDic:
    linha = linha.strip()
    lpalavras.append(linha)
arqEntDic.close()

#escolhendo a palavra aleatoriamente + variaveis
palavra = lpalavras[random.randint(0,205)]
espaçoEscrever = '_ '*len(palavra)
letrasJaUsadas = ''
print(palavra)

#Primeira exibição!
print('J O G O   D A   A D I V I N H A Ç Ã O\n')
print('Você tem 10 chances para acertar a palavra\n')
print('\t\t\t\tPalavra sorteada\t\tLetras já utilizadas\n')
print('\t\t\t\t'+espaçoEscrever)

#entrada (10 tentativas)
cont=0
while cont < 10:
    if '_' in espaçoEscrever:
        letraDig=input('%da. tentativa: ' %(cont + 1)).upper()
        
        if len(letraDig) == 1:
            if not letraDig in espaçoEscrever and not letraDig in letrasJaUsadas:
                for ind,letra in enumerate(palavra):
                    if letra == letraDig:
                        espaçoEscrever = colocarLetra(espaçoEscrever, letra)
                letrasJaUsadas+= letraDig
                print(f'\n\t\t\t\t{espaçoEscrever}\t\t\t{letrasJaUsadas}')
                cont+=1
            else:
                print('\nVoce ja tentou esta letra! Tente novamente...')
                
        elif len(letraDig) > 1:
            if letraDig.upper() == palavra:
                for ind,letra in enumerate(letraDig):
                    espaçoEscrever = colocarLetra(espaçoEscrever, letra)
                cont = 10
            else:
                print("\nPalavra errada! Tente novamente...")
                cont += 1
    else:
        cont+=1
if not '_' in espaçoEscrever:
    print(f'\n\n\t\t\t\t{espaçoEscrever}\t\t\t{letrasJaUsadas}')
    print('\n\nParabéns! Você acertou a palavra! :^) <3'.upper())
else:
    print('\n\n\nQue falta de sorte! Tente novamente mais tarde!')
    print('\nA palavra era %s' %palavra)