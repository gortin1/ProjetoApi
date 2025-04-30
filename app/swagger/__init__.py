from flask_restx import Api

api = Api(
    version='1.0',
    title='Api de gestão escolar',
    description='Documentação da API para alunos,professores e turmas.',
    doc="/docs",
    mask_swagger= False,
    prefix="/api"
)