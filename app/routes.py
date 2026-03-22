from flask import render_template, request, redirect
from .services.bi_queries import (
    buscar_filiais,
    buscar_canal,
    buscar_segmento,
    buscar_receitaTotal,
    buscar_margem_media,
    buscar_Ticket_medio,
    buscar_crescimento_medio
)

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
                filters=filters
            )

        except Exception as e:
            print("Erro na rota /vendas:", e)
            return render_template("vendas.html", erro_db=True)