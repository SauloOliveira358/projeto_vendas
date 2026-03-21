from flask import render_template, request, redirect, url_for
from .services.bi_queries import buscar_filiais, buscar_canal,buscar_segmento,buscar_receitaTotal,buscar_margem_media,buscar_Ticket_medio,buscar_crescimento_medio

def init_routes(app):

    @app.route('/')
    def home():
        
            
        filiais = buscar_filiais()
        canais = buscar_canal()
        segmento = buscar_segmento()
        receita = buscar_receitaTotal()
        receita = (float(receita) if receita else 0)
        margem_media = buscar_margem_media()
        margem_media = (float(margem_media) if receita else 0)
        ticket_medio = buscar_Ticket_medio()
        ticket_medio = (float(ticket_medio) if receita else 0)
        crescimento_medio = buscar_crescimento_medio()
        crescimento_medio = (float(crescimento_medio) if receita else 0)
        
            
        return render_template('base.html',filiais=filiais, canais=canais, segmento = segmento, receita = receita, margem_media = margem_media, ticket_medio = ticket_medio, crescimento_medio = crescimento_medio)

        

