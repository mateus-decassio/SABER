# -*- coding: ISO-8859-1 -*-

import csv
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

for item in [1,2,3,4,5,6,7]:
    print('estou imprimindo o item '+str(item)+'e esperando 90 segundos depois')
    time.sleep(90) #espera 1min30s para enviar a próxima mensagem
