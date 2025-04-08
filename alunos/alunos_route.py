from flask import Blueprint, jsonify, request
from .alunos_model import alunoNaoEncontrado, aluno_por_id, adicionar_aluno,atualizar_aluno,listar_aluno,excluir_aluno

alunos_blueprint =  Blueprint('aluno', __name__)

@alunos_blueprint.route('/aluno', methods=['GET'])
def getalunos():
    return jsonify(listar_aluno())

@alunos_blueprint.route('/aluno/<int:id_aluno>', methods=['GET'])
def getAlunos(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return jsonify(aluno)
    except alunoNaoEncontrado:
        return jsonify({'message':'Aluno não encontrado'}),404

@alunos_blueprint.route('/aluno', methods=['POST'])
def create_aluno():
    data = request.json
    adicionar_aluno(data)
    return jsonify(data),201

@alunos_blueprint.route('/aluno/<int:id_aluno>', methods=['PUT'])
def update_aluno(id_aluno):
    data = request.json
    
    try:
        atualizar_aluno(id_aluno,data)
        return jsonify(aluno_por_id(id_aluno))
    except alunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}),404

@alunos_blueprint.route('/aluno/<int:id_aluno>', methods=['DELETE'])
def delete_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return '', 204
    except alunoNaoEncontrado:
        return jsonify({'message': 'Aluno Não Encontrado'}),404
    
@alunos_blueprint.route('/aluno/<int:id_aluno>', methods=['PATCH'])
def patch_aluno(id_aluno):
    data = request.json
    try:
        atualizar_aluno(id_aluno,data)
        return jsonify(aluno_por_id(id_aluno))
    except alunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}),404