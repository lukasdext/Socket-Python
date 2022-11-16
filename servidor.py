import socket

HOST = 'localhost'   ##trabalhando localmente
PORT = 50000        ## usando a porta 50mil para não ter interferencia com outro programa

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #invocando  metodo socket, trabalhando com a familia IPV4, usando TCP
s.bind((HOST, PORT)) ##Passando para o metado o host e porta 
s.listen() #colocando servidor em modo de escuta 
print('Aguardando conexão de um cliente') #verificação que o servidor 
conn, ender = s.accept() # criando conexão e endereço logo dps aceitando a conexão / ender para verifica o endereço conectado

print('Conectado em', ender ) #verificando conexão aceita
while True:
    data = conn.recv(1024) # limitando tamanho dos dados
    if not data:
        print('Fechando a conexão')
        conn.close() #fechando conexão
        break
    conn.sendall(data) #Retornando a mensagem para cliente 