import socket
#HOST = '127.0.0.1'              # Endereco IP do Servidor
#PORT = 5002            # Porta que o Servidor esta

HOST = input("Qual o endereco de envio?")
PORT = input("Por qual porta deseja enviar?")

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, int(PORT))
udp.bind(orig)

while True:
    msg, cliente = udp.recvfrom(1024)
    if msg.decode('ascii') == 'close':
        print("Conexao encerrada pelo cliente!")
        udp.close()
        quit()
    print (cliente, msg.decode('ascii'))

udp.close()