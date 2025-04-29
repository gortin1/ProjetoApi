from flask import Blueprint, request, jsonify
from professor.professor_model import professor_por_id, ProfessorNaoEncontrado, listar_professores, excluir_professor, adicionar_professor, atualizar_professor

professores_blueprint = Blueprint("professor", __name__)


@professores_blueprint.route('/professor', methods = ['GET'])
def getProfessores():
    return jsonify(listar_professores())

@professores_blueprint.route('/professor/<int:id>', methods = ['GET'])
def getProfessor(id):
    try:
        professor = professor_por_id(id)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
            return jsonify({'Erro': f'Ocorreu um erro: Professor não encontrado'}, 404)
            
        
@professores_blueprint.route('/professor', methods = ['POST'])
def createProfessor():
        dados = request.json
        adicionar_professor(dados)
        return jsonify(dados)
        
@professores_blueprint.route('/professor/<int:id>', methods = ['PUT'])
def updateProfessor(id):
        dados = request.json
        try: 
            atualizar_professor(id, dados)
            return jsonify(professor_por_id(id))
        except ProfessorNaoEncontrado:
            return jsonify({'Erro': f'Ocorreu um erro: Professor não foi atualizado'}, 404)
                
@professores_blueprint.route('/professor/<int:id>', methods=['DELETE'])
def deleteProfessor(id):
    try:
        excluir_professor(id)
        return "", 204
    except ProfessorNaoEncontrado:
<<<<<<< HEAD
        return jsonify({'Erro': f'Ocorreu um erro: Professor não foi Deletado'}, 404)

        
=======
        return jsonify({'Erro': f'Ocorreu um erro: Professor não foi Deletado'}, 404)
>>>>>>> b539fc8f01d5657d876f10005467c94b4c3f46c3
