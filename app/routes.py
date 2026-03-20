from flask import render_template, request, redirect, url_for
from .services.bi_queries import buscar_filiais, buscar_canal,buscar_segmento,buscar_receitaTotal

def init_routes(app):

    @app.route('/')
    def home():
        
            
        filiais = buscar_filiais()
        canais = buscar_canal()
        segmento = buscar_segmento()
        receita = buscar_receitaTotal()
        receita = (float(receita) if receita else 0)
        
        
            
        return render_template('base.html',filiais=filiais, canais=canais, segmento = segmento, receita = receita)

        

