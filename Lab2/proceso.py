import os
import socket
from datetime import datetime


class Process:
    def _init_(self,idprocess,host,port):
        
        self.idprocess=idprocess
        self.host=host
        self.port=port
        
class Vector:
    def _init_(self,p1,p2,p3):  
        self.p1=p1
        self.p2=p2
        self.p3=p3
    

def guardarArchivo(datos):
    path='D:\Lincenciatura\Ciclo 2\Sistemas\Sistemas-Distribuidos\Lab2\datos.txt'
    if(os.path.exists(path)):
       with open (path, "r") as archivo:
           datos_archivos = archivo.read()
           with open (path, "w") as archivo:
                archivo.write(datos_archivos+'\n'+datos)
    else:
        with open (path, "w") as archivo:
            archivo.write(datos+'\n')

def aumentar(msg_proceso):
    lista_msg_proceso = msg_proceso.split(',')
    aumentado = int(lista_msg_proceso[2])+1
    resultado = lista_msg_proceso[0]+","+lista_msg_proceso[1]+","+str(aumentado)
    return resultado

def iniciarCliente(host, puerto):
    
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((host, puerto))
    vect =  Vector(1,0,0)
    c.send(vect)
    c.close()

def reciv(host,puerto):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, puerto))
    s.listen(5) 

    while True:

        (c, addr) = s.accept()

        print("Se estableció conexión con: %s" % str(addr))

        msg = 'Conexión establecida con : %s' % socket.gethostname() + "\r\n"
        c.send(msg.encode('utf8'))
        msg_rec = c.recv(1024)
        print(msg_rec.decode("ascii"))
        datos = aumentar(msg_rec.decode("ascii"))
        guardarArchivo(datos)  
        c.close()
    
    

if __name__ == "__main__":
    
    process1 = Process(1,"10.251.47.45",44440)
    process2 = Process(2, "192.168.43.151",44440)
    process3 = Process(3,"10.251.45.48",44440)
    
    
    #reciv(process1.host, process1.port)

    print("Indicar Proceso para enviar petición")
    _Process_id = input()
    
    if(_Process_id == 1):
        iniciarCliente(process1.host, process1.port)
    if(_Process_id == 2):
         iniciarCliente(process2.host, process2.port)
    if(_Process_id == 3):
         iniciarCliente(process3.host, process3.port)