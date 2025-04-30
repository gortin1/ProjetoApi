from flask import Blueprint, request, jsonify
from turma.turma_model import turma_por_id, TurmaNaoEncontrada, listar_turmas, excluir_turma, adicionar_turma, atualizar_turma

turmas_blueprint = Blueprint("turma", __name__)


@turmas_blueprint.route('/turmas', methods = ['GET'])
def getTurmas():
    return jsonify(listar_turmas())

@turmas_blueprint.route('/turmas/<int:id>', methods = ['GET'])
def getTurma(id):
    try:
        turma = turma_por_id(id)
        return jsonify(turma)
    except TurmaNaoEncontrada:
            return jsonify({'Erro': f'Ocorreu um erro: Turma não encontrado'}, 404)
            
        
@turmas_blueprint.route('/turmas', methods = ['POST'])
def createTurma():
        dados = request.json
        adicionar_turma(dados)
        return jsonify(dados)
        
@turmas_blueprint.route('/turmas/<int:id>', methods = ['PUT'])
def updateTurma(id):
        dados = request.json
        try: 
            atualizar_turma(id, dados)
            return jsonify(turma_por_id(id))
        except TurmaNaoEncontrada:
            return jsonify({'Erro': f'Ocorreu um erro: Turma não foi atualizado'}, 404)
                
@turmas_blueprint.route('/turmas/<int:id>', methods=['DELETE'])
def deleteTurma(id):
    try:
        excluir_turma(id)
        return "", 204
    except TurmaNaoEncontrada:
        return jsonify({'Erro': 'Ocorreu um erro: Turma não foi Deletado'}), 404