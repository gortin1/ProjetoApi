from . import api
from swagger.namespaces.aluno_namespace import aluno_ns
from swagger.namespaces.professor_namespace import professor_ns
from swagger.namespaces.turma_namespace import turma_ns

def configure_swagger(app):
    api.init_app(app)
    api.add_namespace(aluno_ns, path="/aluno")