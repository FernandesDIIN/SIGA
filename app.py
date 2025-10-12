from flask import Flask, render_template

app = Flask(__name__)

# --- DADOS FICTÍCIOS (MAIS TARDE VIRÁ DA BASE DE DADOS) ---
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


@app.route('/')
def homepage():
    # Agora, vamos enviar a nossa lista de anúncios para o HTML
    return render_template('index.html', anuncios=anuncios_da_escola)

# Define a rota para a página de login
@app.route('/login')
def pagina_login():
    return render_template('login.html')


# Permite executar a aplicação
if __name__ == '__main__':
    app.run(debug=True)