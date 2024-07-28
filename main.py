import time
import datetime
import winsound
hora_min = input("Digite o horario que irá despertar no formato HH:MM: ")
dia_da_semana = input("Programe o(s) dia(s) que irá despertar: ")
lista_musicas = input("Qual musica tocará dentre as da lista: 1 - tema ping-pong  2 - tema exit")


hora = int(hora_min.split(':')[0])
min = int(hora_min.split(':')[1])
dias_da_semana = dia_da_semana.split(' ')

def list_music(musics):
  lista = []
  for lists in musics:
    if lists == "tema exit":
      lista.append(0)
    if lists == "tema ping pong":
      lista.append(1)
  return lista


def processar(dias_da_semana):
  dias_da_semana_list = []

  for dia in dias_da_semana:
    if dia == "seg" or dia == "segunda":
      dias_da_semana_list.append(0)
    if dia == "ter" or dia == "terça":
      dias_da_semana_list.append(1)
    if dia == "qua" or dia == "quarta":
      dias_da_semana_list.append(2)
    if dia == "qui" or dia == "quinta":
      dias_da_semana_list.append(3)
    if dia == "sex" or dia == "sexta":
      dias_da_semana_list.append(4)
    if dia == "sab" or dia == "sabado":
      dias_da_semana_list.append(5)
    if dia == "dom" or dia == "domingo":
      dias_da_semana_list.append(6)

  return dias_da_semana_list

dias_da_semana_int = processar(dias_da_semana)


def atual(dias_desejados, data_atual):
  if data_atual.weekday() in dias_desejados:
    return True
  return False

def alarm(horamin_atual):
    if horamin_atual.hour == hora and horamin_atual.minute == min:
        return True
    return False

while True:
    now = datetime.datetime.now()
    if alarm(now) and atual(dias_da_semana_int, now):
        winsound.PlaySound('E:\Programação\Projetos de Outubro 2022\Despertador em python\tema.wav', winsound.SND_ASYNC)
        time.sleep(60)
