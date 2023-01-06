from random import randint
from time import sleep
from os import whaitstatus_to_exitcode
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print ('''Escolha uma opção:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
if jogador >= 3:
    print('JOGADA INVÁLIDA, TENTE NOVAMENTE!')
    whaitstatus_to_exitcode()

    print('...')
sleep(1)
print('PEDRA!')
sleep(1)
print('PAPEL!!')
sleep(1)
print('TESOURA')
sleep(1)

print('-=-' * 11)
print('Computador jogou: {}'.format(itens[computador]))
print('Jogador jogou: {}'.format(itens[jogador]))
print('-=-' * 11)

if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('VOCÊ PERDEU!')
elif computador == 1: #papel
    if jogador == 0:
        print('VOCÊ PERDEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
elif computador == 2: #tesoura
    if jogador == 0:
        print('VOCÊ VENCEU!')
    elif jogador == 1:
        print('VOCÊ PERDEU!')
    elif jogador == 2:
        print('EMPATE!')

