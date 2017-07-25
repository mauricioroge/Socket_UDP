import socket

#HOST = '127.0.0.1'  # Endereco IP do Servidor
#PORT = 5002            # Porta que o Servidor esta
HOST = input("Qual o endereco de envio?")
PORT = input("Por qual porta deseja enviar?")
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, int(PORT))
print ('Para sair use CTRL+X\n')
msg = input()

while (msg != '\x18'):
    udp.sendto (msg.encode('ascii'), dest)
    msg = input()

msg = 'close'
udp.sendto(msg.encode('ascii'),dest)
udp.close()