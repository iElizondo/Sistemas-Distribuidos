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

def seleccionarMetodo(operacion, x, y):
    if operacion == "sumar":
        return calcularSuma(int(x), int(y))
    elif operacion == "multiplicar":
        return calcularMultiplicacion(int(x), int(y))
    elif operacion == "restar":
        return calcularResta(int(x), int(y))
    elif operacion == "dividir":
        if(int(y) == 0):
            return "Error: Division entre cero"
        else:
            return calcularDivision(int(x), int(y))
    else:
        return "Operacion no valida"

def leerMensaje(mensaje):
    respuesta = ""
    try: 
        inicio = mensaje.find("GET")
        fin = mensaje.find("HTTP")
        datos = mensaje[(inicio+5):(fin-1)]
        split_datos = datos.split("?")
        operaciones = split_datos[0]
        split_variables = split_datos[1].split("&")
        x = split_variables[0].split("=")[1]
        y = split_variables[1].split("=")[1]
        resultado = seleccionarMetodo(operaciones,x,y)
        respuesta = "HTTP/1.1 200 OK\r\n"\
                        "Date: Mon, 27 Aug 2018 19:45:24\r\n"\
                        "Server: Laboratorio 1 - Webservers\r\n"\
                        "Content-type: text/html\r\n"\
                        "Connection: close\r\n"\
                        "\r\n"\
                        "<!DOCTYPE html><html><head><title>Laboratorio1</title></head><body><h2>Calculo realizado</h2><h1>Al "+operaciones+" "+x+" y "+y+" el resultado es "+str(resultado)+"</h1></body></html>"
    except:
        respuesta = "HTTP/1.1 404 OK\r\n"\
                    "Date: Mon, 27 Aug 2018 19:45:24\r\n"\
                    "Server: Laboratorio 1 - Webservers\r\n"\
                    "Content-type: text/html\r\n"\
                    "Connection: close\r\n"\
                    "\r\n"\
                    "<!DOCTYPE html><html><head><title>Laboratorio1</title></head><body><h2>ERROR No existe la funcion</h2></body></html>"
    
    return respuesta

def iniciarServidor(host, puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, puerto))
    s.listen() 

    while True:
        # establecer conexión
        (c, addr) = s.accept()
        print("Se estableció conexión con: %s" % str(addr))
        msg_rec = c.recv(1024).decode('ascii')
        respuesta = leerMensaje(msg_rec)
        c.send(respuesta.encode("utf8"))
        c.close()
    
if __name__ == "__main__":
    host = ""
    puerto = 8080
    iniciarServidor(host, puerto)
