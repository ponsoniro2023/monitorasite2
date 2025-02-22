from time import sleep
import requests


def envio_mensagem(fone, msg):
    url = 'https://protectmeseguros.digisac.biz/api/v1/messages'
    headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer 724c60d95d8911ab00097c497f459099233641c5'}
    # Define o corpo da solicitação em formato JSON
    data = {
    "text": f"{msg}",
    "number": f"55{fone}",
     "serviceId": "8e473787-7548-417f-83e1-5eb1bd533d6f",
    "dontOpenTicket": True
    }

    response = requests.post(url, headers=headers, json=data)
    print(f'{fone} - "status", {response.status_code}')
    #print(fone)


phone = [11976829298, 11999341281]
fora = '*Teste monitoramento - SITE FORA DO AR*'
Site_ok = '*SITE ESTA NO AR NOVAMENTE*'
monitora = 'monitoramento por 24hs - ok'

m = 0
cont_erros = 0
email_fora = 0
status = ""


while True:
    try:
        site = requests.get('https://www.protecytme.com.br/assets/img/logoProtectMe-escudo.png')
        #print('ok teste')
    except:
        while cont_erros <= 3:
            #print('deu erro')
            sleep(15)
            cont_erros +=1

        if email_fora == 0:
            for c in phone:
                #print(cont_erros)
                envio_mensagem(c,fora)
                sleep(5)
                email_fora +=1
                status = 'Fora'
                #print(status)
                m=0
        sleep(6)
        print('novamente')
    else:
        m += 1
        if m == 3:
            #print('ok 3')
            #envio_mensagem(phone,monitora)
            m =0
        elif status == 'Fora':
            #print(status)
            for c in phone:
                cont_erros = 0
                email_fora = 0
                envio_mensagem(c, Site_ok)
                sleep(5)
                status = 'no ar'
                #print(status)
                #print(email_fora)

        else:
            #print('OK')
            sleep(10)

