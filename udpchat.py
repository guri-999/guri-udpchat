#iportações
import socket
import threading
import random
import queue
import random
import os


os.system('clear') or None

escolha = 0
while escolha != 4:
	try:
		print("""	
OPÇÕES:
1. Abrir uma porta(udp)
2. Conectar a uma porta
3. Como funciona?
4. Sair\n""")

		escolha = int(input("O que você quer fazer?"))
	except ValueError:
		print('Escolha invalida. Tente novamente!')


	


	os.system('clear') or None

		#aqui ligamos o servidor***************************************************************************************
	if escolha ==1:		
		messages =queue.Queue()
		clients = []
		server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		server.bind(("localhost", 1024))


		#funcao que roda num thread e recebe todas as mensagens armazenando na fila  de mensagens(queue)
		def receive():
		    while True:
		        try:
		            msg, friend = server.recvfrom(1024)
		            messages.put((msg, friend))
		        except:
		            print("algo deu errado. Erro:", error)

		def broadcast():
		    while True:
		        msg, friend = messages.get()
		        print(msg.decode())
		        if friend not in clients:
		            clients.append(friend)
		        for client in clients:
		            try:
		                if msg.decode().startswith("SIGNUP_TAG:"):
		                    name = msg.decode()[msg.decode().index(':')+':']
		                    server.sendto(f"{name} joined!".encode(), client)
		                else:
		                    server.sendto(msg, client)
		            except:
		                    clients.remove(client)





		t1 = threading.Thread(target=receive)
		t2 = threading.Thread(target=broadcast)

		t1.start()
		t2.start()
		print('porta aberta :)')
		break
#aqui o conectamos ao chat******************************************************************************
		
	elif escolha ==2:		
		client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		client.bind(("localhost", random.randint(1024, 2024)))


		name = input('nicname: ')

		def receive():
		    while True:
		        try:
		            msg , _ = client.recvfrom(1024)
		            print(msg.decode())
		        except:
		            print('algo deu errado. Erro: ', error)



		t = threading.Thread(target=receive)
		t.start()


		client.sendto(f"SIGNUP_TAG:{name}".encode(), ("localhost", 1024))


		while True:
		    msg = input(" ")
		    if msg == "!q":
		        exit()
		    else:
		        client.sendto(f"{name}: {msg}".encode(), ("localhost", 1024))





	elif escolha ==3:
		os.system('clear') or None
		print('''
olá esse codigo faz rodar uma especie de chat que usa o protocolo udp.
Para testar:
1. Execute primeiro a opção 1 que abre uma porta no seu localhost.
(caso queira abrir em outro ip modifique o codigo na linha 31 onde esta escrito localhost e troque para o ip desejado)
2. Abra outro terminal e execute o mesmo codigo.
3. Escolha a 2 opção que faz "ouvir" na porta e possibilita mandar e ver mensagens.

Espero que tenham gostado
meu github: https://github.com/guri-999
			''')

	elif escolha == 4:
		print('Obrigado por usar o codigo/progama. Volte sempre.') 

	else:
		os.system('clear') or None

		print('Escolha invalida. Tente novamente!\n\n\n')
