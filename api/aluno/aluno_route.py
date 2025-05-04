from flask import Blueprint, jsonify, request
from aluno.aluno_model import AlunoNaoEncontrado, listar_alunos, aluno_por_id, adicionar_aluno, atualizar_aluno, excluir_aluno

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos/', methods = ['GET'])
def get_alunos():
    return jsonify(listar_alunos()), 200
    
@alunos_blueprint.route('/alunos/<int:id>', methods = ['GET'])
def get_aluno(id):
    try:
        aluno = aluno_por_id(id)
        return jsonify(aluno), 200
    except AlunoNaoEncontrado:
        return jsonify({'erro': 'Aluno não encontrado.'}), 404
        
@alunos_blueprint.route('/alunos/', methods = ['POST'])
def create_aluno():
    try:
        dados = request.json
        response, status_code = adicionar_aluno(dados)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({'erro': 'Erro interno no servidor.'}), 500

@alunos_blueprint.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    dados = request.json
    try:
        atualizar_aluno(id, dados)
        aluno_atualizado = aluno_por_id(id)
        return jsonify({
            'message': 'Aluno atualizado com sucesso.',
            'aluno': aluno_atualizado
        }), 200
    except AlunoNaoEncontrado:
        return jsonify({'erro': 'Aluno não encontrado.'}), 404
        
@alunos_blueprint.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    try:
        excluir_aluno(id)
        return jsonify({'message': 'Aluno excluído com sucesso.'}), 200
    except AlunoNaoEncontrado:
        return jsonify({'erro': 'Aluno não encontrado.'}), 404