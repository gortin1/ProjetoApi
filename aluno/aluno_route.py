from flask import Blueprint, jsonify, request
from aluno.aluno_model import AlunoNaoEncontrado, listar_alunos, aluno_por_id, adicionar_aluno, atualizar_aluno, excluir_aluno

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos', methods = ['GET'])
def get_alunos():
    return jsonify(listar_alunos())
    

@alunos_blueprint.route('/alunos/<int:id>', methods = ['GET'])
def get_aluno(id):
    try:
        aluno = aluno_por_id(id)
        return jsonify(aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message':'Aluno não encontrado'}, 404)
        

@alunos_blueprint.route('/alunos', methods = ['POST'])
def criar_aluno():
    dados = request.json
    adicionar_aluno(dados)
    return jsonify(dados), 201 


@alunos_blueprint.route('/alunos/<int:id>', methods=['PUT'])
def atualiza_aluno(id):
    dados = request.json
    try:
        atualizar_aluno(id, dados)
        return jsonify(aluno_por_id(id))
    except AlunoNaoEncontrado:
        return jsonify({'message':'Aluno não encontrado'}, 404)
        

@alunos_blueprint.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    try:
        excluir_aluno(id)
        return '', 204 
    except AlunoNaoEncontrado:
        return jsonify({'message':'Aluno não encontrado'}, 404)