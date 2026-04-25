from app.db import get_connection

def buscar_filiais():   
    conn = get_connection()
    if conn is None:
        return None
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
    if conn is None:
        return None
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
    if conn is None:
        return None
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
    if conn is None:
        return None
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
    if conn is None:
        return None
    cursor = conn.cursor()
    sql = "SELECT SUM(receita_liquida - custo_total) / NULLIF(SUM(receita_liquida), 0) * 100 FROM vendas.vm_kpis_vendas_mensal WHERE 1=1"
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
    if conn is None:
        return None
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
    if conn is None:
        return None
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






##Grafico de Receira Bruta mesnal


def buscar_receita_por_mes(filial=None, canal=None, segmento=None):
    conn = get_connection()
    if conn is None:
        return None
    
    cursor = conn.cursor()

    sql = """
        SELECT 
            data_mes,
            SUM(receita_bruta) AS receita_total
        FROM vendas.vm_kpis_vendas_mensal
        WHERE 1=1
    """
    
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

    sql += " GROUP BY data_mes ORDER BY data_mes"

    cursor.execute(sql, params)
    dados = cursor.fetchall()

    conn.close()

    return dados


    
## Grafico de Receita Filial

def buscar_Filial_Crecimento(filial=None, canal=None, segmento=None):
    conn = get_connection()
    if conn is None:
        return None
    
    cursor = conn.cursor()

    sql = """
        
            SELECT filial,SUM (receita_liquida)  FROM vendas.vm_kpis_vendas_mensal WHERE 1=1
    """
    
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

    sql += " GROUP BY filial "

    cursor.execute(sql, params)
    dados = cursor.fetchall()

    conn.close()

    return dados





def buscar_receita_por_canal(filial=None, canal=None, segmento=None):
    conn = get_connection()
    if conn is None:
        return None
    
    cursor = conn.cursor()

    sql = """
        SELECT canal, data_mes, SUM(receita_bruta) as receita_total FROM vendas.vm_kpis_vendas_mensal
        WHERE 1=1
    """
    
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

    sql += " GROUP BY canal,data_mes ORDER BY canal,data_mes"

    cursor.execute(sql, params)
    dados = cursor.fetchall()

    conn.close()

    return dados







def buscar_filial_por_mes(filial=None, canal=None, segmento=None):
    conn = get_connection()
    if conn is None:
        return None
    
    cursor = conn.cursor()

    sql = """
        SELECT filial,data_mes,SUM(receita_liquida) as Receita_Filial FROM vendas.vm_kpis_vendas_mensal WHERE 1=1
    """
    
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

    sql += " GROUP BY filial,data_mes ORDER BY filial,data_mes"

    cursor.execute(sql, params)
    dados = cursor.fetchall()

    conn.close()

    return dados