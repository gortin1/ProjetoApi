from flask import Blueprint, jsonify, request
<<<<<<< HEAD
from aluno.aluno_model import AlunoNaoEncontrado, listar_alunos, aluno_por_id, adicionar_aluno, atualizar_aluno, excluir_aluno, excluir_tudo
=======
from aluno.aluno_model import AlunoNaoEncontrado, listar_alunos, aluno_por_id, adicionar_aluno, atualizar_aluno, excluir_aluno
>>>>>>> b539fc8f01d5657d876f10005467c94b4c3f46c3

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/aluno', methods = ['GET'])
<<<<<<< HEAD
def alunos():
    return jsonify(listar_alunos())

@alunos_blueprint.route('/aluno/<int:id>', methods = ['GET'])
def alunos_por_id(id):
=======
def get_alunos():
    return jsonify(listar_alunos())
    

@alunos_blueprint.route('/aluno/<int:id>', methods = ['GET'])
def get_aluno(id):
>>>>>>> b539fc8f01d5657d876f10005467c94b4c3f46c3
    try:
        aluno = aluno_por_id(id)
        return jsonify(aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message':'Aluno não encontrado'}, 404)
        

@alunos_blueprint.route('/aluno', methods = ['POST'])
def criar_aluno():
    dados = request.json
    adicionar_aluno(dados)
<<<<<<< HEAD
    return jsonify(dados), 200 
=======
    return jsonify(dados), 201 
>>>>>>> b539fc8f01d5657d876f10005467c94b4c3f46c3


@alunos_blueprint.route('/aluno/<int:id>', methods=['PUT'])
def atualiza_aluno(id):
    dados = request.json
    try:
        atualizar_aluno(id, dados)
        return jsonify(aluno_por_id(id))
    except AlunoNaoEncontrado:
        return jsonify({'message':'Aluno não encontrado'}, 404)
        

@alunos_blueprint.route('/aluno/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    try:
        excluir_aluno(id)
        return '', 204 
    except AlunoNaoEncontrado:
<<<<<<< HEAD
        return jsonify({'message':'Aluno não encontrado'}, 404)
    
@alunos_blueprint.route('/aluno', methods=['DELETE'])
def deletar_todos():
    try:
        excluir_tudo()
        return '', 204 
    except AlunoNaoEncontrado:
=======
>>>>>>> b539fc8f01d5657d876f10005467c94b4c3f46c3
        return jsonify({'message':'Aluno não encontrado'}, 404)