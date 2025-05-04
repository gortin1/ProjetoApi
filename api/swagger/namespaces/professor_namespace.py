from flask_restx import Namespace, Resource, fields
from professor.professor_model import adicionar_professor, atualizar_professor, excluir_professor, listar_professores, professor_por_id 

professores_ns = Namespace("professores", description="Operações relacionadas aos professores")

professor_model = professores_ns.model("Professor", {
    "nome": fields.String(required=True, description="Nome do professor"),
    "idade": fields.Integer(required=True, description="Idade do professor"),
    "materia": fields.String(required=True, description="Matéria"),
    "observacoes": fields.String(required=True, description="Observações")
})

professor_output_model = professores_ns.model("ProfessorOutput", {
    "id": fields.Integer(description="ID do professor"),
    "nome": fields.String(description="Nome do professor"),
    "idade": fields.Integer(description="Idade do professor"),
    "materia": fields.String(description="Matéria"),
    "observacoes": fields.String(description="Observações")
})

@professores_ns.route("/")
class ProfessoresResource(Resource):
    @professores_ns.marshal_list_with(professor_output_model)
    def get(self):
        """Lista todos os professores"""
        return listar_professores()

    @professores_ns.expect(professor_model)
    def post(self):
        """Cria um novo professor"""
        data = professores_ns.payload
        response, status_code = adicionar_professor(data)
        return response, status_code

@professores_ns.route("/<int:id_professor>")
class ProfessorIdResource(Resource):
    @professores_ns.marshal_with(professor_output_model)
    def get(self, id_professor):
        """Obtém um professor pelo ID"""
        return professor_por_id(id_professor)

    @professores_ns.expect(professor_model)
    def put(self, id_professor):
        """Atualiza um professor pelo ID"""
        data = professores_ns.payload
        atualizar_professor(id_professor, data)
        return data, 200

    def delete(self, id_professor):
        """Exclui um professor pelo ID"""
        excluir_professor(id_professor)
        return {"message": "Professor excluído com sucesso."}, 200