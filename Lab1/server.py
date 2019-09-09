import socket
import sys

def calcularSuma(valor1, valor2):
    return valor1 + valor2

def calcularMultiplicacion(valor1, valor2):
    return valor1 * valor2

def calcularResta(valor1, valor2):
    return valor1 - valor2

def calcularDivision(valor1, valor2):
    return valor1 / valor2

def seleccionarMetodo(msg):
    valores = msg.split()
    if int(valores[2]) == 1:
        return calcularSuma(int(valores[0]), int(valores[1]))
    elif int(valores[2]) == 2:
        return calcularMultiplicacion(int(valores[0]), int(valores[1]))
    elif int(valores[2]) == 3:
        return calcularResta(int(valores[0]), int(valores[1]))
    elif int(valores[2]) == 4:
        if(int(valores[1]) == 0):
            return "Error: Division entre cero"
        else:
            return calcularDivision(int(valores[0]), int(valores[1]))
    else:
        return "Operacion no valida"

def iniciarServidor(host, puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, puerto))
    s.listen(5) #hasta 5 peticiones

    while True:
        # establecer conexión
        (c, addr) = s.accept()

        print("Se estableció conexión con: %s" % str(addr))

        msg = 'Conexión establecida con : %s' % socket.gethostname() + "\r\n"
        c.send(msg.encode('utf8'))
        msg_rec = c.recv(1024)
        calculo = seleccionarMetodo(msg_rec.decode('ascii'))
        c.send(str(calculo).encode("utf8"))
        c.close()
    
if __name__ == "__main__":
    host = ""
    puerto = 44440
    iniciarServidor(host, puerto)