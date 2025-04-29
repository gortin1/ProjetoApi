from flask import Blueprint, request, jsonify
from turma.turma_model import turma_por_id, TurmaNaoEncontrada, listar_turmas, excluir_turma, adicionar_turma, atualizar_turma

turmas_blueprint = Blueprint("turma", __name__)


@turmas_blueprint.route('/turma', methods = ['GET'])
def getTurmas():
    return jsonify(listar_turmas())

@turmas_blueprint.route('/turma/<int:id>', methods = ['GET'])
def getTurma(id):
    try:
        turma = turma_por_id(id)
        return jsonify(turma)
    except TurmaNaoEncontrada:
            return jsonify({'Erro': f'Ocorreu um erro: Turma não encontrado'}, 404)
            
        
@turmas_blueprint.route('/turma', methods = ['POST'])
def createTurma():
        dados = request.json
        adicionar_turma(dados)
        return jsonify(dados)
        
@turmas_blueprint.route('/turma/<int:id>', methods = ['PUT'])
def updateTurma(id):
        dados = request.json
        try: 
            atualizar_turma(id, dados)
            return jsonify(turma_por_id(id))
        except TurmaNaoEncontrada:
            return jsonify({'Erro': f'Ocorreu um erro: Turma não foi atualizado'}, 404)
                
@turmas_blueprint.route('/turma/<int:id>', methods=['DELETE'])
def deleteTurma(id):
    try:
        excluir_turma(id)
        return "", 204
    except TurmaNaoEncontrada:
<<<<<<< HEAD
        return jsonify({'Erro': f'Ocorreu um erro: Turma não foi Deletado'}, 404)

        
=======
        return jsonify({'Erro': 'Ocorreu um erro: Turma não foi Deletado'}), 404
>>>>>>> b539fc8f01d5657d876f10005467c94b4c3f46c3
