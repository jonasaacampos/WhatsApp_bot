import pywhatkit as wa
import datetime


# coloque a lista dos números dos destinatários da mensagem aqui
# separe os contatos por vírgula para mais de 1
contacts = ['+5544988086437', '+55 44 8428-1838']
message = 'Hello world!'

total_contacts = len(contacts)
atual_contacts = 0

## parâmetros de tempo ##

# obtém hora e a data atual do sistema
date_time = datetime.datetime.now()
# extrai somente a hora da variável date_time
time = date_time.time()
# fatia a variál time e transforma-a em string
hora_atual = str(time.hour) + ':' + str(time.minute)

# fatia a string hora_atual, considerando somente os
# 2 primeiros dígitos para a variável disparo_hora
# e os dígitos finais para a variável disparo_minuto
disparo_hora = int(hora_atual[0:2])
disparo_min = int(hora_atual[3:]) + 1

for n in contacts:
    print(
        f'Iniciado o disparo em {hora_atual}\n próximo disparo será às {disparo_hora}: {disparo_min}')
    wa.sendwhatmsg(f'{n}', {message}, disparo_hora, disparo_min)
    atual_contacts += 1
    print(f'Enviando {atual_contacts} de {total_contacts} mensagens.')
    # mostra o histórico da mensagem enviada
    # TODAS as mensagens enviadas serão gravadas no log no pywhatkit_dbs.txt
    wa.showHistory()
    # A hora é redefinida, e são acrescentados + 3 minutos
    disparo_hora = int(hora_atual[0:2])
    disparo_min = int(hora_atual[3:]) + 3
    # repete isso até todoas as mensagens da lista sejam enviadas
