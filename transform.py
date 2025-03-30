import pandas as pd


def calc_horas(coluna_tempo_voo):
    return coluna_tempo_voo.apply(lambda hora: hora * 60)


def classifica_turno(coluna_data_hora):
    # Regra de classificação:
    # 06:00 - 12:00 : MANHÃ
    # 12:00 - 18:00 : TARDE
    # 18:00 - 00:00 : NOITE
    # 00:00 - 06:00 : MADRUGADA

    return coluna_data_hora.apply(selecionar_turno)

def selecionar_turno(data_hora):
    hora = data_hora.hour

    if hora >= 6 and hora < 12:
        return 'MANHÃ'
    elif hora >= 12 and hora < 18:
        return 'TARDE'
    elif hora >= 18 and hora < 24:
        return 'NOITE'
    elif hora >= 0 and hora < 6:
        return 'MADRUGADA'

    return

