from flask import render_template, request, redirect
from .services.bi_queries import (
    buscar_filiais,
    buscar_canal,
    buscar_segmento,
    buscar_receitaTotal,
    buscar_margem_media,
    buscar_Ticket_medio,
    buscar_crescimento_medio,
    buscar_receita_por_mes,
    buscar_Filial_Crecimento,
    buscar_receita_por_canal,
    buscar_filial_por_mes
    )
from collections import defaultdict

def init_routes(app):

    @app.route('/')
    def home():
        return redirect('/vendas')

    @app.route('/vendas')
    def vendas():
        try:

            f_filial = request.args.get('filial', '')
            f_canal = request.args.get('canal', '')
            f_segmento = request.args.get('segmento', '')
            

            filters = {
                "filial": f_filial,
                "canal": f_canal,
                "segmento": f_segmento
            }

            # BUSCA DADOS DOS FILTROS
            filiais = buscar_filiais()
            canais = buscar_canal()
            segmentos = buscar_segmento()

            # VALIDA CONEXÃO 
            if filiais is None or canais is None or segmentos is None:
                return render_template("vendas.html", erro_db=True)

            # 
            receita = buscar_receitaTotal(f_filial, f_canal, f_segmento)
            margem_media = buscar_margem_media(f_filial, f_canal, f_segmento)
            ticket_medio = buscar_Ticket_medio(f_filial, f_canal, f_segmento)
            crescimento_medio = buscar_crescimento_medio(f_filial, f_canal, f_segmento)
            

            dados_grafico = buscar_receita_por_mes(f_filial, f_canal, f_segmento)

            labels = [str(d[0]) for d in dados_grafico]
            valores = [float(d[1]) for d in dados_grafico]

            dados_crescimento = buscar_Filial_Crecimento(f_filial, f_canal, f_segmento)
            labels_crescimento = [str(d[0]) for d in dados_crescimento]
            valores_crescimento = [float(d[1]) for d in dados_crescimento]

            dados_crescimento_canal = buscar_receita_por_canal(f_filial, f_canal, f_segmento)
            

            dados = buscar_receita_por_canal(f_filial, f_canal, f_segmento)

            datas = sorted(list(set([str(d[1]) for d in dados])))
            canais_unicos = sorted(list(set([str(d[0]) for d in dados])))

            estrutura = defaultdict(dict)

            for canal, data, valor in dados:
                estrutura[str(canal)][str(data)] = float(valor)

            datasets = []

            for canal in canais_unicos:
                valores_canal = []
                for data in datas:
                    valores_canal.append(estrutura[canal].get(data, 0))
                
                datasets.append({
                    "label": canal,
                    "data": valores_canal
                })

            dados_filial_mes = buscar_filial_por_mes(f_filial, f_canal, f_segmento)
            datas_filial_mes = sorted(list(set([str(d[1]) for d in dados_filial_mes])))
            filiais_unicas = sorted(list(set([str(d[0]) for d in dados_filial_mes])))

            estrutura_filial_mes = defaultdict(dict)

            for filial, data, valor in dados_filial_mes:
                estrutura_filial_mes[str(filial)][str(data)] = float(valor)
                datasets_filial_mes = []
            for filial in filiais_unicas:
                valores_filial_mes = []
                for data in datas_filial_mes:
                    valores_filial_mes.append(estrutura_filial_mes[filial].get(data, 0))
                
                datasets_filial_mes.append({
                    "label": filial,
                    "data": valores_filial_mes
                })

            if (
                receita is None or
                margem_media is None or
                ticket_medio is None or
                crescimento_medio is None
            ):
                return render_template("vendas.html", erro_db=True)

            
            return render_template(
                'vendas.html',
                filiais=filiais,
                canais=canais,
                segmentos=segmentos,
                receita=receita,
                margem_media=margem_media,
                ticket_medio=ticket_medio,
                crescimento_medio=crescimento_medio,
                filial_sel=f_filial,
                canal_sel=f_canal,
                segmento_sel=f_segmento,
                filters=filters,
                labels=labels,
                valores=valores,
                labels_crescimento=labels_crescimento,
                valores_crescimento=valores_crescimento,
                labels_crescimento_canal=datas,
                datasets_crescimento_canal=datasets,
                labels_filial_mes=datas_filial_mes,
                datasets_filial_mes=datasets_filial_mes

            )

        except Exception as e:
            print("Erro na rota /vendas:", e)
            return render_template("vendas.html", erro_db=True)