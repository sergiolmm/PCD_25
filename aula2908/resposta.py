

def pagina():
    html = """
    <HTML>
      <head>
       <title> Aula PCD 
       </title>
      </head> 
      <body>
        <H1>Deu certo 333</H1>
        <pre><br>
        <button type="button" onclick="location='led1on'">Ligar Led 1</button>
        <br><br>
        <button type="button" onclick="location='led1off'">Desligar Led 1</button>        
      </body>
    </html>
    
    """
    return html
    



def mandaResposta(conn):
    
    conn.send("HTTP/1.1 200 OK\r\n")
    conn.send("Content-Type: text/html\r\n")
    conn.send("Connection: close\r\n\r\n")
    conn.send(pagina())