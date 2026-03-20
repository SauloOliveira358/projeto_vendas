from app.db import get_connection

def buscar_filiais():   # Função para buscar as filiais no banco de dados 
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT distinct filial FROM vendas.vm_kpis_vendas_mensal")
    dados = cursor.fetchall()
    dados = [
    f[0].replace('Filial ', '') 
    for f in dados 
    if f[0] is not None
]
 

    conn.close()
    return dados


def buscar_canal():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT distinct canal FROM vendas.vm_kpis_vendas_mensal")
    dados = cursor.fetchall()
    dados = [f[0] 
    for f in dados 
    if f[0] is not None]


    conn.close()
    return dados




def buscar_segmento():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT distinct segmento FROM vendas.vm_kpis_vendas_mensal")
    dados = cursor.fetchall()
    dados = [f[0] 
    for f in dados 
    if f[0] is not None]

    conn.close()
    return dados

def buscar_receitaTotal():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(receita_bruta) FROM vendas.vm_kpis_vendas_mensal")
    dados = cursor.fetchone()
    conn.close()
    if dados and dados[0] is not None:
        return dados[0]
    else:
        return 0
    





    