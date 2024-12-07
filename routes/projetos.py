from flask import Blueprint, request, jsonify
from database import conectar

projetos_bp = Blueprint('projetos', __name__)

@projetos_bp.route('/', methods=['GET'])
def listar_projetos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projetos")
    projetos = cursor.fetchall()
    conn.close()
    return jsonify(projetos)

@projetos_bp.route('/adicionar', methods=['POST'])
def adicionar_projeto():
    nome = request.json.get('nome')
    descricao = request.json.get('descricao')
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projetos (nome, descricao) VALUES (?, ?)", (nome, descricao))
    conn.commit()
    conn.close()
    return jsonify({"message": "Projeto adicionado com sucesso!"}), 201