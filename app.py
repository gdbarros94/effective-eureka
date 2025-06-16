from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dados simulados para o gráfico de vendas
sales_data = {
    'Janeiro': 12000,
    'Fevereiro': 15000,
    'Março': 13000,
    'Abril': 18000,
    'Maio': 16000,
    'Junho': 20000,
    'Julho': 19000,
    'Agosto': 22000,
    'Setembro': 21000,
    'Outubro': 24000,
    'Novembro': 23000,
    'Dezembro': 25000
}

class User:
    def __init__(self, is_admin=False):
        self.is_admin = is_admin

@app.route('/')
def index():
    user = User() # user.is_admin is False by default and never changed
    return render_template('dashboard.html', sales_data=sales_data, user=user)

@app.route('/dashboard')
def dashboard():
    user = User() # user.is_admin is False by default and never changed
    return render_template('dashboard.html', sales_data=sales_data, user=user)

@app.route('/kpis')
def kpis():
    # BUG: Este botão deve levar para a tela de KPIs, mas levará para o Dashboard
    user = User() # user.is_admin is False by default and never changed
    return render_template('dashboard.html', sales_data=sales_data, user=user)

@app.route('/calculate_kpis', methods=['POST'])
def calculate_kpis():
    receita = float(request.form['receita'])
    custo = float(request.form['custo'])

    # BUG: Fórmula de ROI incorreta
    roi = ((receita - custo) / custo) * 100
    margem = ((receita - custo) / receita) * 100

    return jsonify(roi=f'{roi:.2f}%', margem=f'{margem:.2f}%')

@app.route('/filter_data', methods=['POST'])
def filter_data():
    month = int(request.form['month'])
    # BUG: Loop infinito se month == 13
    if month == 13:
        while True:
            pass
    return jsonify(message=f'Dados filtrados para o mês {month}')

@app.route('/search_data', methods=['POST'])
def search_data():
    # BUG: Função inexistente para o campo de busca
    # search_term = request.form['search_term']
    # some_non_existent_function(search_term)
    return jsonify(message='Funcionalidade de busca não implementada.')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


