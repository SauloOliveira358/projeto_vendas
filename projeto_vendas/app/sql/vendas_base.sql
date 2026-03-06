SELECT
    data_mes,
    filial,
    cidade,
    uf,
    regiao,
    canal,
    segmento,
    receita_liquida,
    margem_bruta_pct,
    ticket_medio,
    crescimento_receita_pct
FROM vendas.vm_kpis_vendas_mensal
ORDER BY data_mes;
