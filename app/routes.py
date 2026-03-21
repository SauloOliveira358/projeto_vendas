from flask import render_template, request, redirect, url_for
from .services.bi_queries import buscar_filiais, buscar_canal,buscar_segmento,buscar_receitaTotal,buscar_margem_media,buscar_Ticket_medio,buscar_crescimento_medio

def init_routes(app):

        @app.route('/')
        def home():
            f_filial = request.args.get('filial')
            f_canal = request.args.get('canal')
            f_segmento = request.args.get('segmento')
                
            filiais = buscar_filiais()
            canais = buscar_canal()
            segmento = buscar_segmento()

            # AGORA PASSAMOS OS FILTROS PARA TODOS OS KPIs
            receita = buscar_receitaTotal(f_filial, f_canal, f_segmento)
            
            # Se a receita for 0 (nenhum dado encontrado), evitamos erro de cálculo
            margem_media = buscar_margem_media(f_filial, f_canal, f_segmento)
            ticket_medio = buscar_Ticket_medio(f_filial, f_canal, f_segmento)
            crescimento_medio = buscar_crescimento_medio(f_filial, f_canal, f_segmento)
            
            return render_template('base.html', 
                                filiais=filiais, 
                                canais=canais, 
                                segmento=segmento, 
                                receita=receita, 
                                margem_media=margem_media, 
                                ticket_medio=ticket_medio, 
                                crescimento_medio=crescimento_medio,
                                filial_sel=f_filial,
                                canal_sel=f_canal,
                                segmento_sel=f_segmento)

        

