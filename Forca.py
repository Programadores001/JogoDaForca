import os, sys
from time import sleep

acertos = []
chances = 6

B, R, Y, G, N = '\33[94m', '\033[91m', '\33[93m', '\033[1;32m', '\033[0m'

def log():
	os.system('clear')
	print('''
{0}$$$$$$$$\                                         
$$  _____|                                        
$$ |       $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$\  
$$$$$\    $$  __$$\ $$  __$$\ $$  _____| \____$$\ 
$$  __|   $$ /  $$ |$$ |  \__|$$ /       $$$$$$$ |
$$ |      $$ |  $$ |$$ |      $$ |      $$  __$$ |
$$ |      \$$$$$$  |$$ |      \$$$$$$$\ \$$$$$$$ |
\__|       \______/ \__|       \_______| \_______|{0}
'''.format(G,N))
	string = '{0}Diga para seu amigo nao olhar enquanto digita a palavra secreta'.format(B)
	up = string.upper()
	for o in range(len(string)):
		l = '\r' + string[0:o] + up[o] + string[o+1:] + '\r'
		sys.stdout.write(l)
		sys.stdout.flush()
		sleep(0.1)
	global dica, palavra, tam
	dica = str(input('\n\n{0}Digite a Dica: '.format(N)))
	palavra = str(input('\nDigite a Palavra Secreta: ')).strip().lower()
	tam = len(palavra)
	k = palavra.split()
	palavra = ''.join(k)
	print('\n'*100)
	os.system('clear')

if __name__ == '__main__':
	log()
	erros = 0
	while True:
		for x in range(5):
			print()
		print('{0}Para Concluir o Jogo Digite a Palavra Inteira!{1}   \n\n'.format(Y,N))
		secreta = ''
		for i in palavra:
			secreta += i if i in acertos else '-'
		print('Dica Do Jogo: {0}{1}{2}'.format(B,dica,N))
		print('Chances: {0}%i{1}\n'.format(B,N) %(chances))
		print('Tamanho da Palavra: {0}%i{1}'.format(B,N) %(tam))
		print('Palavra Chave: ', secreta)
		tenta = input('\n\nDigite uma letra/Palavra: ').strip().lower()
		if tenta == 'sair':
			exit(1)
		if tenta == palavra:
			print('{0}Parabens voce venceu!{1}'.format(G,N))	
			break
		elif tenta not in palavra:
			chances-=1
			if chances == 5:
				print('\n'*100)
				print(' ____   ')
				print('|    |  ')
				print('|    O  ')
				print('|       ')
				print('|       ')
				print('|       ')
			if chances == 4:
				print('\n'*100)
				print(' ____   ')
				print('|    |  ')
				print('|    O  ')
				print('|   /   ')
				print('|       ')
				print('|       ')
			if chances == 3:
				print('\n'*100)
				print(' ___   ')
				print('|    |  ')
				print('|    O  ')
				print('|   /|  ')
				print('|       ')
				print('|       ')
			if chances == 2:
				print('\n'*100)
				print(' ____   ')
				print('|    |  ')
				print('|    O  ')
				print('|   /|\ ')
				print('|       ')
				print('|       ')
			if chances == 1:
				print('\n'*100)
				print(' ____   ')
				print('|    |  ')
				print('|    O  ')
				print('|   /|\ ')
				print('|   /   ')
				print('|       ')
			if chances == 0:
				print('\n'*100)
				print(' ____   ')
				print('|    |  ')
				print('|    {0}O{1}  '.format(R,N))
				print('|   {0}/|\{1} '.format(R,N))
				print('|   {0}/ \{1} '.format(R,N))
				print('|       ')		
				print('Sua Chances acabaram :(')
				break
		elif tenta in palavra:
			print('\n'*100)
			print('{0}Good!'.format(G))
			acertos += tenta
			continue
print('Palavra Secreta eh: {0}{1}'.format(G,palavra))
