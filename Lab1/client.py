
import socket

def iniciarCliente(host, puerto, msg_env):
	c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c.connect((host, puerto))
	msg_rec = c.recv(1024)
	print (msg_rec.decode('utf8'))
	c.send(msg_env.encode('ascii'))

	msg_rec = c.recv(1024)
	print (msg_rec.decode('utf8'))
	c.close()
	
if __name__ == "__main__":
	host = "10.251.46.94" #"192.168.0.105" #"10.251.45.41" #"192.168.0.110"    "10.251.45.95"
	puerto = 44440
	msg = ""
	while True:
		valor1 = int(input("Introducir valor 1: "))
		valor2 = int(input("Introducir valor 2: "))

		operacion = int(input("Cual calculo desea realizar: 1- Suma, 2- Multiplicacion: "))
		msg = '{} {} {}'.format(valor1, valor2, operacion)
		iniciarCliente(host, puerto, msg)