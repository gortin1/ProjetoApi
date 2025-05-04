from flask import Blueprint, request, jsonify
from professor.professor_model import professor_por_id, ProfessorNaoEncontrado, listar_professores, excluir_professor, adicionar_professor, atualizar_professor

professores_blueprint = Blueprint("professor", __name__)

@professores_blueprint.route('/professores', methods = ['GET'])
def get_professores():
    return jsonify(listar_professores())

@professores_blueprint.route('/professores/<int:id>', methods = ['GET'])
def get_professor(id):
    try:
        professor = professor_por_id(id)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado'}), 404
           
@professores_blueprint.route('/professores', methods = ['POST'])
def create_professor():
    dados = request.json
    adicionar_professor(dados)
    return jsonify(dados), 201
   
@professores_blueprint.route('/professores/<int:id>', methods = ['PUT'])
def update_professor(id):
    dados = request.json
    try: 
        atualizar_professor(id, dados)
        return jsonify(professor_por_id(id))
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado'}), 404
                
@professores_blueprint.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    try:
        excluir_professor(id)
        return "", 204
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado'}), 404