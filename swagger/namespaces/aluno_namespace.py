from flask_restx import Namespace, Resource, fields
from aluno.aluno_model import listar_alunos, adicionar_aluno, atualizar_aluno, aluno_por_id, excluir_aluno

aluno_ns = Namespace('aluno','Operções relacionada aos alunos')

aluno_model = aluno_ns.model("Aluno",{
    "nome":fields.String(required=True,description="Nome do aluno"),
    "data_nascimento":fields.String(required= True, description="Data de nascimento do aluno (YYYY-MM-DD)"),
    "nota_primeiro_semestre": fields.Float(required=True, description= "Nota do primeiro semestre do aluno"),
    "nota_segundo_semestre": fields.Float(required=True, description= "Nota do segundo semestre do aluno"),
    "id_turma": fields.Integer(required=True, description= "Id da turma do aluno")
    })
aluno_output_model = aluno_ns.model("Aluno output",{
    "id": fields.Integer(description = "Id do aluno"),
    "nome": fields.String(description = "Nome do aluno"),
    "idade": fields.Integer(description = "Idade do aluno"),
    "turma_id": fields.Integer(description = "Id da turma do aluno"),
    "data_nascimento": fields.String(description = "Data de nascimento do aluno (YYYY-MM-DD)"),
    "nota_primeiro_semestre": fields.Float(description = "Nota do primeiro semestre do aluno"),
    "nota_segundo_semestre": fields.Float(description = "Nota do segundo semestre do aluno") ,
    "media_final": fields.Float(description = "Media final das notas do aluno")
})

@aluno_ns.route("/")
class AlunosResource(Resource):
    @aluno_ns.marshal_list_with(aluno_output_model)
    def get(self):
        """Lista todos os alunos"""
        return listar_alunos()
    @aluno_ns.expect(aluno_model)
    def post(self):
        """Cria um novo aluno"""
        data = aluno_ns.payload
        response, status_code = adicionar_aluno()
        return response, status_code
@aluno_ns.route("/<int:id>")
class AlunoResource(Resource):
    @aluno_ns.marshal_with(aluno_output_model)
    def get(self,id):
        """Obtém um aluno pelo ID"""
        return aluno_por_id(id)
    @aluno_ns.expect(aluno_model)
    def put(self,id):
        """Atualiza um aluno pelo ID"""
        data = aluno_ns.payload
        atualizar_aluno(id,data)
        return data, 200
    def delete(self,id):
        """Exclui um aluno pelo ID"""
        excluir_aluno(id)
        return {'message': "Aluno Excluido com sucesso"},200
    