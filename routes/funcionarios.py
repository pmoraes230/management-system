from flask import Blueprint, request, jsonify
from database import conectar

funcionarios_bp = Blueprint('funcionarios', __name__)

@funcionarios_bp.route('/', methods=['GET'])
def listar_funcionarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()
    conn.close()
    return jsonify(funcionarios)

@funcionarios_bp.route('/adicionar', methods=['POST'])
def adicionar_funcionario():
    nome = request.json.get('nome')
    cargo = request.json.get('cargo')
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO funcionarios (nome, cargo) VALUES (?, ?)", (nome, cargo))
    conn.commit()
    conn.close()
    return jsonify({"message": "Funcionário adicionado com sucesso!"}), 201