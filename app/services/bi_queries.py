from app.db import get_connection

def buscar_filiais():   
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

def buscar_receitaTotal(filial=None, canal=None, segmento=None):
    conn = get_connection()
    cursor = conn.cursor()
    
    
    sql = "SELECT SUM(receita_bruta) FROM vendas.vm_kpis_vendas_mensal WHERE 1=1"
    params = []

   
    if filial:
        
        sql += " AND filial LIKE %s" 
        params.append(f"%{filial}%")
    if canal:
        sql += " AND canal = %s"
        params.append(canal)
    if segmento:
        sql += " AND segmento = %s"
        params.append(segmento)

    cursor.execute(sql, params)
    dados = cursor.fetchone()
    conn.close()
    
    return dados[0] if dados and dados[0] is not None else 0


def buscar_margem_media(filial=None, canal=None, segmento=None):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT AVG(margem_bruta_pct) FROM vendas.vm_kpis_vendas_mensal WHERE 1=1"
    params = []

    
    if filial:
        
        sql += " AND filial LIKE %s" 
        params.append(f"%{filial}%")
    if canal:
        sql += " AND canal = %s"
        params.append(canal)
    if segmento:
        sql += " AND segmento = %s"
        params.append(segmento)

    cursor.execute(sql, params)
    dados = cursor.fetchone()
    conn.close()
    
    return dados[0] if dados and dados[0] is not None else 0




def buscar_Ticket_medio(filial=None, canal=None, segmento=None):
    conn = get_connection()
    cursor = conn.cursor()
   
    sql = "SELECT AVG(ticket_medio) FROM vendas.vm_kpis_vendas_mensal WHERE 1=1"
    params = []

    
    if filial:
        
        sql += " AND filial LIKE %s"     
        params.append(f"%{filial}%")
    if canal:
        sql += " AND canal = %s"
        params.append(canal)
    if segmento:
        sql += " AND segmento = %s"
        params.append(segmento)

    cursor.execute(sql, params)
    dados = cursor.fetchone()
    conn.close()
    
    return dados[0] if dados and dados[0] is not None else 0






def buscar_crescimento_medio(filial=None, canal=None, segmento=None):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = "SELECT AVG(crescimento_receita_pct) FROM vendas.vm_kpis_vendas_mensal WHERE 1=1"
    params = []
     
    if filial:
        
        sql += " AND filial LIKE %s" 
        params.append(f"%{filial}%")
    if canal:
        sql += " AND canal = %s"
        params.append(canal)
    if segmento:
        sql += " AND segmento = %s"
        params.append(segmento)

    cursor.execute(sql, params)
    dados = cursor.fetchone()
    conn.close()
    
    return dados[0] if dados and dados[0] is not None else 0





    