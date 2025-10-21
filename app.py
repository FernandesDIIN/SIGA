from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = 'minha-chave-secreta-para-o-tcc'

anuncios_da_escola = [
    {
        "id": 1,
        "titulo": "Início das Provas do Primeiro Trimestre",
        "conteudo": "As provas do primeiro trimestre terão início na próxima segunda-feira. Por favor, consultem o calendário detalhado no mural da vossa turma.",
        "data": "08-10-2025"
    },
    {
        "id": 2,
        "titulo": "Festa de Fim de Ano",
        "conteudo": "A tradicional festa de fim de ano da escola será realizada no pátio principal no dia 15 de Dezembro. Contamos com a presença de todos!",
        "data": "05-10-2025"
    },
    {
        "id": 3,
        "titulo": "Manutenção do Sistema de Água",
        "conteudo": "Informamos que amanhã, dia 11 de Outubro, haverá um corte no fornecimento de água entre as 10h e as 12h para manutenção.",
        "data": "10-10-2025"
    }
]
# ---------------------------------------------------------

horario_aluno = [
    {"dia": "Segunda-feira", "hora": "08:00-09:30", "disciplina": "Matemática", "sala": "101"},
    {"dia": "Segunda-feira", "hora": "10:00-11:30", "disciplina": "Física", "sala": "203"},
    {"dia": "Terça-feira", "hora": "08:00-09:30", "disciplina": "Português", "sala": "105"},
    {"dia": "Quarta-feira", "hora": "10:00-11:30", "disciplina": "Química", "sala": "201"},
    {"dia": "Quinta-feira", "hora": "08:00-09:30", "disciplina": "História", "sala": "102"},
    {"dia": "Sexta-feira", "hora": "10:00-11:30", "disciplina": "Educação Física", "sala": "Ginásio"}
]


@app.route('/')
def homepage():
    return render_template('index.html', anuncios=anuncios_da_escola)


@app.route('/login', methods=['GET', 'POST'])
def pagina_login():
    if request.method == 'POST':
        utilizador = request.form['utilizador']
        senha = request.form['senha']

        if utilizador == 'aluno' and senha == '1234':
            session['utilizador_logado'] = utilizador  
            return redirect(url_for('homepage'))  

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('utilizador_logado', None)  
    return redirect(url_for('homepage'))  

@app.route('/horario')
def pagina_horario():
    if 'utilizador_logado' not in session:
        return redirect(url_for('pagina_login'))

    return render_template('horario.html', horario=horario_aluno)

if __name__ == '__main__':
    app.run(debug=True)