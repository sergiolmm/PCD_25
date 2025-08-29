import network
from time import sleep
try:
    import usocket as socket
except:
    import socket

import esp # biblioteca para o esp
import gc  # biblioteca para garbage collect

esp.osdebug(None)
gc.collect()

## SSID e senha da rede que desejo conectar.
SSID = 'D-Link_DIR-615'
PWD  = ''

sta = network.WLAN(network.STA_IF)
sta.active(True)
#print(sta.scan())
sta.connect(SSID, PWD)
while not sta.isconnected():
    print(".", end="")
    sleep(1)
    
print(f'Conectado ao SSID = {SSID} no endereço')
print(sta.ifconfig())

  

def web_page():
    
    html = """
        <html><head>
                <title> Pagina de Teste PDC </title>
            </head>
        <body>
            <p>
            <H1> AULA DE PDC  - Prof Sergio </H1>
            
        </body>
        </html>"""

    return html

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    s.bind(('',80))
    s.listen(5)
    
    while True:
        conn, addr = s.accept()
        print(f'Conectado do endereco {addr}')
        request = conn.recv(1024)
        request = request.decode()
        print(request)
        response = web_page()
        conn.send('HTTP/1.1 200 OK\r\n')
        conn.send('Content-Type: text/html\r\n')
        conn.send('Connection: close\r\n\r\n')
        conn.sendall(response)
        conn.close()
    
except OSError as e:
    print(f'Erro de socket {e}')

finally:
    if s:
        s.close()