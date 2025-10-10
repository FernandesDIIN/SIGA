from flask import Flask, render_template

# Cria a nossa aplicação
app = Flask(__name__)

# Define a rota para a página inicial
@app.route('/')
def homepage():
    # Renderiza (desenha) o nosso ficheiro HTML
    return render_template('index.html')

# Permite executar a aplicação
if __name__ == '__main__':
    app.run(debug=True)