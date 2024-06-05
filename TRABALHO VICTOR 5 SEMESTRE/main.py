from flask import Flask, jsonify, request, render_template, session
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import render_template
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_folder='static',template_folder='templates')
CORS(app)
app.secret_key = 'supersecretkey'  


db_config = {
    'dbname': 'Biblioteca',
    'user': 'postgres',
    'password': '123',
    'host': 'localhost'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagina2')
def pagina2():
    return render_template('index2.html')

@app.route('/inicio')
def inicio():
    return render_template('index.html')

def connect_db():
    return psycopg2.connect(**db_config)

@app.route('/livros', methods=['GET'])
def get_livros():
    conn = connect_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM Livros")
    livros = cur.fetchall()
    conn.close()
    return jsonify(livros)

@app.route('/livros', methods=['POST'])
def add_livro():
    data = request.json
    titulo = data.get('titulo')
    autor = data.get('autor')
    genero = data.get('genero')
    ano_publicacao = data.get('ano')
    copias_disponiveis = data.get('copias')

    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO Livros (titulo, autor, genero, ano_publicacao, copias_disponiveis) VALUES (%s, %s, %s, %s, %s)",
                    (titulo, autor, genero, ano_publicacao, copias_disponiveis))
        conn.commit()
        conn.close()
        return jsonify({"message": "Livro adicionado com sucesso"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/livros/filtrar', methods=['GET'])
def filtrar_livros():
    filtro_titulo = request.args.get('filtroTitulo')
    filtro_autor = request.args.get('filtroAutor')
    filtro_genero = request.args.get('filtroGenero')

    sql = "SELECT * FROM Livros WHERE 1=1"  # Inicializa a query

    if filtro_titulo:
        sql += " AND titulo LIKE '%" + filtro_titulo + "%'"
    if filtro_autor:
        sql += " AND autor LIKE '%" + filtro_autor + "%'"
    if filtro_genero:
        sql += " AND genero LIKE '%" + filtro_genero + "%'"

    conn = connect_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(sql)
    livros_filtrados = cur.fetchall()
    conn.close()

    return jsonify(livros_filtrados)

@app.route('/emprestimos', methods=['POST'])
def registrar_emprestimo():
    data = request.json
    livro_id = data['livro_id']
    
    conn = connect_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT copias_disponiveis FROM Livros WHERE id = %s", (livro_id,))
    result = cur.fetchone()
    
    if result and result['copias_disponiveis'] > 0:
        try:
            cur.execute("UPDATE Livros SET copias_disponiveis = copias_disponiveis - 1 WHERE id = %s", (livro_id,))
            conn.commit()
            conn.close()
            return jsonify({"message": "Empréstimo registrado com sucesso"}), 201
        except Exception as e:
            conn.close()
            return jsonify({"error": str(e)}), 500
    else:
        conn.close()
        return jsonify({"error": "Não há cópias disponíveis para empréstimo"}), 400

@app.route('/livros/devolver', methods=['POST'])
def devolver_livro():
    data = request.json
    livro_id = data['livro_id']
    
    try:
        conn = connect_db()
        cur = conn.cursor()
        
        cur.execute("UPDATE Livros SET copias_disponiveis = copias_disponiveis + 1 WHERE id = %s", (livro_id,))
        conn.commit()
        conn.close()
        
        return jsonify({"message": "Livro devolvido com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
