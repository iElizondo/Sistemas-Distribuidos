import socket
import sys

def calcularSuma(valor1, valor2):
    return valor1 + valor2

def calcularMultiplicacion(valor1, valor2):
    return valor1 * valor2

def seleccionarMetodo(msg):
    valores = msg.split()
    if int(valores[2]) == 1:
        return calcularSuma(int(valores[0]), int(valores[1]))
    elif int(valores[2]) == 2:
        return calcularMultiplicacion(int(valores[0]), int(valores[1]))

def iniciarServidor(host, puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, puerto))
    s.listen() #hasta 5 peticiones

    while True:
        # establecer conexión
        (c, addr) = s.accept()

        print("Se estableció conexión con: %s" % str(addr))

        # msg = 'Conexión establecida con : %s' % socket.gethostname() + "\r\n"
        # c.send(msg.encode('utf8'))
        msg_rec = c.recv(1024).decode('ascii')
        
        
        # calculo = seleccionarMetodo(msg_rec.decode('ascii'))
        # c.send(str(calculo).encode("utf8"))
        respuesta = ""
        try:
            inicio = msg_rec.find("GET")
            fin = msg_rec.find("HTTP")
            datos = msg_rec[(inicio+5):(fin-1)]
            split_datos = datos.split("?")
            print(split_datos[0])
            split_variables = split_datos[1].split("&")
            x = split_variables[0].split("=")[1]
            y = split_variables[1].split("=")[1]
            print(x)
            print(y)
            respuesta = "HTTP/1.1 200 OK\r\n"\
                        "Date: Mon, 27 Aug 2018 19:45:24\r\n"\
                        "Server: Laboratorio 1 - Webservers\r\n"\
                        "Content-type: text/html\r\n"\
                        "Connection: close\r\n"\
                        "\r\n"\
                        "<!DOCTYPE html><html><head><title>Laboratorio1</title></head><body><h2>Calculo realizado</h2><h1>Operacion 25+ 12 = 37</h1></body></html>"
        except:
            respuesta = "HTTP/1.1 404 OK\r\n"\
                    "Date: Mon, 27 Aug 2018 19:45:24\r\n"\
                    "Server: Laboratorio 1 - Webservers\r\n"\
                    "Content-type: text/html\r\n"\
                    "Connection: close\r\n"\
                    "\r\n"\
                    "<!DOCTYPE html><html><head><title>Laboratorio1</title></head><body><h2>ERROR No existe la funcion</h2></body></html>"
        c.send(respuesta.encode("utf8"))
        # print(respuesta.encode("utf8"))
        c.close()
    
if __name__ == "__main__":
    host = ""
    puerto = 8080
    iniciarServidor(host, puerto)
