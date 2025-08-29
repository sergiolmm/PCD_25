import station

try:
    import usocket as socket
except:
    import socket
    
import esp
esp.osdebug(None)

import gc
gc.collect()

from machine import Pin

import resposta 

led1 = Pin(2, Pin.OUT)

led2 = Pin(4, Pin.OUT)

# liga o WIFI e se conecta
station.conectar(ssid="Sergio",pwd="123456789")

#cria o socket para poder trabalhar

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind(('',80)) # '' indica qualquer ip e 80 é a porta que estou escutando.

sock.listen(5)     # define numero de conexões que posso atender simultanemente

while True:
    conn, addr = sock.accept()
    print(f"conectado no ip {addr}")
    dados_recebidos = conn.recv(1024)
    request = dados_recebidos.decode()
    print(request)
    
    if "GET /led1on" in request:
        led1.value(1)
    if "GET /led1off" in request:
        led1.value(0)
        
    resposta.mandaResposta(conn)    
  
    conn.close()
    