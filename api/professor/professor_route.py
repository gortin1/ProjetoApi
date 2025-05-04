from flask import Blueprint, request, jsonify
from professor.professor_model import professor_por_id, ProfessorNaoEncontrado, listar_professores, excluir_professor, adicionar_professor, atualizar_professor

professores_blueprint = Blueprint("professor", __name__)

@professores_blueprint.route('/professores/', methods = ['GET'])
def get_professores():
    return jsonify(listar_professores()), 200

@professores_blueprint.route('/professores/<int:id>', methods = ['GET'])
def get_professor(id):
    try:
        professor = professor_por_id(id)
        return jsonify(professor), 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado.'}), 404
           
@professores_blueprint.route('/professores/', methods = ['POST'])
def create_professor():
    try:
        dados = request.json
        response, status_code = adicionar_professor(dados)
        return jsonify(response), status_code
    except Exception as e:
        return jsonify({'erro': 'Erro interno no servidor.'}), 500
   
@professores_blueprint.route('/professores/<int:id>', methods = ['PUT'])
def update_professor(id):
    dados = request.json
    try: 
        atualizar_professor(id, dados)
        professor_atualizado = professor_por_id(id)
        return jsonify({
            'message': 'Professor atualizado com sucesso.',
            'professor': professor_atualizado
        }), 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado.'}), 404
                
@professores_blueprint.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    try:
        excluir_professor(id)
        return jsonify({'message': 'Professor excluído com sucesso.'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado.'}), 404