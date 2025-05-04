from config import app, db
from aluno.aluno_route import alunos_blueprint
from turma.turma_route import turmas_blueprint
from professor.professor_route import professores_blueprint
from swagger.swagger_config import configure_swagger
             
app.register_blueprint(alunos_blueprint, url_prefix='/api')
app.register_blueprint(professores_blueprint, url_prefix='/api')
app.register_blueprint(turmas_blueprint, url_prefix='/api')

configure_swagger(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])