from flask_restx import Namespace, Resource, fields
from professor.professor_model import adicionar_professor, atualizar_professor, excluir_professor, listar_professores, professor_por_id 

professor_ns = Namespace("professor", description="Operações relacionadas aos professores")

professor_model = professor_ns.model("Professor", {
    "nome": fields.String(required=True, description="Nome do professor"),
    "idade": fields.String(required=True, description="Idade do professor"),
    "materia": fields.String(required=True, description="Matéria passada pelo professor"),
    "observacoes": fields.String(required=True, description="Observações sobre o professor")
    
})

professor_output_model = professor_ns.model("ProfessorOutput", {
    "id": fields.Integer(description="ID do professor"),
    "nome": fields.String(description="Nome do professor"),
    "idade": fields.Integer(description="Idade do professor"),
    "materia": fields.String(description="Matéria passada pelo professor"),
    "observacoes": fields.String(description="Observações sobre o professor")
    
})

@professor_ns.route("/")
class professorsResource(Resource):
    @professor_ns.marshal_list_with(professor_output_model)
    def get(self):
        """Lista todos os professores"""
        return listar_professores()

    @professor_ns.expect(professor_model)
    def post(self):
        """Cria um novo professor"""
        data = professor_ns.payload
        response, status_code = adicionar_professor(data)
        return response, status_code

@professor_ns.route("/<int:id_professor>")
class professorIdResource(Resource):
    @professor_ns.marshal_with(professor_output_model)
    def get(self, id_professor):
        """Obtém um professor pelo ID"""
        return professor_por_id(id_professor)

    @professor_ns.expect(professor_model)
    def put(self, id_professor):
        """Atualiza um professor pelo ID"""
        data = professor_ns.payload
        atualizar_professor(id_professor, data)
        return data, 200

    def delete(self, id_professor):
        """Exclui um professor pelo ID"""
        excluir_professor(id_professor)
        return {"message": "professor excluído com sucesso"}, 200