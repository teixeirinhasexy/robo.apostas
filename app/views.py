from flask import render_template, request
from app.init import app

@app.route('/', methods=['GET', 'POST'])
def show_filters():
    if request.method == 'POST':
        filters = request.form  # Obter os filtros do usuário
        # Processar filtros e mostrar apostas
    return render_template('filters.html')
