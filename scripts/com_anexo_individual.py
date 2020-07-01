# -*- coding: ISO-8859-1 -*-

import csv
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

path="./CRACHA/"

# lista de participantes do evento no formato .csv (nome,email)
lista = open('./participantes.csv', encoding="ISO-8859-1")
participantes = csv.DictReader(lista)

# pré-definição da mensagem a ser enviada
msg1 = "Prezado(a) "
msg2 = open('./mensagem.txt', 'r', encoding="ISO-8859-1").read()

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

# username ou email para logar no servidor
username = 'saber.ufpr@gmail.com'
password = 'Kdy,Z(VEyNJX0R6'

# remetente
from_addr = 'saber.ufpr@gmail.com'

# conexão de forma segura usando SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

# para interagir com um servidor externo precisaremos fazer login nele
server.login(username, password)

contador = 0
for pessoa in participantes:
    nome = pessoa["nome"]
    to_addrs = pessoa["email"] # destinatário

    body = msg1+str(nome)+",\n\n";
    body = body + msg2;

    # parâmetros da mensagem a ser enviada
    message = MIMEMultipart()
    message['subject'] = 'Agradecimento e feedback - SABER 2019' # não pode ter acentuação no assunto da mensagem
    message['from'] = from_addr
    message['to'] = to_addrs
    message.attach(MIMEText(body, 'plain'))

    #----------------------------------------------------------------------------
    # parâmetros para anexar um documento
    filename = nome+".pdf"
    file = path+nome+".pdf"
    attachment = open(file, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    message.attach(part)
    #----------------------------------------------------------------------------


    # ENVIO DA MENSAGEM
    server.sendmail(from_addr, to_addrs, message.as_string())

    print ("mensagem enviada com sucesso para:   "+nome+"   no e-mail:   "+to_addrs)
    contador = contador + 1

    if (contador > 9):
        server.quit()
        print("RECONECTANDO COM O SERVIDOR...")
        time.sleep(120) #espera 2min para reconectar com o servidor

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)

        contador = 0
        print("RECONECTADO")
    else:
        time.sleep(150) #espera 2min30s para enviar a próxima mensagem

server.quit()
print("\nMENSAGEM ENVIADA A TODOS OS PARTICIPANTES")
