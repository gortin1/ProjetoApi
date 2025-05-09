from flask import Blueprint, request, jsonify
from turma.turma_model import turma_por_id, TurmaNaoEncontrada, listar_turmas, excluir_turma, adicionar_turma, atualizar_turma

turmas_blueprint = Blueprint("turma", __name__)

@turmas_blueprint.route('/turmas/', methods = ['GET'])
def get_turmas():
    return jsonify(listar_turmas())

@turmas_blueprint.route('/turmas/<int:id>', methods = ['GET'])
def get_turma(id):
    try:
        turma = turma_por_id(id)
        return jsonify(turma)
    except TurmaNaoEncontrada:
        return jsonify({'erro': 'Turma não encontrada'}), 404
               
@turmas_blueprint.route('/turmas/', methods = ['POST'])
def create_turma():
    try:
        dados = request.json
        response, status_code = adicionar_turma(dados)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({'error': 'Erro interno no servidor.'}), 500
        
@turmas_blueprint.route('/turmas/<int:id>', methods = ['PUT'])
def update_turma(id):
    dados = request.json
    try:
        atualizar_turma(id, dados)
        turma_atualizada = turma_por_id(id)
        return jsonify({
            'message': 'Turma atualizada com sucesso.',
            'turma': turma_atualizada
        }), 200
    except TurmaNaoEncontrada:
        return jsonify({'erro': 'Turma não encontrada'}), 404

@turmas_blueprint.route('/turmas/<int:id>', methods=['DELETE'])
def delete_turma(id):
    try:
        excluir_turma(id)
        return jsonify({'message': 'Turma excluída com sucesso.'}), 200
    except TurmaNaoEncontrada:
        return jsonify({'erro': 'Turma não encontrada'}), 404