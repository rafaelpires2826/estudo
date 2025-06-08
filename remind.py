import json
import schedule
import time
from datetime import datetime


def carregar_atividades(caminho='atividades.json'):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def lembrar(atividade):
    horario = datetime.now().strftime('%H:%M')
    print(f"[{horario}] Lembrete: {atividade}")


def agendar_atividades(atividades):
    for item in atividades:
        hora = item.get('hora')
        nome = item.get('atividade')
        if hora and nome:
            schedule.every().day.at(hora).do(lembrar, nome)


def main():
    atividades = carregar_atividades()
    if not atividades:
        print('Nenhuma atividade encontrada em atividades.json.')
        return
    agendar_atividades(atividades)
    print('Iniciando lembretes de atividades... (Ctrl+C para sair)')
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
