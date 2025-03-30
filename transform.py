def calc_horas(coluna_tempo_voo):
    """
    Calcula o tempo de voo em minutos.

    :param coluna_tempo_voo: Coluna contendo os tempos de voo em horas.

    :return: Um panda series com o tempo de voo em minutos.
    """

    return coluna_tempo_voo.apply(lambda hora: hora * 60)


def classifica_turno(coluna_data_hora):
    """
    Classificar o turno de acordo com a hora do dia.

    Regra de classificação:
    06:00 - 12:00 : MANHÃ
    12:00 - 18:00 : TARDE
    18:00 - 00:00 : NOITE
    00:00 - 06:00 : MADRUGADA

    :param coluna_data_hora: Um pandas Series com a data e hora de cada voo.

    :return: Um pandas Series com o turno de cada voo.
    """

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

