from flask_restx import Namespace, Resource, fields
from turma.turma_model import adicionar_turma, atualizar_turma, excluir_turma, listar_turmas, turma_por_id 

turma_ns = Namespace("turma", description="Operações relacionadas aos turma")

turma_model = turma_ns.model("turma", {
    "nome": fields.String(required=True, description="Nome do turma"),
    "idade": fields.String(required=True, description="Idade do turma"),
    "materia": fields.String(required=True, description="Matéria passada pelo turma"),
    "observacoes": fields.String(required=True, description="Observações sobre o turma")
    
})

turma_output_model = turma_ns.model("turmaOutput", {
    "id": fields.Integer(description="ID do turma"),
    "nome": fields.String(description="Nome do turma"),
    "idade": fields.Integer(description="Idade do turma"),
    "materia": fields.String(description="Matéria passada pelo turma"),
    "observacoes": fields.String(description="Observações sobre o turma")

})

@turma_ns.route("/")
class turmasResource(Resource):
    @turma_ns.marshal_list_with(turma_output_model)
    def get(self):
        """Lista todos os turmas"""
        return listar_turmas()

    @turma_ns.expect(turma_model)
    def post(self):
        """Cria um novo turma"""
        data = turma_ns.payload
        response, status_code = adicionar_turma(data)
        return response, status_code

@turma_ns.route("/<int:id_turma>")
class turmaIdResource(Resource):
    @turma_ns.marshal_with(turma_output_model)
    def get(self, id_turma):
        """Obtém um turma pelo ID"""
        return turma_por_id(id_turma)

    @turma_ns.expect(turma_model)
    def put(self, id_turma):
        """Atualiza um turma pelo ID"""
        data = turma_ns.payload
        atualizar_turma(id_turma, data)
        return data, 200

    def delete(self, id_turma):
        """Exclui um turma pelo ID"""
        excluir_turma(id_turma)
        return {"message": "turma excluído com sucesso"}, 200