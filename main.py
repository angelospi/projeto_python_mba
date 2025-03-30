import pandas as pd

import sqlite3
from sqlalchemy import create_engine, inspect
from data_clean import DataClean
from utils import padroniza_str, create_db
from transform import calc_horas, classifica_turno

def carregar_dataset():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv",
        index_col=0
    )

    configs = pd.read_excel("metadado.xlsx", sheet_name="schema")

    df["date_time"] = pd.to_datetime(df[["year", "month", "day", "hour", "minute"]], dayfirst=True)
    dc = DataClean(df, configs)

    return dc

def insere_bd(df_tratada):
    con = sqlite3.connect('projeto_python.db')
    cur = con.cursor()
    engine = create_engine("sqlite:///projeto_python.db")

    if not inspect(engine).has_table("flights"):
        create_db(engine)
        # Não esquecer de acrescentar as novas colunas na criação da base

    with engine.connect() as connection:
        df_tratada.to_sql(name='flights', con=connection, index=False, if_exists='append')

    cur.execute('SELECT * from flights limit 10')
    result = cur.fetchall()
    print(result)

def tratar_dados(dc):
    df = dc.return_data()
    coluna_turno_partida = classifica_turno(df["date_time"])


    dc.select_cols()
    dc.rename_cols()
    dc.select_nnull_cols()
    dc.select_nneg_cols()
    dc.data_type()
    df_tratada = dc.return_data()

    configs = pd.read_excel("metadado.xlsx", sheet_name="schema")
    for col in list(configs[configs["padroniza_str"] == 1]["nome"]):
        df_tratada[col] = df_tratada.loc[:, col].apply(lambda x: padroniza_str(x))

    # Novas colunas
    df_tratada["tempo_voo_minutos"] = calc_horas(df_tratada["tempo_voo"])
    df_tratada["turno_partida"] = coluna_turno_partida


    return df_tratada

if __name__ == '__main__':

    dc = carregar_dataset()
    df_tratada = tratar_dados(dc)

    insere_bd(df_tratada)




