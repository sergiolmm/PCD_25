import network
from time import sleep

def conectar( ssid, pwd,tipo = "AP"):
    if tipo != "AP":
        # me conecto a um ponte de acesso
        sta = network.WLAN(network.STA_IF)
        sta.active(False)
        sleep(1)
        sta.active(True)
        sta.connect(ssid,pwd)
        while not sta.isconnected():
            print('.', end="")
            sleep(0.3)        
    else:
        # viro um ponto de acesso
        sta = network.WLAN(network.AP_IF)
        sta.active(False)
        sleep(1)
        sta.active(True)
        sta.config(essid=ssid, password= pwd)
        while sta.active() == False:
            print('.', end="")
            sleep(0.3)
        
    print('\nConectado ao ip: ', sta.ifconfig()[0])
    
    
if __name__ == "__main__":
    print('Testando ')
    conectar(ssid="Teste", pwd="123456789")
    conectar(ssid="D-Link_DIR-615", pwd="", tipo= "AF")
    